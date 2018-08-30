import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core import script_variables
from core.config import CONF

app = None


def initialize(p):
    global app
    app = p


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

    def keyPressEvent(self, *args, **kwargs):
        super().keyPressEvent(*args, **kwargs)
        app.signal_change_editor(True)


class QDMLineEdit(QLineEdit):
    def focusInEvent(self, event):
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)

    def keyPressEvent(self, *args, **kwargs):
        super().keyPressEvent(*args, **kwargs)
        app.signal_change_editor(True)


class Completer(QCompleter):

    def __init__(self, *__args):
        super().__init__(*__args)


class VariableNameEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFont(QFont("맑은 고딕", 9))
        self._completer = QCompleter(list(script_variables.globals.keys()), self)
        self.setCompleter(self._completer)
        self.color_palette = QPalette()
        # self.completer = QCompleter(list(script_variables.globals.keys()), self)
        # self.completer.setCompletionMode(QCompleter.InlineCompletion)
        # self.setFixedSize(100, 30)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if self.text() not in tuple(script_variables.globals.keys()):
            self.setToolTip(f"{self.text()} 그런 이름의 변수가 없습니다.")
            self.color_palette.setColor(QPalette.Text, Qt.red)
        else:
            self.color_palette.setColor(QPalette.Text, Qt.white)
        self.setPalette(self.color_palette)
        app.signal_change_editor(True)

    def focusInEvent(self, event):
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        # self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)
        self.setText(self.text().replace(" ", "_"))

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

    def keyPressEvent(self, *args, **kwargs):
        super().keyPressEvent(*args, **kwargs)
        app.signal_change_editor(True)
