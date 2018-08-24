import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core import script_variables
from core.config import CONF


def NotImplementationWidget(self):
    self.layout = QVBoxLayout()
    self.wdg_label = QLabel("NotImplementation")  # 그거 종류 그 뭐냐 하여튼 그거
    self.wdg_label.setAlignment(Qt.AlignCenter)

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.wdg_label)
    self.setLayout(self.layout)


class QDMTextEdit(QPlainTextEdit):
    def focusInEvent(self, event):
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)


class QDMLineEdit(QLineEdit):
    def focusInEvent(self, event):
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)


class Completer(QCompleter):

    def __init__(self, *__args):
        super().__init__(*__args)


class VariableNameEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFont(QFont("맑은 고딕", 9))
        self._completer = QCompleter(list(script_variables.globals.keys()), self)
        self.setCompleter(self._completer)
        # self.completer = QCompleter(list(script_variables.globals.keys()), self)
        # self.completer.setCompletionMode(QCompleter.InlineCompletion)
        # self.setFixedSize(100, 30)

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.setFixedSize(90, 30)

    def focusOutEvent(self, event):
        # self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)
        self.setText(self.text().replace(" ", "_"))
        self.setFixedSize(60, 30)

    def textToVariableName(self):
        return self.text().replace(" ", "_")

    def setVariableNameFromText(self, s: str):
        self.setText(s.replace("_", " "))


class ImagePathLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_path: str = str()

        self.setFont(QFont("맑은 고딕", 9))
        # self.setFixedSize(100, 30)

    def focusInEvent(self, event):
        # self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        # self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)

    def setPath(self, path):
        if os.path.dirname(path) == str():
            path = "%s/%s" % (os.path.dirname(CONF["FILE_PATH"]), path)
        self.setText(os.path.basename(path))
        self.image_path = path

    def WhereIsImage(self):
        if CONF["FILE_PATH"] is None:
            return False
        if os.path.dirname(CONF["FILE_PATH"]) == os.path.dirname(self.image_path):
            return os.path.basename(self.image_path)
        return self.image_path

    def enterEvent(self, *args, **kwargs):
        self.setToolTip(self.image_path)
