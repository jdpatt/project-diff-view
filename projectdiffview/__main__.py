"""Entry Point when called by python -m projectdiffview."""
import sys

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

from projectdiffview import projectdiffview, prompts


def main():  # pragma: no cover
    """Gui entry point."""
    app = QApplication([])
    QCoreApplication.setOrganizationName("jdpatt")
    QCoreApplication.setApplicationName("project-diff-view")
    gui = projectdiffview.ProjectDiffView(verbose=True)
    gui.show()
    prompts.warn_user()
    app.exec_()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
