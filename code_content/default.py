PRINT = "Print"
INPUT = "Input"
ENTRY_POINT = "시작했을 때"
IF = "Branch"

WINDOW_NEW = "창 만들기"
WINDOW_DESTROY = "Destroy Window"

DRAW_TEXT = "말하기"

# ================================================================================================== #


ALL_LEAF_TYPES = dir()[0:-8]
print(ALL_LEAF_TYPES)

GetNameFromStr = {}
for i in range(len(ALL_LEAF_TYPES)):
    GetNameFromStr[locals()[ALL_LEAF_TYPES[i]]] = ALL_LEAF_TYPES[i]
