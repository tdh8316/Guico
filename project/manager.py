import os
import json

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from core.config import *


def new(base, name, script="main.gvs"):
    _dir = os.path.join(base, name)

    packages_info: dict = {
        "GUICO_VERSION": VERSION,
        "NAME": name,
        "SCRIPT": script,
    }
    if os.path.isdir(_dir):
        if QMessageBox.Warning(None, f"{NAME} - 프로젝트 생성",
                               f"{_dir} 에 프로젝트를 생성하려고 했지만 이미 폴더가 존재합니다.\n"
                               f"무시하고 진행할까요?",
                               QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return False

    # 프로젝트 생성
    with open(_dir + name + ".json", "w", encoding="utf-8") as _:
        _.write(json.dumps(packages_info, indent=4))
