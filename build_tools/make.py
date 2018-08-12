import autopep8
from PyQt5.QtWidgets import QPlainTextEdit

from build_tools import generator
from leaf_content.default import *
from core.config import *


def indent(level=1):
    return "\t" * level


parent = None


def initialize(_parent):
    global parent
    parent = _parent


class GuicoBuildError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class MakeTokenIntoPyCode:
    def __init__(self, intercode):
        self.original_code = intercode
        self.converted_code = []
        self.python_main_code = ["\n"]

        for code in self.original_code:
            self.putting_code(code)

        self.converted_code.insert(0, "import Engine\n\n")
        self.converted_code.append(f"{indent(2)}Engine.display.update()")

    def putting_code(self, original):
        _type = original[0]
        contents = original[1]

        if _type == ENTRY_POINT:
            self.python_main_code.append(generator.PYTHON_MAIN)
        elif _type == WINDOW_NEW:
            self.python_main_code.append(indent(1) + generator.WINDOW_NEW.format(int(contents["size"].split(",")[0]),
                                                                                 int(contents["size"].split(",")[1]),
                                                                                 "Guico Display (pygame)"))
            self.python_main_code.append(indent(1) + "main()")
            self.converted_code.append(generator.DEF_MAIN)
        elif _type == KEY_INPUT:
            self.converted_code.append(generator.KEY_PRESSED.format(contents["key"]))
        elif _type == DRAW_TEXT:
            self.converted_code.append(generator.DRAW_TEXT.format(contents["str"],
                                                                  contents["pos"].split(",")[0],
                                                                  contents["pos"].split(",")[1])
                                       if not self.converted_code[-1].endswith(":")
                                       else indent(1) + generator.DRAW_TEXT.format(contents["str"],
                                                                                   contents["pos"].split(",")[0],
                                                                                   contents["pos"].split(",")[1]))

    def get_code(self) -> str:
        # print("\n".join(self.converted_code + self.python_main_code))
        return autopep8.fix_code("\n".join(self.converted_code + self.python_main_code))


class _MakeTokenIntoPyCode:

    def __init__(self, code):
        # print(f"{NAME}Build::Python:{build_tools}")
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

        if not self.is_window_init:
            if self.used_label:
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
            leaf_content = code[1]

            if code_type == ENTRY_POINT:
                pass
            elif code_type == PRINT:
                self.add_to_code(self.print(leaf_content["str"]))
            elif code_type == WINDOW_NEW:
                self.is_window_init = True
                self.add_to_code(pygame.WINDOW(display_width=leaf_content["size"].split(',')[0],
                                               display_height=leaf_content["size"].split(',')[1]))
            elif code_type == DRAW_TEXT:
                self.used_label = True
                self.add_to_code(f"{indent(1)}message_display(\"{leaf_content['str']}\", "
                                 f"{int(leaf_content['pos'].split(',')[0])}, "
                                 f"{int(leaf_content['pos'].split(',')[1])})")

    def add_to_code(self, line):
        self.output.append(line)

    # noinspection PyMethodMayBeStatic
    def print(self, str_1: str, option=str()):
        try:
            int(eval(str_1))
        except ValueError and NameError and SyntaxError:
            return "print(\"" + str_1 + "\", " + f"end=\"{option}\")"
        else:
            return f"print({str_1}, end=\"{option}\")"
