import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.widgets.customized import ImagePathLineEdit

from core.config import PERSON_IMAGE


def content_DRAW_IMAGE(self):
    self.layout = QGridLayout()
    self.image_path = ImagePathLineEdit()
    self.image_path.setFont(QFont("맑은 고딕", 9))
    self.image_path.setPath(PERSON_IMAGE)

    btn_find_image = QPushButton("...", clicked=lambda: setup_image(self))
    btn_find_image.setFixedSize(30, 30)

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.image_path, 0, 0)
    self.layout.addWidget(btn_find_image, 0, 1)
    # self.layout.addWidget(QLabel(" 아직 구상중인 모델입니다."))
    self.setLayout(self.layout)


def setup_image(self):
    fname, f = QFileDialog.getOpenFileName(caption="이미지 찾기", filter="이미지 파일 (*.png *.jpg *.gif *.bmp)")
    if os.path.isfile(fname):
        self.image_path.setPath(fname)
