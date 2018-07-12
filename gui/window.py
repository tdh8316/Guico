import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from gui.node.editor_widget import NodeEditorWidget
from core.config import *


class Editor(QMainWindow):

    def __init__(self):
        super().__init__()

        self.editor = NodeEditorWidget(self)

        self.editor.scene.addHasBeenModifiedListener(lambda: self.setWindowTitle(f"{NAME} - {CONF['FILE_NAME']}*"))

        self.dock_editor = QDockWidget("편집 환경", self)
        self.dock_editor.setWidget(self.editor)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_editor)

        self.setWindowTitle(NAME)

        self.show()

    def renewal(self):
        self.setWindowTitle(f"{NAME} - {CONF['FILE_NAME']}")

    def is_modified(self):
        return self.centralWidget().scene.has_been_modified

    def closeEvent(self, event):
        event.accept()
