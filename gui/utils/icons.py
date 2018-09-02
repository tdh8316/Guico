from os.path import isfile

from PyQt5.QtGui import QIcon


BASE_DIR = "./images/{}.png"


def get_icon(name: str):
    if isfile(BASE_DIR.format(name)):
        return QIcon(BASE_DIR.format(name))
    return QIcon()
