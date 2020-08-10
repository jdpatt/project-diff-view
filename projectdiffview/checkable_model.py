"""Model to watch the filesystem and report it to the QTreeView."""
from pathlib import Path

from PySide2 import QtCore, QtGui, QtWidgets


class CheckableFileSystemModel(QtWidgets.QFileSystemModel):
    """Sub-class QFileSystemModel to allow checkable items."""

    def __init__(self, view):
        super().__init__()
        self.checks = {}
        self.view = view
        # The template shouldn't change, so we can avoid the performance hit.
        self.setOption(QtWidgets.QFileSystemModel.DontWatchForChanges, on=False)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """Return the data stored under the given role for the item referred to by the index."""
        if role == QtCore.Qt.BackgroundRole:
            file_path = Path(self.filePath(index))
            if file_path in self.view.template_only:
                return QtGui.QColor(self.view.config.color_deleted)
        elif role == QtCore.Qt.CheckStateRole and index.column() == 0:
            return self.check_state(index)

        return super().data(index, role)

    def flags(self, index):
        """Return the item flags for the given index."""
        return super().flags(index) | QtCore.Qt.ItemIsUserCheckable

    def check_state(self, index):
        """Return the current checked state."""
        if index in self.checks:
            return self.checks[index]
        return QtCore.Qt.CheckState.Unchecked

    def setData(self, index, value, role):
        """Set the role data for the item at index to value."""
        if role == QtCore.Qt.CheckStateRole and index.column() == 0:
            self.checks[index] = value
            if self.hasChildren(index):
                self.recursively_check_files_and_folders(index, value)
            self.dataChanged.emit(index, index)
            return True
        return super().setData(index, value, role)

    def recursively_check_files_and_folders(self, index, value=QtCore.Qt.CheckState.Checked):
        """Check the files and folders under the item checked."""
        path = self.filePath(index)
        dir_iterator = QtCore.QDirIterator(path, self.filter() | QtCore.QDir.NoDotAndDotDot)
        while dir_iterator.hasNext():
            child_index = self.index(dir_iterator.next())
            self.setData(child_index, value, QtCore.Qt.CheckStateRole)
            self.recursively_check_files_and_folders(child_index, value)
