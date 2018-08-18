import os

NAME = "Guico"
AUTHOR = "tdh8316@naver.com"
TEAM = "TakturStudio"
VERSION = "0.6c2 빌드 193"
OPEN_SOURCE_LICENSE = open(r".\docs\LICENSE.txt", "r", encoding="utf-8").read()
TMP_PATH = os.path.join(os.path.expanduser("~"), f".{NAME}")
PREF_FILE = os.path.join(TMP_PATH, ".pref")
PERSON_IMAGE = (os.path.join("gui", "resources", "person.png")
                if os.path.isdir(os.path.join("gui", "resources"))
                else os.path.join("resources", "person.png"))
MAX_VAR = 99

FILE_TYPES = f"{NAME} script files (*.gvs);;" \
             "모든 파일 (*.*)"

CONF = {
    "FILE_PATH": None,
    "SOURCE_PATH": None,
    "MODIFIED": False,
    "MOUSE_X": int(),
    "MOUSE_Y": int()
}

INDEX = None

RELEASE = False
