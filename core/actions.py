import json
import os
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from gui import theme
from gui.node.node import Node as CreateNode
from gui.node.graphics_node import QDMGraphicsNode
from gui.dialogs import OpenSourceLicense, setLeafType

from build_tools.compiler import build
from build_tools.packager import *
from core.config import *
from gui.utils.icons import get_icon
from gui.utils.image import save_node_as_image

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
    if CONF["FILE_PATH"] is None:
        _name, _filter = QFileDialog.getSaveFileName(parent, f'{NAME} - 저장', '', FILE_TYPES)
        if _name == '':
            return False
        CONF["FILE_PATH"] = _name
    parent.editor.scene.saveToFile(CONF["FILE_PATH"])
    parent.statusBar().showMessage("Successfully saved %s" % CONF["FILE_PATH"])
    parent.signal_change_editor(False)
    parent.renewal()
    return True


def file_new():
    return QAction(get_icon("filenew"),
                   "새 파일 (&N)", parent, shortcut="Ctrl+N", triggered=lambda:
    QMessageBox.information(None, "0", "0"))


def file_open():
    return QAction(get_icon("fileopen"),
                   "열기 (&O)", parent, shortcut="Ctrl+O", triggered=lambda:
    parent.load())


def file_save():
    return QAction(get_icon("filesave"),
                   "저장 (&A)", parent, shortcut="Ctrl+S", triggered=lambda:
    parent.save())


def file_save_as():
    return QAction(get_icon("filesaveas"),
                   "다른 이름으로 저장 (&A)...", parent, shortcut="Ctrl+Shift+S", triggered=lambda:
    parent.save_as())


def file_save_as_image():
    return QAction("파일을 사진으로 저장", parent, shortcut="Ctrl+I", triggered=lambda:
    save_node_as_image(target=parent.editor, parent=parent))


def undo():
    return QAction(get_icon("undo"),
                   "실행 취소 (&U)", parent, shortcut="Ctrl+Z", triggered=lambda:
    parent.editor.scene.history.undo())


def redo():
    return QAction(get_icon("redo"),
                   "다시 실행 (&R)", parent, shortcut="Ctrl+Shift+Z", triggered=lambda:
    parent.editor.scene.history.redo())


def cut():
    def _cut():
        data = parent.editor.scene.clipboard.serializeSelected(delete=True)
        QApplication.instance().clipboard().setText(json.dumps(data, indent=4))

    return QAction(get_icon("cut"),
                   "잘라내기 (&U)", parent, shortcut="Ctrl+X", triggered=lambda:
    _cut())


def copy():
    return QAction(get_icon("copy"),
                   "복사 (&C)", parent, shortcut="Ctrl+C",
                   triggered=lambda: QApplication.instance().clipboard().setText(
                       json.dumps(parent.editor.scene.clipboard.serializeSelected(delete=False), indent=4)))


def _paste():
    try:
        data = json.loads(QApplication.instance().clipboard().text())
    except Exception as e:
        QMessageBox.warning(None, "올바른 JSON 자료가 아닙니다.", "JSON 에서 인식할 수 없는 자료 형식입니다.\n"
                                                        f"{e}")
        return False

    # check if the json data are correct
    if 'nodes' not in data or data['nodes'] == []:
        QMessageBox.warning(None, "올바른 자료 구조가 아닙니다.", f"{NAME} 에서 인식할 수 없는 자료 형식입니다.")
        return False
    parent.editor.scene.clipboard.deserializeFromClipboard(data)


def paste():
    return QAction(get_icon("paste"),
                   "붙여넣기 (&P)", parent, shortcut="Ctrl+V", triggered=lambda:
    _paste())


def delete():
    return QAction(get_icon("delete"),
                   "지우기 (&D)", parent, shortcut="Del", triggered=lambda:
    parent.editor.scene.grScene.views()[0].deleteSelected())


def save_to_py(f):
    parent.save()
    if build(f if f is not None else CONF["FILE_PATH"], mode="py", ):
        QMessageBox.information(None, "빌드 성공!", "작업이 완료되었습니다.")
    else:
        return False


def run():
    def _save_and_run(f):
        on_file_save()
        build(f if f is not None else CONF["FILE_PATH"])

    return QAction("R&un_TEST", parent, shortcut="Shift+F5", triggered=lambda:
    _save_and_run(CONF["FILE_PATH"]))


def run_as_python():
    def _save_and_run(f):
        parent.save()
        build(f if f is not None else CONF["FILE_PATH"], mode="py", run=True)

    return QAction(get_icon("run"),
                   "컴파일 후 실행(&U)", parent, shortcut="F5", triggered=lambda:
    _save_and_run(CONF["FILE_PATH"]))


def run_as_python__dev():
    def _save_and_run(f):
        parent.save()
        build(f if f is not None else CONF["FILE_PATH"], mode="py", run=True, test=True)

    return QAction("컴파일 후 실행 (개발 중 디버깅용)(&U)", parent, shortcut="F1", triggered=lambda:
    _save_and_run(CONF["FILE_PATH"]))


def compile_to_python():
    return QAction("Python Code 로 변환", parent, shortcut="Shift+F5", triggered=lambda:
    save_to_py(CONF["FILE_PATH"]))


def packaging():
    def _():
        if save_to_py(CONF["FILE_PATH"]):
            _dir, kw = QFileDialog.getExistingDirectory(parent, f"{NAME} - "
                                                                f"패키징 폴더 지정",
                                                        os.path.expanduser("~"),
                                                        QFileDialog.ShowDirsOnly)
            if not os.path.isdir(_dir):
                return False
            packaging_windows(bsd=_dir)
        else:
            QMessageBox.information(None, "패키징 실패!", "죄송 ㅠ")

    return QAction("패키징(&P)...", parent, shortcut="", triggered=lambda:
    _())


'''def build_and_run():
    return QAction("R&un", parent, shortcut="Shift+F5", triggered=lambda:
    parent.editor.scene.grScene.views()[0].deleteSelected())'''


def license_dialog():
    return QAction("라이선스", parent, shortcut="", triggered=lambda:
    OpenSourceLicense(parent))


def on_scene_pos_changed(x, y):
    # parent.status_mouse_pos.setText("Mouse Pos(%d, %d)" % (x, y))
    CONF["MOUSE_X"], CONF["MOUSE_Y"] = x, y


def on_new_leaf(x, y, defined=False):
    global leaf_count
    leaf_count += 1
    x
    y
    # noinspection PyBroadException
    # try:
    if not defined:
        '''while True:
            str_1, _make = setLeafType.get(parent=parent)

            if not _make:
                if str_1 is not None:
                    return False
                elif str_1 == "CANCELED":
                    return False
            else:
                break'''
        setLeafType.make(parent)
        #                         ↓TODO: Show(s) the icon of its function.
        # exec(f'Leaf{leaf_count} = CreateNode(editor.scene, " ", inputs=[0,], outputs=[1], types=str_1)')
        # exec(f'Leaf{leaf_count}.setPos(x, y)')

    elif type(defined) == str:
        #                         ↓TODO: Show(s) the icon of its function.
        exec(f'Leaf{leaf_count} = CreateNode(editor.scene, " ", inputs=[0,], outputs=[1], types=defined)')
        exec(f'Leaf{leaf_count}.setPos(x, y)')

    parent.signal_change_editor()


def test_on_new_leaf():
    if setLeafType(parent).exec_():
        print("exec")
    else:
        print("else")
    import sys
    sys.exit()


def new_leaf():
    return QAction("새 잎 만들기", parent, shortcut="Ctrl+L",
                   triggered=lambda: on_new_leaf(CONF["MOUSE_X"], CONF["MOUSE_Y"]))


def create_editor_menu(p, QContextMenuEvent):
    menu = QMenu(p)
    # menu.setFont(QFont("나눔바른펜", 10))
    '''menu.addAction(QAction("이 위치(%s,%s)에 새 잎 만들기" %
                           (CONF["MOUSE_X"], CONF["MOUSE_Y"]), p, shortcut="Ctrl+L",
                           triggered=lambda: on_new_leaf(CONF["MOUSE_X"], CONF["MOUSE_Y"])))'''
    if parent.editor.scene.clipboard.itemSelected():
        menu.addAction(QAction("선택한 잎 복사", p, triggered=lambda: QApplication.instance().clipboard().setText(
            json.dumps(parent.editor.scene.clipboard.serializeSelected(delete=False), indent=4))))
        menu.addAction(QAction("선택한 잎 제거", p, triggered=lambda: parent.editor.scene.grScene.views()[0].deleteSelected()))
        menu.addAction(QAction("선택한 잎 잘라내기", p, triggered=lambda: QApplication.instance().clipboard().setText(
            json.dumps(parent.editor.scene.clipboard.serializeSelected(delete=True), indent=4))))
    else:
        menu.addAction(QAction("붙여넣기", p, triggered=lambda: _paste()))
        menu.addAction(QAction("실행 취소", p, triggered=lambda: parent.editor.scene.history.undo()))
        menu.addAction(QAction("마지막 작업 다시 실행", p, triggered=lambda: parent.editor.scene.history.redo()))
        menu.addAction(file_save_as_image())
    menu.exec_(QContextMenuEvent.globalPos())
