NAME = "Guico"
AUTHOR = "tdh8316@naver.com"
TEAM = "TakturStudio"
VERSION = "0.12.1"
OPEN_SOURCE_LICENSE = open(r"doc\LICENSE.txt", "r", encoding="utf-8").read()

FILE_TYPES = f"{NAME} script files (*.gvs);;" \
             "모든 파일 (*.*)"

CONF = {"FILE_NAME": None,
        "MODIFIED": False,
        "MOUSE_X": int,
        "MOUSE_Y": int,
        "LEAF_TYPES": ("Print", "Entry"),  #("Branch", "Print"),
        }
