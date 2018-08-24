import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

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


class VariableNameEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFont(QFont("맑은 고딕", 9))
        # self.setFixedSize(100, 30)

    def focusInEvent(self, event):
        # self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        # self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)

    def textToVariableName(self):

        return self.text().replace(" ", "_")

    def setVariableNameToText(self, s: str):

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
        self.setText(os.path.basename(path))
        self.image_path = path

    def WhereIsImage(self):
        if os.path.dirname(CONF["FILE_PATH"]) == os.path.dirname(self.image_path):
            return os.path.basename(self.image_path)
        return self.image_path
