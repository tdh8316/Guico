from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# from gui.widgets.tree_combobox import TreeComboBox
from code_content.leaf_types import getLeafTypeModel
from core.actions import on_new_leaf
from gui.widgets.tree_selector import QBasedTreeSelector
from core.config import *


class ScriptWidget(QWidget):

    def __init__(self, parent=None):
        super(ScriptWidget, self).__init__(parent=parent)

        self.x_count = 5
        self.y_count = -3
        self.first = True

        self.types = QBasedTreeSelector()
        self.setWindowTitle(f"{NAME} - 새 잎 만들기")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(480, 240)

        self.base_layout = QFormLayout(self)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.create_widgets()

        self.vbox.addWidget(self.types)

        self.base_layout.addRow(self.vbox)
        self.base_layout.addRow(self.hbox)

        self.setLayout(self.base_layout)

    def create_widgets(self):
        # self.types = TreeComboBox(self)
        # self.types.resize(240, 30)
        # self.types.currentIndexChanged.connect(self.change)
        # self.types.setFont(QFont("맑은 고딕", 9))
        self.types.setModel(getLeafTypeModel())
        self.types.doubleClicked.connect(self.doubleClickEvent)

    def selectedType(self):
        for ix in self.types.selectedIndexes():
            text = ix.data(Qt.DisplayRole)  # or ix.data()
            INDEX = text
            return INDEX

    def doubleClickEvent(self):
        global isDoubleClicked
        isDoubleClicked = True
        if self.selectedType() in ALL_LEAF_TYPES:
            if self.first:
                on_new_leaf(x=0, y=-250, defined=str(self.selectedType()))
                self.first = False
                return True
            elif self.x_count > 3:
                self.x_count = 1
            elif self.y_count > 7:
                self.y_count = 1
            on_new_leaf(x=self.x_count*150, y=self.y_count*50, defined=str(self.selectedType()))

            self.x_count += 1
            self.y_count += 1

    def change(self):
        if self.types.currentText() not in ALL_LEAF_TYPES:
            self.types.showPopup()
