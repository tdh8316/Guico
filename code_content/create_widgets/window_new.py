from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from gui.widgets.customized import QDMLineEdit


def content_WINDOW_NEW(self):
    self.layout = QGridLayout()
    self.wdg_label = QLabel("윈도우를 초기화하는 함수입니다.")  # 그거 종류 그 뭐냐 하여튼 그거
    self.wdg_label.setAlignment(Qt.AlignCenter)

    self._win_size = QDMLineEdit("800,600")
    self._win_size.setMaximumWidth(100)
    self._win_size.setFont(QFont("맑은 고딕", 9))

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.wdg_label, 0, 0, 1, 0)
    self.layout.addWidget(self._win_size, 1, 1)
    self.layout.addWidget(QLabel("창 크기(w,h)"), 1, 0)
    self.setLayout(self.layout)