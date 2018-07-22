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
        self.editor.scene.addHasBeenModifiedListener(lambda: self.signal_change_editor())
        self.editor.view.scenePosChanged.connect(actions.on_scene_pos_changed)

        self.dock_editor = QDockWidget("편집 환경", self)
        self.dock_editor.setWidget(self.editor)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_editor)

        self.setWindowTitle(f"{TEAM} {NAME} {VERSION}")

        self.showMaximized()
        # self.showFullScreen()

    def create_menu(self):
        menu_bar:QMenu = self.menuBar()

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
        menu_leaf = menu_bar.addMenu("스크립트(&L)")
        menu_leaf.addAction(actions.new_leaf())
        menu_run = menu_bar.addMenu("실행(&R)")
        menu_run.addAction(actions.run_as_python())
        menu_run.addAction(actions.run())
        menu_help = menu_bar.addMenu("도움말(&H)")
        menu_help.addAction(actions.license_dialog())
        # menu_edit.addAction(actions.new_leaf())

    def signal_change_editor(self, true=True):
        # print(self.focusWidget())
        CONF["MODIFIED"] = True if true else False
        self.renewal()

    def renewal(self):
        if not CONF["MODIFIED"]:
            self.setWindowTitle(f"{TEAM} {NAME} {VERSION} - {CONF['FILE_NAME']}"
                                if CONF['FILE_NAME'] is not None
                                else f"{TEAM} {NAME} {VERSION} - 빈 파일")
        elif CONF["MODIFIED"]:
            self.setWindowTitle(f"{TEAM} {NAME} {VERSION} - {CONF['FILE_NAME']}*"
                                if CONF['FILE_NAME'] is not None
                                else f"{TEAM} {NAME} {VERSION} - 제목 없음*")

    def is_modified(self):
        return self.editor.scene.has_been_modified

    def maybe_save(self):
        if not self.is_modified():
            return True

        res = QMessageBox.warning(None, f"{NAME} - 현재 파일이 변경됨",
                                  f"현재 파일 ["
                                  f"{CONF['FILE_NAME'] if CONF['FILE_NAME'] is not None else '제목 없음'}"
                                  f"]이 수정되었습니다.\n"
                                  f"Do you want to save your changes?",
                                  QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
                                  )

        if res == QMessageBox.Save:
            return actions.on_file_save()
        elif res == QMessageBox.Cancel:
            return False

        return True

    def closeEvent(self, event):
        if self.maybe_save():
            self.deleteLater()
            event.accept()
        else:
            event.ignore()
