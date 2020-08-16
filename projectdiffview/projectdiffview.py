"""Project Directory Utility."""
import distutils.dir_util as dir_util
import filecmp
import os
import platform
import shutil
import time
import typing
import webbrowser
from pathlib import Path

from PySide2 import QtCore, QtWidgets

import projectdiffview.folder as folder
import projectdiffview.prompts as prompts
from projectdiffview import __version__, gui, logger
from projectdiffview.checkable_model import CheckableFileSystemModel
from projectdiffview.colorable_model import ColorableFileSystemModel
from projectdiffview.configuration import Configuration
from projectdiffview.settings_widget import SettingsDialog


def working_directory_set(method):
    """Make sure the working directory is set before copy operations."""
    # pylint: disable=R1710
    def wrapper(self, *method_args, **method_kwargs):
        if self.working_directory:
            return method(self, *method_args, **method_kwargs)
        self.log.error("Working Directory not set.")
        prompts.error("Working Directory not set.", close_app=False)

    return wrapper


class ProjectDiffView(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    """Main powertree Window."""

    # pylint: disable=R0902

    def __init__(self, verbose: bool = False, debug: bool = False):
        QtWidgets.QMainWindow.__init__(self)
        self.log = logger.setup_logger(
            "projectdiffview", "projectdiffview.log", is_verbose=verbose
        )
        self.setupUi(self)
        self.config = Configuration()
        self.config.load_config()

        # Setup the rest of the GUI.
        self.setWindowTitle("Project Directory Utility")
        self.menubar.setNativeMenuBar(False)  # Until Qt fixes QMenu for Catalina
        self.connect_actions()

        # Setup Logging features
        thread_log = logger.ThreadLogHandler()
        self.log.addHandler(thread_log)
        thread_log.new_record.connect(self.log_message)
        self.log.info(f"Python Version: {platform.python_version()}")
        self.log.info(f"Utility Version: {__version__}")

        # Lists of Complete Paths
        self.common: list = []
        self.template_only: list = []
        self.working_only: list = []

        self.working_model = ColorableFileSystemModel(self)
        self.working_directory: typing.Optional[Path] = None

        self.template_model = CheckableFileSystemModel(self)

        if debug:
            # Use the local path under tests/data.
            template_dir = self.config.debug_template_directory.resolve()
        else:
            template_dir = self.resolve_network_or_local_template()

        self.template_directory: Path = self.load_template_directory(template_dir)

        self.cleanup_has_run: bool = False

    def connect_actions(self) -> None:
        """Connect all the GUI elements to the business logic."""
        self.actionExit.triggered.connect(quit_app)
        self.actionSettings.triggered.connect(self.update_settings)
        self.actionDocumentation.triggered.connect(documentation)
        self.browse.clicked.connect(self.browse_for_folder)
        self.directory_path.returnPressed.connect(self.directory_path_was_edited)
        self.add_selected.clicked.connect(self.copy_selected)
        self.copy_template.clicked.connect(self.copy_template_folder)
        self.cleanup_working.clicked.connect(self.cleanup_working_folder)

    def log_message(self, level, msg: str) -> None:
        """Log any logger messages via the slot/signal mechanism so that its thread safe."""
        del level  # Unused
        self.statusbar.showMessage(msg, 5000)  # ms

    def browse_for_folder(self) -> None:
        """Display a FileDialog window and allow the user to navigate to the project folder."""
        new_directory = Path(
            QtWidgets.QFileDialog.getExistingDirectory(
                self,
                "Select the Project Directory",
                "",
                QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks,
            )
        )
        if new_directory.exists() and new_directory.is_dir():
            self.working_directory = new_directory
            self.directory_path.setText(str(self.working_directory))
            self.load_working_directory()

    def directory_path_was_edited(self) -> None:
        """Update the path since the QLineEdit changed."""
        new_directory = Path(self.directory_path.text())
        if new_directory.exists() and new_directory.is_dir():
            self.working_directory = new_directory
            self.load_working_directory()

    def load_template_directory(self, directory: Path) -> Path:
        """Read in the template directory into the template tree."""
        if directory and not directory.exists():
            self.log.error(f"Template Not Found: {directory}")
            prompts.error("Error: Template Not Found")
        directory_str = str(directory)

        # Set the Version Text
        self.template_version.setText(folder.folder_version(directory))

        # Create the Template Model
        self.template_model.setResolveSymlinks(False)
        self.template_model.setRootPath(directory_str)

        # Update the Tree
        self.template_tree.setModel(self.template_model)
        self.template_tree.setRootIndex(self.template_model.index(directory_str))
        self.template_tree.header().resizeSection(0, 250)
        self.template_tree.hideColumn(1)  # Size

        self.log.info(f"Template Directory: {directory_str}")
        return directory

    def load_working_directory(self) -> None:
        """Read in the working directory into the working tree."""
        directory = str(self.working_directory)
        self.log.info(f"Loading Directory: {directory}")

        # Set the Version Text
        self.directory_version.setText(folder.folder_version(self.working_directory))

        # Create the Working Model
        self.working_model.setResolveSymlinks(False)
        self.working_model.setRootPath(directory)

        # Update the Tree
        self.working_tree.setModel(self.working_model)
        self.working_tree.setRootIndex(self.working_model.index(directory))
        self.working_tree.header().resizeSection(0, 250)
        self.working_tree.hideColumn(1)  # Size

        self.cleanup_has_run = False

        self.get_folder_differences()

    def get_folder_differences(self) -> None:
        """Compare the template to the working directory and update the tree visuals."""
        dir_cmp = filecmp.dircmp(
            str(self.template_directory), str(self.working_directory), ignore=self.config.ignored
        )
        self.common, self.template_only, self.working_only = folder.recursively_compare_folders(
            dir_cmp
        )

    @working_directory_set
    def copy_template_folder(self) -> None:
        """Copy the entire template folder into the working directory."""
        confirmed = prompts.confirm_action(
            "Are you sure?", "Make sure the directory is empty or this may overwrite files."
        )
        if confirmed:
            self.log.debug("Copying template to working directory.")
            dir_util.copy_tree(
                str(self.template_directory),
                str(self.working_directory),
                preserve_symlinks=True,
                update=True,
            )
            self.get_folder_differences()

    @working_directory_set
    def copy_selected(self) -> None:
        """Copy the selected items from the template into the working directory."""
        items_to_copy = [
            Path(self.template_model.filePath(key)).resolve()
            for key, value in self.template_model.checks.items()
            if value == QtCore.Qt.CheckState.Checked
        ]
        confirmed = prompts.confirm_action(
            "Are you sure?",
            "This may overwrite files.",
            detail="Files to Copy:\n" + "\n".join([str(path) for path in items_to_copy]),
        )
        if confirmed:
            for old_filepath in items_to_copy:
                new_filepath = Path(
                    str(old_filepath).replace(
                        str(self.template_directory), str(self.working_directory)
                    )
                )
                if Path(old_filepath).is_dir():
                    os.makedirs(new_filepath, exist_ok=True)
                else:
                    os.makedirs(
                        new_filepath.parent, exist_ok=True
                    )  # Create any sub directories to path.
                    shutil.copy2(old_filepath, new_filepath, follow_symlinks=False)

    @working_directory_set
    def cleanup_working_folder(self) -> None:
        """Collect all the files to be cleaned and if confirmed, clean the working folder.

        Remove identical paths that have not changed from the template and
        delete any empty directories.

        If a sub folder has a new file in it, do not remove it.  Only remove paths
        that are indentical to the template.
        """
        if self.cleanup_has_run:
            prompts.error("Folder has already been cleaned.", close_app=False)
            return
        total = 0
        self.get_folder_differences()
        # Collect the files and folders that would be deleted.
        files_to_delete = folder.get_unchanged_files(self.common)

        # Generate the detail content
        detail_str = "Files to be deleted:\n\n"
        if files_to_delete:
            total += len(files_to_delete)
            for file_name in files_to_delete:
                detail_str += f"\t{file_name}\n"

        confirmed = prompts.confirm_action(
            "Are you sure?",
            f"This will permanently delete {total} files and any empty folders.",
            detail=detail_str,
        )
        if confirmed:
            for filepath in files_to_delete:
                try:
                    filepath.unlink()
                except FileNotFoundError:
                    self.log.error(f"Unabled to delete {filepath}")

            time.sleep(1)

            for folder_name in folder.get_empty_folders(self.working_directory):
                try:
                    folder_name.rmdir()
                except OSError:
                    self.log.error(f"Unabled to delete {folder_name}")

            time.sleep(1)
            self.get_folder_differences()
            self.cleanup_has_run = True

    def resolve_network_or_local_template(self) -> Path:
        """Test to see if the network path exits or return the local template."""
        network_dir = self.config.template_directory
        if network_dir.exists():
            return network_dir
        return Path(__file__).parents[1].joinpath("template").resolve()

    def update_settings(self) -> None:
        """Update the program's settings."""
        dialog = SettingsDialog(self.config)
        dialog.exec_()

def quit_app() -> None:
    """Close the application."""
    QtCore.QCoreApplication.instance().quit()

def documentation() -> None:
    """Open the documentation for powertree."""
    webbrowser.open("https://eng.plexus.com/git/projects/PLXSSPF/repos/projectdiffview/browse")
