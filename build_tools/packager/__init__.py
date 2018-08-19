import os
import sys
import shutil
import subprocess

from PyQt5.QtWidgets import QMessageBox

from core.config import *


parent = None


def initialize(_parent):
    global parent
    parent = _parent


def packaging_windows(bsd):
    parent.dock_log.show()
    if not os.path.isfile(os.path.join(os.path.dirname(os.environ["PYTHON"]), "Scripts", "pyinstaller.exe")):
        parent.log.appendPlainText("installing pyinstaller...")
        p = subprocess.Popen([os.environ["PYTHON"], "-m", "pip", "install", "pyinstaller"],
                             stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        p.wait()
        parent.log.appendPlainText(f"installed pyinstaller successfully {output}")
    parent.log.appendPlainText(f"{CONF['FILE_PATH']} 에 대한 패키징 시작...")

