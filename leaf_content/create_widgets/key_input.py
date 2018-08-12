from PyQt5.QtWidgets import *

from core.constants import ALL_KEYS
from leaf_content.default import KEY_INPUT


def content_KEY_INPUT(self):
    self.layout = QVBoxLayout()
    # self.wdg_label = QLabel("NotImplementedError")  # 그거 종류 그 뭐냐 하여튼 그거
    # self.wdg_label.setAlignment(Qt.AlignCenter)
    self.key = QComboBox()
    self.key.addItems(ALL_KEYS)
    self.key.setEditable(True)
    self.key.completer().setCompletionMode(QCompleter.PopupCompletion)
    self.key.currentTextChanged.connect(lambda: changeTitle(self))

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.key)
    self.setLayout(self.layout)


def changeTitle(self):
    self.node.title = f"[{self.key.currentText()}] {KEY_INPUT}"
