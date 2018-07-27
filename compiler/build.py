import autopep8
from PyQt5.QtWidgets import QPlainTextEdit

from compiler.generator import pygame
from core.config import *


def indent(level=1):
    return "    " * level


parent = None


def initialize(_parent):
    global parent
    parent = _parent


class GuicoBuildError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class BuildToPython:

    def __init__(self, code):
        # print(f"{NAME}Build::Python:{compiler}")
        self.code = code
        self.output: list = []

        self.used_label = False
        self.is_window_init = False

        self.generate_code()
        self.refactoring_code()

        # print(f"{NAME}Build::Python:Completed", )

    def get_code(self):
        return self.output

    def refactoring_code(self):
        self.output = autopep8.fix_code("\n".join(self.output)).split("\n")
        # print(self.output)

        if not (self.used_label):
            return True
        else:
            e = ""
            if not self.is_window_init:
                e = "오류 : pygame window 가 초기화되지 않았습니다."
                parent.log: QPlainTextEdit
                parent.log.appendPlainText(e)
                raise GuicoBuildError(e)
            else:
                self.output.append(f"{indent()}pygame.display.update()\n{indent()}fps.tick(60)")

        for _ in range(len(self.output)):
            if self.output[_] == "# define point":
                if self.used_label:
                    self.output[_] = "# define point\n" + pygame.LABEL()

    def generate_code(self):
        for _ in ["import pygame\nfrom pygame.locals import *", "import sys"]:
            self.output.append(_)
        for code in self.code:
            code_type = code[0]
            code_content = code[1]

            if code_type == ENTRY_POINT:
                pass
            elif code_type == PRINT:
                self.add_to_code(self.print(code_content["str"]))
            elif code_type == WINDOW_NEW:
                self.is_window_init = True
                self.add_to_code(pygame.WINDOW(display_width=code_content["size"].split(',')[0],
                                               display_height=code_content["size"].split(',')[1]))
            elif code_type == DRAW_TEXT:
                self.used_label = True
                self.add_to_code(f"{indent(1)}message_display(\"{code_content['str']}\", "
                                 f"{int(code_content['pos'].split(',')[0])}, "
                                 f"{int(code_content['pos'].split(',')[1])})")

    def add_to_code(self, line):
        self.output.append(line)

    def print(self, str_1: str, option=str()):
        try:
            int(eval(str_1))
        except ValueError and NameError and SyntaxError:
            return "print(\"" + str_1 + "\", " + f"end=\"{option}\")"
        else:
            return f"print({str_1}, end=\"{option}\")"
