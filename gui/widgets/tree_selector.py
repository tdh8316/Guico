from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QBasedTreeSelector(QTreeView):
    def __init__(self):
        super().__init__()
        self.setAlternatingRowColors(True)
        # self.setStyleSheet("QTreeWidget::item { border-bottom: 1px solid white;}")
