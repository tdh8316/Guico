import os

NAME = "Guico"
AUTHOR = "tdh8316@naver.com"
TEAM = "TakturStudio"
VERSION = "261"
EDITION = "Saucy Stone"


if os.name != "nt":
    print(f"{NAME} is not supported *nix systems.")
    input("Press Enter to continue (with error) or Ctrl+C to abort...")


TMP_PATH = os.path.join(os.path.expanduser("~"), f".{NAME}")
PREF_FILE = os.path.join(TMP_PATH, ".pref")
PLUGIN_DIR = "./plugins"
PERSON_IMAGE = (os.path.join(os.getcwd(), "images", "person.png"))
MAX_VAR = 99

FILE_TYPES = f"{NAME} script files (*.gvs);;" \
             "모든 파일 (*.*)"

CONF = {
    "FILE_PATH": None,
    "SOURCE_PATH": None,
    "MODIFIED": False,
    "MOUSE_X": int(),
    "MOUSE_Y": int(),
    "THEME": "BLACK"
}

INDEX = None

RELEASE = False

OPEN_SOURCE_LICENSE = """OPEN SOURCES LICENSE.

네이버 나눔글꼴
Copyright (c) 2010, NAVER Corporation (http://www.nhncorp.com),


with Reserved Font Name Nanum, Naver Nanum, NanumGothic, Naver NanumGothic, NanumMyeongjo, Naver NanumMyeongjo, NanumBrush, Naver NanumBrush, NanumPen, Naver NanumPen, Naver NanumGothicEco, NanumGothicEco, Naver NanumMyeongjoEco, NanumMyeongjoEco, Naver NanumGothicLight, NanumGothicLight, NanumBarunGothic, Naver NanumBarunGothic,

This Font Software is licensed under the SIL Open Font License, Version 1.1.

This license is copied below, and is also available with a FAQ at: http://scripts.sil.org/OFL

SIL OPEN FONT LICENSE

Version 1.1 - 26 February 2007

Node Editor UI
https://gitlab.com/pavel.krupala/pyqt-node-editor-tutorials

PyQt5
https://www.riverbankcomputing.com/software/pyqt

Python
https://docs.python.org/3.6/license.html"""
