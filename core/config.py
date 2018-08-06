from code_content.default import *

NAME = "Guico"
AUTHOR = "tdh8316@naver.com"
TEAM = "TakturStudio"
VERSION = "0.4fa31 빌드 128"
OPEN_SOURCE_LICENSE = open(r".\docs\LICENSE.txt", "r", encoding="utf-8").read()

FILE_TYPES = f"{NAME} script files (*.gvs);;" \
             "모든 파일 (*.*)"

CONF = {
    "FILE_PATH": None,
    "SOURCE_PATH": None,
    "MODIFIED": False,
    "MOUSE_X": int,
    "MOUSE_Y": int
}

LEAF_TYPES = {
    "Entry": ENTRY_POINT,
    "CONSOLE": [PRINT, INPUT],
    "WINDOW": [WINDOW_NEW, DRAW_TEXT],
}

ALL_LEAF_TYPES = [
    ENTRY_POINT,
    PRINT,
    INPUT,
    WINDOW_NEW,
    # WINDOW_DESTROY,
    DRAW_TEXT,
]

INDEX = None

RELEASE = False
