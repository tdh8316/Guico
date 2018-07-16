import json
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from gui.node.node import Node as CreateNode
from gui.node.graphics_node import QDMGraphicsNode
from gui.dialogs import OpenSourceLicense

from core.code.executer import interpreter as _run
from core.config import *

parent: QInputDialog = None
editor = None
leaf_count = 0

CreateNode
QDMGraphicsNode


def initialize(self):
    global parent
    parent = self
    # print(parent)


def set_editor(_):
    global editor
    editor = _


def on_file_save():
    if CONF["FILE_NAME"] is None:
        _name, _filter = QFileDialog.getSaveFileName(parent, f'{NAME} - 저장', '', FILE_TYPES)
        if _name == '':
            return False
        CONF["FILE_NAME"] = _name
    parent.editor.scene.saveToFile(CONF["FILE_NAME"])
    parent.statusBar().showMessage("Successfully saved %s" % CONF["FILE_NAME"])
    parent.signal_change_editor(true=False)
    parent.renewal()
    return True


def file_new():
    return QAction("새 파일 (&N)", parent, shortcut="Ctrl+N", triggered=lambda:
    print("File new"))


def file_open():
    def _file_open():
        _name, _filter = QFileDialog.getOpenFileName(parent, f'{NAME} - 열기', '', FILE_TYPES)
        if _name == '':
            return
        if os.path.isfile(_name):
            parent.editor.scene.loadFromFile(_name)
            CONF["FILE_NAME"] = _name
            parent.renewal()
    return QAction("열기 (&O)", parent, shortcut="Ctrl+O", triggered=lambda:
    _file_open())


def file_save():
    def _file_save():
        if CONF["FILE_NAME"] is None:
            _name, _filter = QFileDialog.getSaveFileName(parent, f'{NAME} - 저장', '', FILE_TYPES)
            if _name == '':
                return False
            CONF["FILE_NAME"] = _name
        parent.editor.scene.saveToFile(CONF["FILE_NAME"])
        parent.statusBar().showMessage("Successfully saved %s" % CONF["FILE_NAME"])
        parent.signal_change_editor(true=False)
        parent.renewal()
        return True

    return QAction("저장 (&A)", parent, shortcut="Ctrl+S", triggered=lambda:
    _file_save())


def file_save_as():
    def _file_save_as():
        _name, _filter = QFileDialog.getSaveFileName(parent, f'{NAME} - 다른 이름으로 저장', '', FILE_TYPES)
        if _name == '':
            return False
        CONF["FILE_NAME"] = _name
        parent.editor.scene.saveToFile(CONF["FILE_NAME"])
        parent.statusBar().showMessage("Successfully saved %s" % CONF["FILE_NAME"])
        parent.signal_change_editor(true=False)
        parent.renewal()
        return True

    return QAction("다른 이름으로 저장 (&A)...", parent, shortcut="Ctrl+Shift+S", triggered=lambda:
    _file_save_as())


def undo():
    return QAction("실행 취소 (&U)", parent, shortcut="Ctrl+Z", triggered=lambda:
    parent.editor.scene.history.undo())


def redo():
    return QAction("다시 실행 (&R)", parent, shortcut="Ctrl+Shift+Z", triggered=lambda:
    parent.editor.scene.history.redo())


def cut():
    def _cut():
        data = parent.editor.scene.clipboard.serializeSelected(delete=True)
        QApplication.instance().clipboard().setText(json.dumps(data, indent=4))

    return QAction("잘라내기 (&U)", parent, shortcut="Ctrl+X", triggered=lambda:
    _cut())


def copy():
    def _copy():
        data = parent.editor.scene.clipboard.serializeSelected(delete=False)
        QApplication.instance().clipboard().setText(json.dumps(data, indent=4))

    return QAction("복사 (&C)", parent, shortcut="Ctrl+C", triggered=lambda:
    _copy())


def paste():
    def _paste():
        try:
            data = json.loads(QApplication.instance().clipboard().text())
        except Exception as e:
            print("Pasting of not valid json data!", e)
            return

        # check if the json data are correct
        if 'nodes' not in data:
            print("JSON does not contain any nodes!")
            return

        parent.editor.scene.clipboard.deserializeFromClipboard(data)

    return QAction("붙여넣기 (&P)", parent, shortcut="Ctrl+V", triggered=lambda:
    _paste())


def delete():
    return QAction("지우기 (&D)", parent, shortcut="Del", triggered=lambda:
    parent.editor.scene.grScene.views()[0].deleteSelected())


def run():
    def _save_and_run(f):
        on_file_save()
        _run(f)

    return QAction("R&un", parent, shortcut="Shift+F5", triggered=lambda:
    _save_and_run(CONF["FILE_NAME"]))


'''def build_and_run():
    return QAction("R&un", parent, shortcut="Shift+F5", triggered=lambda:
    parent.editor.scene.grScene.views()[0].deleteSelected())'''


def compile_and_run():
    """Convert .py to .exe and run"""
    return QAction("컴파일 후 실행 (&C)", parent, shortcut="F5", triggered=lambda:
    print())


def license_dialog():
    return QAction("오픈 소스 라이선스...", parent, shortcut="", triggered=lambda:
    OpenSourceLicense(parent))


def on_scene_pos_changed(x, y):
    parent.status_mouse_pos.setText("Mouse Pos(%d, %d)" % (x, y))
    CONF["MOUSE_X"], CONF["MOUSE_Y"] = x, y


def on_new_leaf(x, y):
    global leaf_count
    leaf_count += 1
    str_1, _ = QInputDialog.getItem(parent, " ", "Set this type of leaf:", CONF["LEAF_TYPES"], 0, False,
                                    Qt.FramelessWindowHint)
    if not _:
        return False
    #                         ↓TODO: Show(s) the icon of its function.

    exec(f'Leaf{leaf_count} = CreateNode(editor.scene, " ", inputs=[0, ], outputs=[1], types=str_1)')
    exec(f'Leaf{leaf_count}.setPos(x, y)')
    parent.signal_change_editor()


def create_editor_menu(p, QContextMenuEvent):
    menu = QMenu(p)
    menu.addAction(QAction("새 잎 만들기", p, shortcut="Ctrl+l",
                           triggered=lambda: on_new_leaf(CONF["MOUSE_X"], CONF["MOUSE_Y"])))
    menu.exec_(QContextMenuEvent.globalPos())
