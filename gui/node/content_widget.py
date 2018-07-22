from collections import OrderedDict

from PyQt5.QtCore import Qt

from builder.default import *
from gui.node.leaf_attribute import QDMTextEdit
from gui.node.serializable import Serializable
from PyQt5.QtWidgets import *

from gui.node import leaf_attribute, scene


class QDMNodeContentWidget(QWidget, Serializable):

    def __init__(self, node, title, parent=None):
        super().__init__(parent)

        self.node = node
        self.title = title
        self.type = title

        # print(f"QDMNodeContentWidget::title={title}")

        if self.type == IF:
            leaf_attribute.content_if(self)
        elif self.type == PRINT or self.type == DRAW_TEXT:
            self.content_print()
        elif self.type == ENTRY_POINT:
            self.layout = QVBoxLayout()
            self.wdg_label = QLabel("이 파일의 진입점 입니다.")  # 그거 종류 그 뭐냐 하여튼 그거
            self.wdg_label.setAlignment(Qt.AlignCenter)

            self.layout.setContentsMargins(0, 0, 0, 0)
            self.layout.addWidget(self.wdg_label)
            self.setLayout(self.layout)
            # self.layout.addWidget(self.wdg_label)

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value

    def content_print(self):
        self.layout = QVBoxLayout()
        self.textbox = QDMTextEdit("")  # 그 텍스트박스 그거임
        # self.wdg_label = QLabel(self.title)  # 그거 종류 그 뭐냐 하여튼 그거

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(self.textbox)

    def serialize(self):
        # print("Content::serialize::type =", self.type)
        if self.type == PRINT or self.type == DRAW_TEXT:
            # print(self.textbox.toPlainText())
            return OrderedDict([
                ("str", self.textbox.toPlainText())
            ])

        return OrderedDict([

        ])

    def deserialize(self, data, hashmap={}):
        if self.type == PRINT or self.type == DRAW_TEXT:
            self.textbox.setPlainText(data["str"])
