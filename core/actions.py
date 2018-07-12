from PyQt5.QtWidgets import QAction
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from gui.node.node import Node

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


def on_new_leaf():
    node1 = Node(editor.scene, "My Awesome Node 1", inputs=[0, 0, 0], outputs=[1])
