import os
import sys
import shutil

from PyQt5.QtWidgets import QMessageBox

from core.config import *
from build_tools.packager.python_environment import MakePyEnv


parent = None


def initialize(_parent):
    global parent
    parent = _parent


def packaging_windows(bsd):
    if (bsd or CONF['SOURCE_PATH'] or CONF['FILE_PATH']) is None:
        QMessageBox.critical(None, "패키징 실패", "패키징 실패!")
        return False
    try:
        parent.log.appendPlainText(f"{CONF['FILE_PATH']} 에 대한 패키징 시작...")
        MakePyEnv(basedir=bsd)
        shutil.copy("NanumBarunpenR.ttf", os.path.join(bsd, "NanumBarunpenR.ttf"))
        with open(os.path.join(bsd, "bootstrapper.cmd"), "w") as script:
            script.write("@ECHO OFF\n")
            script.write(f".\Binaries\python.exe "
                         r".\Binaries\\" +
                         os.path.join(CONF['SOURCE_PATH'].replace("/", "\\").split('\\')[-1].split('.')[0]))
        QMessageBox.information(None, "패키징 완료",
                                f"{CONF['FILE_PATH']} 의 Windows 에 대한 패키징을 완료했습니다!")
        os.system(f"explorer {bsd}")

    except Exception as e:
        QMessageBox.critical(
            None, "패키징 실패", f"패키징 실패!\n{e}\n{sys.exc_info()}\n{sys.exc_info()[2].tb_lineno}")

