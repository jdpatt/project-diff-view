"""Default settings or constants for projectdiffview."""
import filecmp
import logging
from pathlib import Path

from PySide2 import QtCore, QtGui

LOG = logging.getLogger("projectdiffview.config")


class Configuration:
    """Container to store settings for ProjectDiffView."""
    def __init__(self):
        self.template_directory = Path(__file__).parents[1].joinpath("template")
        self.debug_template_directory = Path(__file__).parents[1].joinpath("tests", "data", "template")
        self.ignored = filecmp.DEFAULT_IGNORES + [".keep"]

        self.color_deleted = QtGui.QColor(255, 162, 137)
        self.color_new = QtGui.QColor(68, 188, 145)
        self.color_added = QtGui.QColor(27, 157, 226)

    def load_config(self):
        """Load the settings into ProjectDiffView."""
        settings = QtCore.QSettings()
        LOG.info("Loading Configuration...")
        for item in self.__dict__:
            value = settings.value(item)
            if value:
                self.__dict__[item] = value

    def save_config(self):
        """Save the settings out from ProjectDiffView."""
        LOG.info("Saving Configuration...")
        settings = QtCore.QSettings()
        for key, value in self.__dict__.items():
            LOG.debug(f"Saving {value} to {key}")
            settings.setValue(key, value)
        settings.sync()
