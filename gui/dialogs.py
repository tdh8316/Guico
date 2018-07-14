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
        textbox.setFixedWidth(720)
        textbox.setFixedHeight(640)
        layout.addRow(textbox)

        self.setLayout(layout)
        self.show()
