from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from core.constants import ALL_KEYS
from contents.default import KEY_INPUT


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


def content_KEY_NOT_INPUT(self):
    self.layout = QVBoxLayout()
    self.wdg_label = QLabel("키 입력이 없을 때")
    self.wdg_label.setAlignment(Qt.AlignCenter)
    self.setToolTip("이 시작점에 연결된 잎들은 눌려진 키가 있다면 실행되지 않습니다.")

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.wdg_label)
    self.setLayout(self.layout)


def changeTitle(self):
    self.node.title = f"[{self.key.currentText()}] {KEY_INPUT}"
