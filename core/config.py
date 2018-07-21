NAME = "Guico"
AUTHOR = "tdh8316@naver.com"
TEAM = "TakturStudio"
VERSION = "Pre-Alpha 5"
OPEN_SOURCE_LICENSE = open(r"doc\LICENSE.txt", "r", encoding="utf-8").read()

FILE_TYPES = f"{NAME} script files (*.gvs);;" \
             "모든 파일 (*.*)"

CONF = {
    "FILE_NAME": None,
    "MODIFIED": False,
    "MOUSE_X": int,
    "MOUSE_Y": int
}

LEAF_TYPES = {
    "Entry": "Entry",
    "CONSOLE": ["Print", "Input"],
    "WINDOW": ["New Window", "Destroy Window"],
}

ALL_LEAF_TYPES = [
    "Entry",
    "Print",
    "Input",
    "New Window",
    "Destroy Window"
]

INDEX = None

RELEASE = False
