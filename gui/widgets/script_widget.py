import random

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# from gui.widgets.tree_combobox import TreeComboBox
from leaf_content.leaf_types import *
from core import actions
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
                actions.on_new_leaf(x=0, y=-250, defined=str(self.selectedType()))
                self.first = False
                return True
            elif self.x_count > 3:
                self.x_count = 1
            elif self.y_count > 7:
                self.y_count = 1
                actions.on_new_leaf(x=self.x_count * 150, y=self.y_count * 50, defined=str(self.selectedType()))

            self.x_count += 1
            self.y_count += 1

    def change(self):
        if self.types.currentText() not in ALL_LEAF_TYPES:
            self.types.showPopup()


class TabScriptWidget(QWidget):

    def __init__(self, parent=None):
        super(TabScriptWidget, self).__init__(parent=parent)

        self.latest_pos: dict = {"X": int,
                                 "Y": int}

        self.tab = QTabWidget(self)
        self.tab_looks = QWidget()
        self.tab_sounds = QWidget()
        self.tab_event = QWidget()
        self.tab_etc = QWidget()

        self.widget_tab_looks = QBasedTreeSelector()
        self.widget_tab_looks.setMinimumHeight(500)
        self.widget_tab_looks.setModel(getLooksLeafTypeModel())
        self.widget_tab_looks.doubleClicked.connect(self.itemDoubleClickEvent)

        self.widget_tab_event = QBasedTreeSelector()
        self.widget_tab_event.setMinimumHeight(500)
        self.widget_tab_event.setModel(getEventLeafTypeModel())
        self.widget_tab_event.doubleClicked.connect(self.itemDoubleClickEvent)

        self.widget_tab_sounds = QBasedTreeSelector()
        self.widget_tab_sounds.setMinimumHeight(500)
        self.widget_tab_sounds.setModel(getSoundsLeafTypeModel())
        self.widget_tab_sounds.doubleClicked.connect(self.itemDoubleClickEvent)

        self.widget_tab_etc = QBasedTreeSelector()
        self.widget_tab_etc.setMinimumHeight(500)
        # self.widget_tab_etc.setModel(getConsoleLeafTypeModel())
        self.widget_tab_etc.doubleClicked.connect(self.itemDoubleClickEvent)

        self.initialize_widgets()

        self.setMinimumWidth(300)

    def initialize_widgets(self):
        self.tab.setMinimumHeight(500)
        self.tab.addTab(self.tab_looks, "형태")
        self.tab.addTab(self.tab_event, "이벤트")
        self.tab.addTab(self.tab_sounds, "소리")
        self.tab.addTab(self.tab_etc, "일반")

        lay_tab_looks = QFormLayout()
        lay_tab_looks.addWidget(self.widget_tab_looks)

        lay_tab_event = QFormLayout()
        lay_tab_event.addWidget(self.widget_tab_event)

        lay_tab_sounds = QFormLayout()
        lay_tab_sounds.addWidget(self.widget_tab_sounds)

        lay_tab_etc = QFormLayout()
        lay_tab_etc.addWidget(self.widget_tab_etc)

        self.tab_looks.setLayout(lay_tab_looks)
        self.tab_event.setLayout(lay_tab_event)
        self.tab_sounds.setLayout(lay_tab_sounds)
        self.tab_sounds.setLayout(lay_tab_etc)

    def selectedType(self):
        for ix in self.focusWidget().selectedIndexes():
            return ix.data(Qt.DisplayRole)

    def itemDoubleClickEvent(self):
        # if self.selectedType() in ALL_LEAF_TYPES:
            if [self.latest_pos["X"], self.latest_pos["Y"]] != [CONF["MOUSE_X"], CONF["MOUSE_Y"]]:
                actions.on_new_leaf(x=CONF["MOUSE_X"] + 255, y=CONF["MOUSE_Y"], defined=str(self.selectedType()))
            else:
                actions.on_new_leaf(x=CONF["MOUSE_X"] + random.randint(128, 512), y=CONF["MOUSE_Y"] - random.randint(64, 256),
                            defined=str(self.selectedType()))
            self.latest_pos["X"], self.latest_pos["Y"] = CONF["MOUSE_X"], CONF["MOUSE_Y"]


class TabScriptWidget_Button(QWidget):

    def __init__(self, parent=None):
        super(TabScriptWidget_Button, self).__init__(parent=parent)
        self.setMinimumWidth(300)

        self.latest_pos: dict = {"X": int,
                                 "Y": int}

        self.tab = QTabWidget(self)
        self.tab_window = QWidget()
        self.tab_console = QWidget()
        self.tab_event = QWidget()
        self.tab_etc = QWidget()
        self.tab.setMinimumSize(300,500)
        self.tab.addTab(self.tab_window, "윈도우")
        self.tab.addTab(self.tab_event, "이벤트")
        self.tab.addTab(self.tab_console, "표준입출력")
        self.tab.addTab(self.tab_etc, "기타")

        self.lay_tab_window = QGridLayout()

        self.initialize_widgets()

        self.tab_window.setLayout(self.lay_tab_window)

    def initialize_widgets(self):
        self.init_window_buttons()

    def init_window_buttons(self):
        window_new = QPushButton(WINDOW_NEW)
        draw = QPushButton(DRAW_TEXT)

        window_new.clicked.connect(self.itemClickEvent)
        draw.clicked.connect(self.itemClickEvent)

        self.lay_tab_window.addWidget(window_new)
        self.lay_tab_window.addWidget(draw)



    def selectedType(self):
        return self.focusWidget().text()

    def itemClickEvent(self):
        if self.selectedType() in ALL_LEAF_TYPES:
            if [self.latest_pos["X"], self.latest_pos["Y"]] != [CONF["MOUSE_X"], CONF["MOUSE_Y"]]:
                on_new_leaf(x=CONF["MOUSE_X"] + 255, y=CONF["MOUSE_Y"], defined=str(self.selectedType()))
            else:
                on_new_leaf(x=CONF["MOUSE_X"] + random.randint(128, 512), y=CONF["MOUSE_Y"] - random.randint(64, 256),
                            defined=str(self.selectedType()))
            self.latest_pos["X"], self.latest_pos["Y"] = CONF["MOUSE_X"], CONF["MOUSE_Y"]
