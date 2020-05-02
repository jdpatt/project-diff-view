"""Default settings or constants for projectdiffview."""
import filecmp
from pathlib import Path

from PySide2 import QtGui

TEMPLATE_DIRECTORY = Path(__file__).parents[1].joinpath("template")
DEBUG_TEMPLATE_DIRECTORY = Path(__file__).parents[1].joinpath("tests", "data", "template")
IGNORED = filecmp.DEFAULT_IGNORES + [".keep"]

COLOR_DELETED = QtGui.QColor(255, 162, 137)
COLOR_NEW = QtGui.QColor(68, 188, 145)
COLOR_ADDED = QtGui.QColor(27, 157, 226)
