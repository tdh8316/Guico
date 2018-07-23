import autopep8

from compiler.generator import pygame
from core.config import *


def indent(level=1):
    return "    " * level


class BuildToPython:

    def __init__(self, code):
        # print(f"{NAME}Build::Python:{compiler}")
        self.code = code
        self.output: list = []

        self.used_label = False

        self.generate_code()
        self.refactoring_code()

        print(f"{NAME}Build::Python:Completed", )
        CONF["SOURCE_PATH"] = str(CONF["FILE_NAME"]).split("/")[-1].split(".")[0] + ".py"
        with open(CONF["SOURCE_PATH"], "w", encoding="utf-8") as _source:
            _source.write("\n".join(self.output))

    def refactoring_code(self):
        self.output = autopep8.fix_code("\n".join(self.output)).split("\n")
        # print(self.output)

        if not (self.used_label):
            return True

        for _ in range(len(self.output)):
            if self.output[_] == "# define point":
                if self.used_label:
                    self.output[_] = "# define point\n"+pygame.LABEL()

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
                self.add_to_code(pygame.WINDOW())
            elif code_type == DRAW_TEXT:
                self.used_label = True
                self.add_to_code(f"{indent(2)}message_display(\"{code_content['str']}\")")

    def add_to_code(self, line):
        self.output.append(line)

    def print(self, str_1: str, option=str()):
        try:
            int(eval(str_1))
        except ValueError and NameError and SyntaxError:
            return "print(\"" + str_1 + "\", " + f"end=\"{option}\")"
        else:
            return f"print({str_1}, end=\"{option}\")"
