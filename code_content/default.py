PRINT = "Print"
INPUT = "Input"
ENTRY_POINT = "시작했을 때"
IF = "Branch"

WINDOW_NEW = "창 만들기"
WINDOW_DESTROY = "Destroy Window"

DRAW_TEXT = "말하기"

# ================================================================================================== #
LEAF_TYPES = {
    "Entry": ENTRY_POINT,
    "CONSOLE": [PRINT, INPUT],
    "WINDOW": [WINDOW_NEW, DRAW_TEXT],
}

'''ALL_LEAF_TYPES = [
    ENTRY_POINT,
    PRINT,
    INPUT,
    WINDOW_NEW,
    # WINDOW_DESTROY,
    DRAW_TEXT,
]'''

ALL_LEAF_TYPES = dir()[0:-9]

GetNameFromStr: dict = {PRINT: "PRINT",
                        INPUT: "INPUT",
                        ENTRY_POINT: "ENTRY_POINT",
                        IF: "IF",
                        WINDOW_NEW: "WINDOW_NEW",
                        DRAW_TEXT: "DRAW_TEXT"}
