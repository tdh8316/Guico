from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gui import theme
from core.config import *


class TreeComboBox(QComboBox):
    def __init__(self, *args):
        super().__init__(*args)
        self.__skip_next_hide = False

        tree_view = QTreeView(self)
        tree_view.setFrameShape(QFrame.NoFrame)
        tree_view.setEditTriggers(tree_view.NoEditTriggers)
        tree_view.setAlternatingRowColors(True)
        tree_view.setSelectionBehavior(tree_view.SelectRows)
        tree_view.setWordWrap(False)
        tree_view.setAllColumnsShowFocus(False)
        self.setView(tree_view)

        self.view().viewport().installEventFilter(self)

    def showPopup(self):
        self.setRootModelIndex(QModelIndex())
        super().showPopup()

    def hidePopup(self):
        self.setRootModelIndex(self.view().currentIndex().parent())
        self.setCurrentIndex(self.view().currentIndex().row())
        if self.__skip_next_hide:
            self.__skip_next_hide = False
        else:
            super().hidePopup()

    def selectIndex(self, index):
        self.setRootModelIndex(index.parent())
        self.setCurrentIndex(index.row())

    def eventFilter(self, object, event):
        if event.type() == QEvent.MouseButtonPress and object is self.view().viewport():
            index = self.view().indexAt(event.pos())
            self.__skip_next_hide = not self.view().visualRect(index).contains(event.pos())
        return False


def test():
    app = QApplication([])

    combo = TreeComboBox()
    combo.currentIndexChanged.connect(lambda: print(combo.currentText()))
    combo.resize(200, 30)

    parent_item = QStandardItem('Item 1')
    parent_item.appendRow(QStandardItem('Child'))
    model = QStandardItemModel()
    model.appendRow(parent_item)
    model.appendRow(QStandardItem('Item 2'))
    combo.setModel(model)
    model.setHeaderData(0, Qt.Horizontal, str(), Qt.DisplayRole)

    combo.show()
    app.exec_()
