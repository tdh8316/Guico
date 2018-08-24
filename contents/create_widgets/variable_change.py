from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QLabel, QVBoxLayout

from gui.widgets.customized import *


def content_VARIABLE_CHANGE(self):
    self.layout = QGridLayout()
    self.var_name = VariableNameEdit("")  # 그 텍스트박스 그거임
    self.var_name.setPlaceholderText("변수")
    self.var_name.setFont(QFont("맑은 고딕", 9))
    self.var_value = QDMLineEdit("")  # 그 텍스트박스 그거임
    self.var_value.setPlaceholderText("값")
    # self.position.setMaxLength(3)
    self.var_value.setFont(QFont("맑은 고딕", 9))

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.layout)
    self.layout.addWidget(self.var_name, 0, 0)
    self.layout.addWidget(QLabel("를"), 0, 1)
    self.layout.addWidget(self.var_value, 0, 2)
    self.layout.addWidget(QLabel("로 정하기"), 0, 3)
