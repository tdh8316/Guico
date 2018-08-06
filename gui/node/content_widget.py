from collections import OrderedDict

from PyQt5.QtGui import QFont

from code_content.default import *
from gui.widgets.customized import *
from gui.node.serializable import Serializable
from PyQt5.QtWidgets import *


class QDMNodeContentWidget(QWidget, Serializable):

    def __init__(self, node, title, parent=None):
        super().__init__(parent)

        self.node = node
        self.title = title
        self.type = title

        # print(f"QDMNodeContentWidget::title={title}")

        if self.type == IF:
            pass
        elif self.type == PRINT:
            self.content_print()
        elif self.type == DRAW_TEXT:
            self.content_drawtext()
        elif self.type == ENTRY_POINT:
            content_entry(self)
        elif self.type == WINDOW_NEW:
            self.content_wininit()

    def content_wininit(self):
        self.layout = QGridLayout()
        self.wdg_label = QLabel("윈도우를 초기화하는 함수입니다.")  # 그거 종류 그 뭐냐 하여튼 그거
        self.wdg_label.setAlignment(Qt.AlignCenter)

        self._win_size = QDMLineEdit("800,600")

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.wdg_label, 0, 0, 1, 0)
        self.layout.addWidget(self._win_size, 1, 1)
        self.layout.addWidget(QLabel("창 크기(w,h)"), 1, 0)
        self.setLayout(self.layout)

    def content_print(self):
        self.layout = QVBoxLayout()
        self.textbox = QDMTextEdit("")  # 그 텍스트박스 그거임
        # self.wdg_label = QLabel(self.title)  # 그거 종류 그 뭐냐 하여튼 그거

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(self.textbox)

    def content_drawtext(self):
        self.layout = QGridLayout()
        self.textbox = QDMLineEdit("")  # 그 텍스트박스 그거임
        self.position = QDMLineEdit("0,0")  # 그 텍스트박스 그거임
        # self.position.setMaxLength(3)
        self.position.setFont(QFont("맑은 고딕", 9))
        self.wdg_label = QLabel("출력 위치(x,y)")  # 그거 종류 그 뭐냐 하여튼 그거

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.layout.addWidget(self.textbox, 0, 0, 1, 0)
        self.layout.addWidget(self.position, 1, 0)
        self.layout.addWidget(self.wdg_label, 1, 1)

    def serialize(self):
        # print("Content::serialize::type =", self.type)
        if self.type == PRINT:
            return OrderedDict([("str", self.textbox.toPlainText())])
        elif self.type == DRAW_TEXT:
            return OrderedDict([
                ("str", self.textbox.text()),
                ("pos", self.position.text())])
        elif self.type == WINDOW_NEW:
            return OrderedDict([
                # ("str", self.textbox.text()),
                ("size", self._win_size.text())])

        return OrderedDict([])

    def deserialize(self, data, hashmap={}):
        if self.type == PRINT:
            self.textbox.setPlainText(data["str"])
        elif self.type == DRAW_TEXT:
            self.textbox.setText(data["str"])
            self.position.setText(data["pos"])
        elif self.type == WINDOW_NEW:
            self._win_size.setText(data["size"])

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value
