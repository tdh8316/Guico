from collections import OrderedDict

from PyQt5.QtWidgets import *

from contents.default import *
from contents.create_widgets import *
from core.serial_communication import Serial
from gui.node.serializable import Serializable
from gui.widgets.customized import *

NODE_CONTENTS


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
        self.sprite_name = None
        self.group_name = None
        self.group1 = None
        self.group2 = None
        self.serial_communication = Serial(self)

        try:
            exec(f"content_{GetNameFromStr[self.type]}(self)")
        except NameError:
            try:
                exec(f"self.content_{GetNameFromStr[self.type]}()")
            except AttributeError:
                QMessageBox.critical(None, "잎 콘텐츠 없음", "해당하는 콘텐츠가 없습니다.")

    def content_ENTRY_POINT(self):
        self.layout = QVBoxLayout()
        self.wdg_label = QLabel("프로그램이 시작될 때")  # 그거 종류 그 뭐냐 하여튼 그거
        self.wdg_label.setAlignment(Qt.AlignCenter)
        self.setToolTip("이 시작점에 연결된 잎들은 어떠한 사건에도 종속되지 않고 계속해서 실행됩니다.")

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.wdg_label)
        self.setLayout(self.layout)
        # self.layout.addWidget(self.wdg_label)

    '''def content_PRINT(self):
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
        self.layout.addWidget(self.textbox)'''

    def serialize(self):
        return self.serial_communication.serialize()

    def deserialize(self, data, hashmap=None):
        self.serial_communication.deserialize(data=data, hashmap=hashmap)

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value

    def wheelEvent(self, QWheelEvent):
        super().wheelEvent(QWheelEvent)
