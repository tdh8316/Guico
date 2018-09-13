from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.utils.icons import get_icon_s
from gui.utils.layout import clear_layout
from gui.widgets.customized import CodeEditWithDisabledError


def content_PYTHON_NATIVE(self):
    self.layout = QVBoxLayout()
    self.textbox = CodeEditWithDisabledError()  # 그 텍스트박스 그거임
    self.textbox.hide()
    self.btn_hide = QPushButton()
    self.btn_hide.setIcon(QIcon(QPixmap(get_icon_s("downarrow"))))
    self.btn_hide.setCheckable(True)
    self.btn_hide.toggle()
    self.btn_hide.setFixedSize(60,20)
    self.btn_hide.clicked.connect(lambda: hide_PYTHON_NATIVE(self))
    # self.wdg_label = QLabel(self.title)  # 그거 종류 그 뭐냐 하여튼 그거

    # self.layout.addWidget(self.wdg_label)
    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.addWidget(self.btn_hide)
    self.layout.addWidget(self.textbox)
    self.setLayout(self.layout)


def hide_PYTHON_NATIVE(self):
    self.textbox: CodeEditWithDisabledError
    if self.btn_hide.isChecked():
        # Widgets must hide.
        self.btn_hide.setIcon(QIcon(QPixmap(get_icon_s("downarrow"))))

    else:
        # Widgets must show.
        self.btn_hide.setIcon(QIcon(QPixmap(get_icon_s("uparrow"))))
