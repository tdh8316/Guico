from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QLabel, QVBoxLayout

from gui.widgets.customized import QDMLineEdit


def content_DRAW_TEXT(self):
    self.layout = QGridLayout()
    self.textbox = QDMLineEdit("")  # 그 텍스트박스 그거임
    self.textbox.setPlaceholderText("뭐라고 말할까?")
    self.textbox.setFont(QFont("맑은 고딕", 9))
    self.position = QDMLineEdit("0,0")  # 그 텍스트박스 그거임
    # self.position.setMaxLength(3)
    self.position.setFont(QFont("맑은 고딕", 9))

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.layout)
    self.layout.addWidget(self.textbox, 0, 0, 1, 0)
    # self.layout.addWidget(QLabel("출력 위치(x,y)"), 0, 1, 3, 0)
    self.layout.addWidget(self.position, 1, 1)
    self.layout.addWidget(QLabel("출력 위치(x,y)"), 1, 0)


def content_SCREEN_CLEAR(self):
    self.layout = QVBoxLayout()
    self.wdg_label = QLabel("배경색 (255, 255, 255)")  # 그거 종류 그 뭐냐 하여튼 그거
    self.wdg_label.setAlignment(Qt.AlignCenter)

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.wdg_label)
    self.setLayout(self.layout)
