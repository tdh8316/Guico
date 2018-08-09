from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from gui.widgets.customized import QDMLineEdit


def content_KEY_INPUT(self):
    self.layout = QVBoxLayout()
    self.wdg_label = QLabel("NotImplementedError")  # 그거 종류 그 뭐냐 하여튼 그거
    self.wdg_label.setAlignment(Qt.AlignCenter)

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.wdg_label)
    self.setLayout(self.layout)
    # self.layout.addWidget(self.wdg_label)