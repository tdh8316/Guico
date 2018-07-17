from core.code.parser.script_parser import Parse
from core.code.parser.script_lexer import Lexer
from core.code.parser.combiner import Combiner

# from core.actions import on_file_save as save
from core.config import *


class ConvertToC:

    def __init__(self, code):
        pass


class PromptlyExecute:

    def __init__(self, code):
        print(f"\n{'=' * 50}\n{CONF['FILE_NAME']} Has started.\n{'=' * 50}")
        self.code = code

        for code in self.code:
            if code[0] == "Print":
                self.print(code[1]["str"])

        print(f"\n{'=' * 50}\n{CONF['FILE_NAME']} Completed successfully.\n{'=' * 50}\n")

    @staticmethod
    def print(str_1: str, *args):
        print(str_1.replace("\\n", "\n"), end=str())


def interpreter(target):
    try:
        lexer = Lexer(target)
    except IOError:
        return
    tokenize = lexer.lexer()

    parser = Parse(target=tokenize, edges=lexer.edges())
    if parser.leaves is not 1:
        raw_scr = parser.get_token()[0]
        # print(raw_scr)
        connector = parser.get_token()[1]

        # TODO: 노드 소켓의 시작 부분과 끝 부분으로 나눠진 데이터를 하나로 합치는 더 정교한 함수 필요...
        array = Combiner(code=raw_scr, conn=connector).combine()

        # print(array)
    else:
        array = parser.get_token()[0]

    print(array)

    PromptlyExecute(array)
