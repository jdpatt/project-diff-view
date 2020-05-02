"""User prompts that the GUI may use."""
import sys

from PySide2 import QtWidgets


def confirm_action(title, informative=None, detail=None) -> bool:
    """Prompt the user to confirm the action."""
    prompt = QtWidgets.QMessageBox()
    prompt.setText(title)
    if informative:
        prompt.setInformativeText(informative)
    if detail:
        prompt.setDetailedText(detail)
    prompt.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
    prompt.setDefaultButton(QtWidgets.QMessageBox.Cancel)

    for button in prompt.buttons():
        if prompt.buttonRole(button) == QtWidgets.QMessageBox.ActionRole:
            button.click()
            break

    text_boxes = prompt.findChildren(QtWidgets.QTextEdit)
    if text_boxes:
        text_boxes[0].setFixedSize(800, 300)

    if prompt.exec() == QtWidgets.QMessageBox.Yes:
        return True
    return False


def warn_user() -> None:
    """Prompt the user and let them know the risks."""
    prompt = QtWidgets.QMessageBox()
    prompt.setText("Warning: Inproper use can lead to deleted files.")
    prompt.setInformativeText("Backup the project folder before using this application.")
    prompt.setStandardButtons(QtWidgets.QMessageBox.Ok)
    prompt.setDefaultButton(QtWidgets.QMessageBox.Ok)
    prompt.setIcon(QtWidgets.QMessageBox.Warning)
    prompt.exec()


def error(error_message: str, close_app: bool = True) -> None:
    """Prompt the user with the error message and optionally close the app."""
    prompt = QtWidgets.QMessageBox()
    prompt.setText(error_message)
    prompt.setStandardButtons(QtWidgets.QMessageBox.Ok)
    prompt.setDefaultButton(QtWidgets.QMessageBox.Ok)
    prompt.setIcon(QtWidgets.QMessageBox.Critical)
    prompt.exec()
    if close_app:
        sys.exit(1)  # Non-Zero Return Code
