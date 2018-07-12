import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from gui.node.editor_widget import NodeEditorWidget
from core.config import *
from core import actions


class NewLeafDialog(QWidget):

    def __init__(self, parent=None):
        super(NewLeafDialog, self).__init__(parent)

        self.setWindowTitle(f"{NAME} - 새 잎 만들기")

        layout = QFormLayout()

        self.name = QLineEdit()
        self.type = QComboBox()

        layout.addRow(self.name, self.type)


class Editor(QMainWindow):

    def __init__(self):
        super().__init__()
        actions.initialize(self)

        self.editor = NodeEditorWidget(self)

        self.editor.scene.addHasBeenModifiedListener(lambda: self.setWindowTitle(f"{NAME} - {CONF['FILE_NAME']}*"))

        self.dock_editor = QDockWidget("편집 환경", self)
        self.dock_editor.setWidget(self.editor)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_editor)

        self.setWindowTitle(NAME)

        self.showMaximized()
        self.show()

    def renewal(self):
        self.setWindowTitle(f"{NAME} - {CONF['FILE_NAME']}")

    def is_modified(self):
        return self.centralWidget().scene.has_been_modified

    def closeEvent(self, event):
        event.accept()
