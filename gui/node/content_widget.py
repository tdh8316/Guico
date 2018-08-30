from collections import OrderedDict

from PyQt5.QtGui import QFont

from contents.default import *
from contents.create_widgets import *
from core.config import *
from gui.widgets.customized import *
from gui.node.serializable import Serializable
from PyQt5.QtWidgets import *


class QDMNodeContentWidget(QWidget, Serializable):

    def __init__(self, node, title=None, parent=None):
        super().__init__(parent)

        self.node = node
        self.title = title
        self.type: str = title

        self.layout = None
        self.wdg_label = None
        self.textbox = None
        self.position = None
        self._win_size = None
        self.image_path = None
        self.key = None
        self.var_name = None
        self.var_value = None

        try:
            exec(f"self.content_{GetNameFromStr[self.type]}()")
        except AttributeError:
            try:
                exec(f"content_{GetNameFromStr[self.type]}(self)")
            except NameError:
                QMessageBox.critical(None, "잎 콘텐츠 없음", "해당하는 콘텐츠가 없습니다.")

    def content_ENTRY_POINT(self):
        self.layout = QVBoxLayout()
        self.wdg_label = QLabel("프로그램이 시작될 때")  # 그거 종류 그 뭐냐 하여튼 그거
        self.wdg_label.setAlignment(Qt.AlignCenter)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.wdg_label)
        self.setLayout(self.layout)
        # self.layout.addWidget(self.wdg_label)

    def content_PRINT(self):
        self.layout = QVBoxLayout()
        self.textbox = QDMTextEdit("")  # 그 텍스트박스 그거임
        # self.wdg_label = QLabel(self.title)  # 그거 종류 그 뭐냐 하여튼 그거

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(self.textbox)

    def content_INPUT(self):
        self.layout = QVBoxLayout()
        self.textbox = QDMTextEdit("")  # 그 텍스트박스 그거임
        # self.wdg_label = QLabel(self.title)  # 그거 종류 그 뭐냐 하여튼 그거

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(self.textbox)

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
        elif self.type == KEY_INPUT:
            return OrderedDict([
                ("key", self.key.currentText())])
        elif self.type == DRAW_IMAGE:
            return OrderedDict([
                ("path", self.image_path.WhereIsImage()),
                ("pos", self.position.text())])
        elif self.type == VARIABLE_CHANGE:
            return OrderedDict([
                ("name", self.var_name.textToVariableName()),
                ("value", self.var_value.text())])
        elif self.type == VARIABLE_PLUS:
            return OrderedDict([
                ("name", self.var_name.textToVariableName()),
                ("value", self.var_value.text())])

        return OrderedDict([])

    def deserialize(self, data, hashmap=None):
        if hashmap is None:
            hashmap = {}
        if self.type == PRINT:
            self.textbox.setPlainText(data["str"])
        elif self.type == DRAW_TEXT:
            self.textbox.setText(data["str"])
            self.position.setText(data["pos"])
        elif self.type == WINDOW_NEW:
            self._win_size.setText(data["size"])
        elif self.type == KEY_INPUT:
            self.key.setCurrentText(data["key"])
            self.node.title = f"[{data['key']}] {KEY_INPUT}"
        elif self.type == DRAW_IMAGE:
            self.image_path.setPath(data["path"])
        elif self.type == VARIABLE_CHANGE:
            self.var_name.setVariableNameFromText(data["name"])
            self.var_value.setText(data["value"])
            self.position.setText(data["pos"])
        elif self.type == VARIABLE_PLUS:
            self.var_name.setVariableNameFromText(data["name"])
            self.var_value.setText(data["value"])

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value

    def wheelEvent(self, QWheelEvent):
        super().wheelEvent(QWheelEvent)
