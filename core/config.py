from code_content.default import *

NAME = "Guico"
AUTHOR = "tdh8316@naver.com"
TEAM = "TakturStudio"
VERSION = "0.4fa31 빌드 137"
OPEN_SOURCE_LICENSE = open(r".\docs\LICENSE.txt", "r", encoding="utf-8").read()

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
