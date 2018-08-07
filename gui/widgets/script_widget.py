from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# from gui.widgets.tree_combobox import TreeComboBox
from code_content.leaf_types import getLeafTypeModel, getWindowLeafTypeModel, getEtcLeafTypeModel
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


class TabScriptWidget(QWidget):

    def __init__(self, parent=None):
        super(TabScriptWidget, self).__init__(parent=parent)
        self.x_count = 5
        self.y_count = -3
        self.first = True

        self.tab = QTabWidget(self)
        self.tab_window = QWidget()
        self.tab_console = QWidget()
        self.tab_event = QWidget()
        self.tab_etc = QWidget()

        self.widget_tab_window = QBasedTreeSelector()
        self.widget_tab_window.setMinimumHeight(500)
        self.widget_tab_window.setModel(getWindowLeafTypeModel())
        self.widget_tab_window.doubleClicked.connect(self.widget_tab_window_doubleClickEvent)

        self.widget_tab_etc = QBasedTreeSelector()
        self.widget_tab_etc.setMinimumHeight(500)
        self.widget_tab_etc.setModel(getEtcLeafTypeModel())
        self.widget_tab_etc.doubleClicked.connect(self.widget_tab_etc_doubleClickEvent)

        self.initialize_widgets()

        self.setMinimumWidth(300)

    def initialize_widgets(self):
        self.tab.setMinimumHeight(500)
        self.tab.addTab(self.tab_window, "윈도우")
        self.tab.addTab(self.tab_event, "이벤트")
        self.tab.addTab(self.tab_console, "표준입출력")
        self.tab.addTab(self.tab_etc, "기타")

        lay_tab_window = QFormLayout()
        lay_tab_window.addWidget(self.widget_tab_window)

        lay_tab_etc = QFormLayout()
        lay_tab_etc.addWidget(self.widget_tab_etc)

        self.tab_window.setLayout(lay_tab_window)
        self.tab_etc.setLayout(lay_tab_etc)

    def selectedType_window(self):
        for ix in self.widget_tab_window.selectedIndexes():
            return ix.data(Qt.DisplayRole)

    def selectedType_etc(self):
        for ix in self.widget_tab_etc.selectedIndexes():
            return ix.data(Qt.DisplayRole)

    def widget_tab_window_doubleClickEvent(self):
        if self.selectedType_window() in ALL_LEAF_TYPES:
            if self.first:
                on_new_leaf(x=0, y=-250, defined=str(self.selectedType_window()))
                self.first = False
                return True
            elif self.x_count > 3:
                self.x_count = 1
            elif self.y_count > 7:
                self.y_count = 1
            on_new_leaf(x=self.x_count*150, y=self.y_count*50, defined=str(self.selectedType_window()))

            self.x_count += 1
            self.y_count += 1

    def widget_tab_etc_doubleClickEvent(self):
        print(self.selectedType_etc())
        if self.selectedType_etc() in ALL_LEAF_TYPES:
            if self.first:
                on_new_leaf(x=0, y=-250, defined=str(self.selectedType_etc()))
                self.first = False
                return True
            elif self.x_count > 3:
                self.x_count = 1
            elif self.y_count > 7:
                self.y_count = 1
            on_new_leaf(x=self.x_count*150, y=self.y_count*50, defined=str(self.selectedType_etc()))

            self.x_count += 1
            self.y_count += 1

