from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from core.config import *


class OpenSourceLicense(QDialog):

    def __init__(self, parent=None):
        super(OpenSourceLicense, self).__init__(parent)
        self.setWindowFlags(Qt.Popup)

        layout = QFormLayout(self)
        textbox = QPlainTextEdit()
        textbox.setPlainText(OPEN_SOURCE_LICENSE)
        textbox.setReadOnly(True)
        textbox.setFixedWidth(720)
        textbox.setFixedHeight(640)
        layout.addRow(textbox)

        self.setLayout(layout)
        self.show()


class ActivateKey(QDialog):

    def __init__(self, parent=None):
        super(ActivateKey, self).__init__(parent)

        self.setWindowTitle(f"{NAME} 테스터 인증 키 입력")

        layout = QFormLayout(self)
        _input = QLineEdit()
        # noinspection SpellCheckingInspection
        _input.setInputMask(">0000-0000-AAAA-AAAA;_")
        layout.addRow(_input)

        self.setLayout(layout)
        self.show()
