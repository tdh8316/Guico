import os

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core.config import NAME


def save_node_as_image(target: QWidget, parent: QMainWindow):
    _name, _filter = QFileDialog.getSaveFileName(None, f'{NAME} - 노드를 사진으로 저장', os.path.expanduser("~"), "png (*.png)")
    target.grab().save(_name, "png")
