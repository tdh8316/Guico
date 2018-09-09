from contents.default import *

# title, bg, width, height
NODE_UI: dict = {
    # IF: ("만약", "#01579B"),
    # PRINT: ("출력 (STDIO)", "#F57C00"),
    # INPUT: ("입력 (STDIO)", "#F57C00"),

    # TYPE : EVENT
    ENTRY_POINT: ("EntryPoint", "#4CAF50", 180, 61),
    KEY_INPUT: ("[a]{}".format(KEY_INPUT), "#4CAF50", 180, 76),
    KEY_NOT_INPUT: (KEY_NOT_INPUT, "#4CAF50", 180, 61),
    DETECT_COLLISION: (DETECT_COLLISION, "#4CAF50", 180, 61),

    # TYPE : LOOKS
    WINDOW_NEW: ("Window Initializer", "#498DEB", 200, 100),
    DRAW_TEXT: ("화면에 글쓰기", "#EC4466"),
    SCREEN_CLEAR: (SCREEN_CLEAR, "#EC4566"),
    DRAW_IMAGE: ("화면에 사진 추가", "#EC4466"),  # , 180, 76)
    DRAW_SPRITE: (DRAW_SPRITE, "#EC4466", 180, 76),

    # TYPE : STANDARD
    VARIABLE_DEFINE: (VARIABLE_DEFINE, "#E456DC",),
    VARIABLE_PLUS: ("변수에 연산하기", "#E456DC",),
    ADD_GROUP: (ADD_GROUP, "#E456DC",),
}
