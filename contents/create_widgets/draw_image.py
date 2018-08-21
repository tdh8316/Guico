from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core.config import PERSON_IMAGE


def content_DRAW_IMAGE(self):
    self.layout = QVBoxLayout()
    self.image_path = QLineEdit()
    self.image_path.setFont(QFont("맑은 고딕", 9))
    self.image_path.setText(PERSON_IMAGE)

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.image_path)
    self.layout.addWidget(QLabel(" 아직 구상중인 모델입니다."))
    self.setLayout(self.layout)
