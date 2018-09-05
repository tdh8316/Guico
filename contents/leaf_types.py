from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from contents.default import *

'''def getLeafTypeModel():
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
    # type_model.appendRow(console_parent)
    type_model.appendRow(window_parent)

    type_model.setHeaderData(0, Qt.Horizontal, "잎의 유형을 선택하세요↓", Qt.DisplayRole)

    return type_model'''


def getLooksLeafTypeModel():
    type_model = QStandardItemModel()

    item = QStandardItem(WINDOW_NEW)
    item.setEditable(False)
    type_model.appendRow(item)
    item = QStandardItem(DRAW_TEXT)
    item.setEditable(False)
    type_model.appendRow(item)
    item = QStandardItem(DRAW_IMAGE)
    item.setEditable(False)
    type_model.appendRow(item)
    item = QStandardItem(SCREEN_CLEAR)
    item.setEditable(False)
    type_model.appendRow(item)

    type_model.setHeaderData(0, Qt.Horizontal, "더블클릭해서 배치할 수 있습니다.", Qt.DisplayRole)

    return type_model


def getEventLeafTypeModel():
    type_model = QStandardItemModel()

    entry = QStandardItem(ENTRY_POINT)
    entry.setEditable(False)
    type_model.appendRow(entry)
    item = QStandardItem(KEY_INPUT)
    item.setEditable(False)
    type_model.appendRow(item)
    item = QStandardItem(KEY_NOT_INPUT)
    item.setEditable(False)
    type_model.appendRow(item)

    type_model.setHeaderData(0, Qt.Horizontal, "더블클릭해서 배치할 수 있습니다.", Qt.DisplayRole)

    return type_model


def getSoundsLeafTypeModel():
    type_model = QStandardItemModel()

    type_model.setHeaderData(0, Qt.Horizontal, "더블클릭해서 배치할 수 있습니다.", Qt.DisplayRole)

    return type_model


def getStdLeafTypeModel():
    type_model = QStandardItemModel()

    item = QStandardItem(VARIABLE_NEW)
    item.setEditable(False)
    type_model.appendRow(item)
    item = QStandardItem(VARIABLE_CHANGE)
    item.setEditable(False)
    type_model.appendRow(item)
    item = QStandardItem(VARIABLE_PLUS)
    item.setEditable(False)
    type_model.appendRow(item)

    type_model.setHeaderData(0, Qt.Horizontal, "더블클릭해서 배치할 수 있습니다.", Qt.DisplayRole)

    return type_model
