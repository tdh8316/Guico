from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from gui.node.node import Node as CreateNode
from core.config import *

parent = None
editor = None


def initialize(self):
    global parent
    parent = self
    print(parent)


def set_editor(_):
    global editor
    editor = _


def new_file():
    return QAction("새 파일 (&N)", parent, shortcut="Ctrl+N", triggered=lambda: print("a"))


def new_leaf(x, y):
    str_1, _ = QInputDialog.getItem(parent, " ", "leaf type:.", ("조건문", "출력"), 0, False)
    if not _:
        return False
    CreateNode(editor.scene, str_1, inputs=[0, 0, 0], outputs=[1]).setPos(x, y)
