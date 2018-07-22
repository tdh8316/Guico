from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from core.config import LEAF_TYPES


def getLeafTypeModel():
    type_model = QStandardItemModel()

    entry_parent = QStandardItem("Entry")
    entry_parent.setEditable(False)

    console_parent = QStandardItem("Console")
    for console_item in LEAF_TYPES["CONSOLE"]:
        item = QStandardItem(console_item)
        item.setEditable(False)
        console_parent.appendRow(QStandardItem(item))
    console_parent.setEditable(False)

    window_parent = QStandardItem("Window")
    for console_item in LEAF_TYPES["WINDOW"]:
        item = QStandardItem(console_item)
        item.setEditable(False)
        window_parent.appendRow(QStandardItem(item))
    window_parent.setEditable(False)

    type_model.appendRow(entry_parent)
    type_model.appendRow(console_parent)
    type_model.appendRow(window_parent)

    type_model.setHeaderData(0, Qt.Horizontal, "잎의 유형을 선택하세요↓", Qt.DisplayRole)

    return type_model
