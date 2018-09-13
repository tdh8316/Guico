from os.path import isfile

from PyQt5.QtGui import QIcon

BASE_DIR = "./images/{}.png"


def get_icon(name: str):
    if isfile(BASE_DIR.format(name)):
        return QIcon(BASE_DIR.format(name))
    return QIcon()


def get_icon_s(name: str) -> str or bool:
    if isfile(BASE_DIR.format(name)):
        return BASE_DIR.format(name)
    else:
        return False
