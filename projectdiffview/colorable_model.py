"""Model to watch the filesystem and report it to the QTreeView."""
from pathlib import Path

from PySide2 import QtCore, QtGui, QtWidgets


class ColorableFileSystemModel(QtWidgets.QFileSystemModel):
    """Sub-class QFileSystemModel to allow colored items."""

    def __init__(self, view):
        super().__init__()
        self.view = view

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """Return the data stored under the given role for the item referred to by the index."""
        if role == QtCore.Qt.BackgroundRole:
            file_path = Path(self.filePath(index))
            if file_path in self.view.working_only:
                return QtGui.QColor(self.view.config.color_new)
        return super().data(index, role)
