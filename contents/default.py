PRINT = "Print"
INPUT = "Input"
IF = "Branch"

WINDOW_NEW = "창 만들기"
# WINDOW_DESTROY = "Destroy Window"
DRAW_TEXT = "화면에 글쓰기"
SCREEN_CLEAR = "화면 지우기"
DRAW_IMAGE = "새 이미지"

KEY_INPUT = "키가 눌려있을 때"
ENTRY_POINT = "시작했을 때"

VARIABLE_NEW = "새 변수"
VARIABLE_CHANGE = "변수 값 정하기"

# ================================================================================================== #


ALL_VARIABLE_NAME = dir()[0:-8]
# print(ALL_LEAF_TYPES)

GetNameFromStr = {}
for i in range(len(ALL_VARIABLE_NAME)):
    GetNameFromStr[locals()[ALL_VARIABLE_NAME[i]]] = ALL_VARIABLE_NAME[i]

ALL_LEAF_TYPES = []
for _LEAF_TYPE in ALL_VARIABLE_NAME:
    ALL_LEAF_TYPES.append(locals()[_LEAF_TYPE])

# print(ALL_LEAF_TYPES)
# print(GetNameFromStr)
