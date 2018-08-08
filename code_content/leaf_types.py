from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from code_content.default import *
from core.config import LEAF_TYPES


def getLeafTypeModel():
    type_model = QStandardItemModel()

    entry_parent = QStandardItem(LEAF_TYPES["Entry"])
    entry_parent.setEditable(False)

    console_parent = QStandardItem("Console")
    for console_item in LEAF_TYPES["CONSOLE"]:
        item = QStandardItem(console_item)
        item.setEditable(False)
        console_parent.appendRow(QStandardItem(item))
    console_parent.setEditable(False)

    window_parent = QStandardItem("Window")
    for window_item in LEAF_TYPES["WINDOW"]:
        item = QStandardItem(window_item)
        item.setEditable(False)
        window_parent.appendRow(QStandardItem(item))
    window_parent.setEditable(False)

    type_model.appendRow(entry_parent)
    type_model.appendRow(console_parent)
    type_model.appendRow(window_parent)

    type_model.setHeaderData(0, Qt.Horizontal, "잎의 유형을 선택하세요↓", Qt.DisplayRole)

    return type_model


def getWindowLeafTypeModel():
    type_model = QStandardItemModel()

    for window_item in LEAF_TYPES["WINDOW"]:
        window_item = QStandardItem(window_item)
        window_item.setEditable(False)
        type_model.appendRow(QStandardItem(window_item))

    type_model.setHeaderData(0, Qt.Horizontal, "더블클릭해서 배치할 수 있습니다.", Qt.DisplayRole)

    return type_model


def getEventLeafTypeModel():
    type_model = QStandardItemModel()

    entry = QStandardItem(ENTRY_POINT)
    entry.setEditable(False)

    type_model.appendRow(entry)

    type_model.setHeaderData(0, Qt.Horizontal, "더블클릭해서 배치할 수 있습니다.", Qt.DisplayRole)

    return type_model


def getConsoleLeafTypeModel():
    type_model = QStandardItemModel()

    for console_item in LEAF_TYPES["CONSOLE"]:
        console_item = QStandardItem(console_item)
        console_item.setEditable(False)
        type_model.appendRow(QStandardItem(console_item))

    type_model.setHeaderData(0, Qt.Horizontal, "더블클릭해서 배치할 수 있습니다.", Qt.DisplayRole)

    return type_model
