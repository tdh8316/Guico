import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# from gui.widgets.tree_combobox import TreeComboBox
from gui import theme
from core.config import *


class OpenSourceLicense(QDialog):

    def __init__(self, parent=None):
        super(OpenSourceLicense, self).__init__(parent)
        self.setWindowFlags(Qt.Popup)

        layout = QFormLayout(self)
        textbox = QPlainTextEdit()
        textbox.setPlainText(OPEN_SOURCE_LICENSE)
        textbox.setReadOnly(True)
        textbox.setFixedWidth(720)
        textbox.setFixedHeight(640)
        layout.addRow(textbox)

        self.setLayout(layout)
        self.show()


class ActivateKey(QDialog):

    def __init__(self, parent=None):
        super(ActivateKey, self).__init__(parent)

        self.setWindowTitle(f"{NAME} 테스터 인증 키 입력")

        layout = QFormLayout(self)
        _input = QLineEdit()
        # noinspection SpellCheckingInspection
        _input.setInputMask(">0000-0000-AAAA-AAAA;_")
        layout.addRow(_input)

        self.setLayout(layout)
        self.show()


class setLeafType(QDialog):

    def __init__(self, parent):
        QDialog.__init__(self, parent)

        self.setWindowTitle(f"{NAME} - 새 잎 만들기")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(480, 240)

        self.base_layout = QFormLayout(self)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.create_widgets()

        self.vbox.addWidget(self.types)
        self.hbox.addWidget(self.buttons)

        self.base_layout.addRow(self.vbox)
        self.base_layout.addRow(self.hbox)

        self.setLayout(self.base_layout)

        INDEX = self.types.currentIndex()

    def create_widgets(self):
        # self.types = TreeComboBox(self)
        # self.types.resize(240, 30)
        # self.types.currentIndexChanged.connect(self.change)
        # self.types.setFont(QFont("맑은 고딕", 9))
        self.types = QTreeView()

        type_model = QStandardItemModel()

        entry_parent = QStandardItem("Entry")
        entry_parent.setEditable(False)

        console_parent = QStandardItem("Console")
        for console_item in LEAF_TYPES["CONSOLE"]:
            item = QStandardItem(console_item)
            item.setEditable(False)
            console_parent.appendRow(QStandardItem(item))
        console_parent.setEditable(False)

        type_model.appendRow(entry_parent)
        type_model.appendRow(console_parent)

        type_model.setHeaderData(0, Qt.Horizontal, "잎의 유형을 선택하세요↓", Qt.DisplayRole)
        self.types.setModel(type_model)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def selectedType(self):
        try:
            for ix in self.types.selectedIndexes():
                text = ix.data(Qt.DisplayRole)  # or ix.data()
                INDEX = text
            return INDEX
        except UnboundLocalError as e:
            QMessageBox.critical(None, f"{NAME} - 처리되지 않은 예외", f"{e}\n{sys.exc_info()}")

    def change(self):
        if self.types.currentText() not in ALL_LEAF_TYPES:
            self.types.showPopup()

    @staticmethod
    def get(parent=None):
        _win = setLeafType(parent)
        result = _win.exec_()
        data = _win.selectedType()
        if data in ALL_LEAF_TYPES:
            return data, result == QDialog.Accepted
