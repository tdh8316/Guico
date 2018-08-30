from contents.default import *

# title, bg, width, height
NODE_UI: dict = {
    # IF: ("만약", "#01579B"),
    # PRINT: ("출력 (STDIO)", "#F57C00"),
    # INPUT: ("입력 (STDIO)", "#F57C00"),

    # TYPE : EVENT
    ENTRY_POINT: ("EntryPoint", "#4CAF50", 180, 61),
    KEY_INPUT: ("[a]{}".format(KEY_INPUT), "#4CAF50", 180, 76),

    # TYPE : LOOKS
    WINDOW_NEW: ("Window Initializer", "#498DEB", 200, 100),
    DRAW_TEXT: ("화면에 글쓰기", "#498DEB"),
    SCREEN_CLEAR: (SCREEN_CLEAR, "#498DEB"),
    DRAW_IMAGE: ("화면에 사진 추가", "#EC4466"),  # , 180, 76)

    # TYPE : STANDARD
    VARIABLE_CHANGE: (VARIABLE_CHANGE, "#CC7337", ),
    VARIABLE_PLUS: (VARIABLE_PLUS, "#CC7337",),
}
