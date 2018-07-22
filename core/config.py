from code.default import *

NAME = "Guico"
AUTHOR = "tdh8316@naver.com"
TEAM = "TakturStudio"
VERSION = "Pre-Alpha 5"
OPEN_SOURCE_LICENSE = open(r"doc\LICENSE.txt", "r", encoding="utf-8").read()

FILE_TYPES = f"{NAME} script files (*.gvs);;" \
             "모든 파일 (*.*)"

SOURCE_PATH = "./code/generator/sources/"

CONF = {
    "FILE_NAME": None,
    "SOURCE_PATH": None,
    "MODIFIED": False,
    "MOUSE_X": int,
    "MOUSE_Y": int
}

LEAF_TYPES = {
    "Entry": ENTRY_POINT,
    "CONSOLE": [PRINT, INPUT],
    "WINDOW": [WINDOW_NEW, WINDOW_DESTROY],
}

ALL_LEAF_TYPES = [
    ENTRY_POINT,
    PRINT,
    INPUT,
    WINDOW_NEW,
    WINDOW_DESTROY
]

INDEX = None

RELEASE = False
