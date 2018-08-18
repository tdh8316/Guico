import os
import sys
import shutil

from PyQt5.QtWidgets import QMessageBox

from core.config import *


parent = None


def initialize(_parent):
    global parent
    parent = _parent


def packaging_windows(bsd):
    parent.log.appendPlainText(f"{CONF['FILE_PATH']} 에 대한 패키징 시작...")

