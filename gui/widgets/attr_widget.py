from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from core.config import *


class AttributesTableWidget(QTableWidget):

    def __init__(self, parent=None):
        super(AttributesTableWidget, self).__init__(parent)

        self.setColumnCount(2)
        self.setRowCount(MAX_VAR)
        self.setHorizontalHeaderLabels(["변수명", "값"])

        self.setItem(0, 0, QTableWidgetItem("name"))
        self.setItem(0, 1, QTableWidgetItem("value"))

        # print(QTableWidgetItem(self.item(0,0)).text())
