"""Widget to allow the user to edit the highlighting colors."""
from PySide2 import QtCore, QtWidgets


class SettingsDialog(QtWidgets.QDialog):
    """Settings Menu for Project Diff View."""
    def __init__(self, configuration):
        super(SettingsDialog, self).__init__()

        self.setWindowTitle("Settings")
        self.config = configuration

        q_button_box = QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel

        self.buttonBox = QtWidgets.QDialogButtonBox(q_button_box)
        self.buttonBox.accepted.connect(self.save_config)
        self.buttonBox.rejected.connect(self.reject)

        self.deleted = self.config.color_deleted
        self.new = self.config.color_new
        self.added = self.config.color_added

        self.deleted_button = QtWidgets.QPushButton(self.deleted.name())
        self.deleted_button.setStyleSheet("background-color: %s;" % self.deleted.name())
        self.new_button = QtWidgets.QPushButton(self.new.name())
        self.new_button.setStyleSheet("background-color: %s;" % self.new.name())
        self.added_button = QtWidgets.QPushButton(self.added.name())
        self.added_button.setStyleSheet("background-color: %s;" % self.added.name())

        layout = QtWidgets.QFormLayout()
        # layout.addRow("Template Directory", self.update_directory)
        layout.addRow("Color Added", self.added_button)
        layout.addRow("Color Deleted", self.deleted_button)
        layout.addRow("Color New", self.new_button)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

        # Connect Signal/Slots
        self.deleted_button.clicked.connect(self.change_deleted_color)
        self.new_button.clicked.connect(self.change_new_color)
        self.added_button.clicked.connect(self.change_added_color)

    def __str__(self):
        return f"Widget for {self.graphic.__class__.__name__}"

    # @QtCore.Slot()
    # def update_directory(self):
    #     pass

    @QtCore.Slot()
    def change_deleted_color(self):
        """Update the btn label after selection and tell the gui to the update the background."""
        color_picker = QtWidgets.QColorDialog(self.deleted)
        new_color = color_picker.getColor()
        if new_color.isValid():
            self.deleted = new_color
            self.deleted_button.setText(self.deleted.name())
            self.deleted_button.setStyleSheet("background-color: %s;" % self.deleted.name())

    @QtCore.Slot()
    def change_new_color(self):
        """Update the btn label after selection and tell the gui to the update the background."""
        color_picker = QtWidgets.QColorDialog(self.new)
        new_color = color_picker.getColor()
        if new_color.isValid():
            self.new = new_color
            self.new_button.setText(self.new.name())
            self.new_button.setStyleSheet("background-color: %s;" % self.new.name())

    @QtCore.Slot()
    def change_added_color(self):
        """Update the btn label after selection and tell the gui to the update the background."""
        color_picker = QtWidgets.QColorDialog(self.added)
        new_color = color_picker.getColor()
        if new_color.isValid():
            self.added = new_color
            self.added_button.setText(self.added.name())
            self.added_button.setStyleSheet("background-color: %s;" % self.added.name())

    @QtCore.Slot()
    def save_config(self):
        """Update the configuration values and save it."""
        self.config.color_deleted = self.deleted
        self.config.color_new = self.new
        self.config.color_added = self.added
        self.config.save_config()
        self.accept()
