"""Entry Point when called by python -m projectdiffview."""
import sys

from projectdiffview import projectdiffview, prompts
from PySide2.QtWidgets import QApplication


def main():  # pragma: no cover
    """Gui entry point."""
    app = QApplication([])
    gui = projectdiffview.projectdiffview(verbose=True)
    gui.show()
    prompts.warn_user()
    app.exec_()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
