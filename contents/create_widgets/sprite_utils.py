from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from gui.widgets.customized import ImagePathLineEdit, QDMLineEdit
from core.config import *


def content_ADD_GROUP(self):
    self.layout = QGridLayout()
    self.sprite_name = QDMLineEdit("")  # 그 텍스트박스 그거임
    self.sprite_name.setPlaceholderText("스프라이트 이름")
    self.sprite_name.setFont(QFont("맑은 고딕", 9))
    self.group_name = QDMLineEdit()  # 그 텍스트박스 그거임
    self.group_name.setPlaceholderText("그룹 이름")
    # self.position.setMaxLength(3)
    self.group_name.setFont(QFont("맑은 고딕", 9))

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.layout)
    self.layout.addWidget(self.sprite_name, 0, 0, 1, 0)
    self.layout.addWidget(QLabel("를"), 0, 1, Qt.AlignRight)
    self.layout.addWidget(self.group_name, 1, 0)
    self.layout.addWidget(QLabel("에 추가"), 1, 1)


def content_DRAW_GROUP(self):
    self.layout = QGridLayout()
    self.sprite_name = QDMLineEdit("")  # 그 텍스트박스 그거임
    self.sprite_name.setPlaceholderText("스프라이트 그룹명")
    self.sprite_name.setFont(QFont("맑은 고딕", 9))

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.layout)
    self.layout.addWidget(self.sprite_name, 0, 0)
    self.layout.addWidget(QLabel("그리기"), 0, 1)


def content_DETECT_COLLISION(self):
    self.layout = QGridLayout()
    self.group1 = QDMLineEdit("")  # 그 텍스트박스 그거임
    self.group1.setPlaceholderText("스프라이트")
    self.group1.setFont(QFont("맑은 고딕", 9))
    self.group2 = QDMLineEdit("")  # 그 텍스트박스 그거임
    self.group2.setPlaceholderText("그룹")
    self.group2.setFont(QFont("맑은 고딕", 9))

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.layout)
    self.layout.addWidget(self.group1, 0, 0)
    self.layout.addWidget(self.group2, 0, 1)
