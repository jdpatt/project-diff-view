"""Default settings or constants for projectdiffview."""
import filecmp
import logging
from dataclasses import dataclass
from pathlib import Path

from PySide2 import QtCore, QtGui

LOG = logging.getLogger("projectdiffview.config")


@dataclass
class Configuration:
    """Container to store settings for ProjectDiffView."""

    template_directory = Path(__file__).parents[1].joinpath("template")
    debug_template_directory = Path(__file__).parents[1].joinpath("tests", "data", "template")
    ignored = filecmp.DEFAULT_IGNORES + [".keep"]

    color_deleted = QtGui.QColor(255, 162, 137)
    color_new = QtGui.QColor(68, 188, 145)
    color_added = QtGui.QColor(27, 157, 226)

    def load_config(self):
        """Load the settings into ProjectDiffView."""
        settings = QtCore.QSettings()
        LOG.info("Loading Configuration...")
        for item in self.__dict__:
            self.__dict__[item] = settings.value(item)

    def save_config(self):
        """Save the settings out from ProjectDiffView."""
        LOG.info("Saving Configuration...")
        settings = QtCore.QSettings()
        for key, value in self.__dict__.items():
            LOG.debug(f"Saving {value} to {key}")
            settings.setValue(key, value)
        settings.sync()
