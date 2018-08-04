import datetime

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from gui.node.editor_widget import NodeEditorWidget
import build_tools
from core.config import *
from core import actions


class MainForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.log = QPlainTextEdit(self)
        self.log.setReadOnly(True)
        self.dock_log = QDockWidget("Log", self)
        self.dock_log.setWidget(self.log)
        self.dock_log.hide()

        actions.initialize(self)
        build_tools.initialize(self)

        self.create_menu()
        self.status_mouse_pos = QLabel("Unknown Mouse Pos")
        self.statusBar().addPermanentWidget(self.status_mouse_pos)

        self.editor = NodeEditorWidget(self)
        self.editor.scene.addHasBeenModifiedListener(lambda: self.signal_change_editor())
        self.editor.view.scenePosChanged.connect(actions.on_scene_pos_changed)

        self.dock_editor = QDockWidget("편집 환경", self)
        self.dock_editor.setWidget(self.editor)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_editor)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock_log)

        self.setWindowTitle(f"{TEAM} {NAME} {VERSION}")

        self.showMaximized()
        self.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 {NAME} 위젯 초기화 성공")
        # self.showFullScreen()

    def create_menu(self):
        menu_bar:QMenu = self.menuBar()
        # menu_bar.setFont(QFont("맑은 고딕", 9))

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
        menu_view = menu_bar.addMenu("보기(&V)")
        menu_view.addAction(QAction("출력 창 보기(&O)", self, shortcut="Alt+1", triggered=lambda: self.dock_log.show()))
        menu_view.addAction(QAction(
            "전체 화면으로 보기(&S)", self, shortcut="F11", triggered=self._showFullScreen, checkable=True))
        menu_leaf = menu_bar.addMenu("스크립트(&L)")
        menu_leaf.addAction(actions.new_leaf())
        menu_run = menu_bar.addMenu("실행(&R)")
        menu_run.addAction(actions.run_as_python())
        menu_run.addAction(actions.compile_to_python())
        menu_run.addSeparator()
        menu_run.addAction(actions.packaging())
        menu_help = menu_bar.addMenu("도움말(&H)")
        menu_help.addAction(actions.license_dialog())
        # menu_edit.addAction(actions.new_leaf())

    def signal_change_editor(self, true=True):
        # print(self.focusWidget())
        CONF["MODIFIED"] = True if true else False
        self.renewal()

    def renewal(self):
        if not CONF["MODIFIED"]:
            self.setWindowTitle(f"{TEAM} {NAME} {VERSION} - {CONF['FILE_PATH']}"
                                if CONF['FILE_PATH'] is not None
                                else f"{TEAM} {NAME} {VERSION} - 빈 파일")
        elif CONF["MODIFIED"]:
            self.setWindowTitle(f"{TEAM} {NAME} {VERSION} - {CONF['FILE_PATH']}*"
                                if CONF['FILE_PATH'] is not None
                                else f"{TEAM} {NAME} {VERSION} - 제목 없음*")

    def _showFullScreen(self, checked):
        if checked:
            self.showFullScreen()
        else:
            self.showNormal()

    def is_modified(self) -> bool:
        return self.editor.scene.has_been_modified

    def maybe_save(self):
        if not (self.is_modified() or CONF["MODIFIED"]):
            return True

        res = QMessageBox.warning(None, f"{NAME} - 현재 파일이 변경됨",
                                  f"현재 파일 ["
                                  f"{CONF['FILE_PATH'] if CONF['FILE_PATH'] is not None else '제목 없음'}"
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
