import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from gui.node.editor_widget import NodeEditorWidget
from core.config import *
from core import actions


class Editor(QMainWindow):

    def __init__(self):
        super().__init__()
        actions.initialize(self)
        self.create_menu()
        self.status_mouse_pos = QLabel("Mouse Pos(0, 0)")
        self.statusBar().addPermanentWidget(self.status_mouse_pos)

        self.editor = NodeEditorWidget(self)
        self.editor.scene.addHasBeenModifiedListener(lambda:
                                                     self.setWindowTitle(f"{NAME} - {CONF['FILE_NAME']}*"))
        self.editor.view.scenePosChanged.connect(actions.on_scene_pos_changed)

        self.dock_editor = QDockWidget("편집 환경", self)
        self.dock_editor.setWidget(self.editor)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_editor)

        self.setWindowTitle(NAME)

        self.showMaximized()
        self.show()

    def create_menu(self):
        menu_bar = self.menuBar()
        menu_file = menu_bar.addMenu("파일(&F)")
        menu_file.addAction(actions.file_new())
        menu_file.addAction(actions.file_open())
        menu_file.addAction(actions.file_save())
        menu_file.addAction(actions.file_save_as())
        menu_edit = menu_bar.addMenu("편집(&E)")
        menu_edit.addAction(actions.undo())
        menu_edit.addAction(actions.redo())
        menu_edit.addSeparator()
        menu_edit.addAction(actions.cut())
        menu_edit.addAction(actions.copy())
        menu_edit.addAction(actions.paste())
        menu_edit.addAction(actions.delete())
        menu_edit.addSeparator()
        menu_help = menu_bar.addMenu("도움말(&H)")
        menu_help.addAction(actions.license_dialog())
        # menu_edit.addAction(actions.new_leaf())

    def renewal(self):
        self.setWindowTitle(f"{NAME} - {CONF['FILE_NAME']}")

    def is_modified(self):
        return self.centralWidget().scene.has_been_modified

    def maybe_save(self):
        if not self.is_modified():
            return True

        res = QMessageBox.warning(None, "About to loose your work?",
                                  f"현재 파일 [{CONF['FILE_NAME']}]이 수정되었습니다.\n"
                                  f"Do you want to save your changes?",
                                  QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
                                  )

        if res == QMessageBox.Save:
            return actions.on_file_save()
        elif res == QMessageBox.Cancel:
            return False

        return True

    def closeEvent(self, event):
        event.accept()
