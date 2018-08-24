import autopep8
from PyQt5.QtWidgets import QPlainTextEdit

from build_tools import generator
from contents.default import *
from core.config import *
from core import script_variables


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
        self.putting_variables()

        mod_ext = "/".join(CONF["FILE_PATH"].replace("\\", "/").split("/")[0:-1]) + "/Engine.dll"
        self.converted_code.insert(0, f"import sys\nsys.path.append(\"{mod_ext}\")\nimport Engine\n\n")
        self.converted_code.append(f"\n{indent(2)}Engine.display.update()")

    def putting_variables(self):
        for name in script_variables.globals.keys():
            try:
                int(script_variables.globals[name])
            except:
                if str(script_variables.globals[name]).endswith("'") or str(script_variables.globals[name]).endswith(
                        "\""):
                    py_code = "{0} = {1}".format(name, script_variables.globals[name])
                if os.path.isfile(script_variables.globals[name]):
                    py_code = "{0} = fr\"{1}\"".format(name, script_variables.globals[name])
                else:
                    py_code = "{0} = f\"{1}\"".format(name, script_variables.globals[name])
            else:
                py_code = "{0} = {1}".format(name, script_variables.globals[name])
            finally:
                # noinspection PyUnboundLocalVariable
                self.converted_code.insert(0, py_code)

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
            var = str()
            for var_item in list(script_variables.globals.keys()):
                var += "{}, ".format(var_item) if list(script_variables.globals.keys())[-1] != var_item else var_item
            self.converted_code.append(generator.DEF_MAIN.format(var))
        elif _type == KEY_INPUT:
            self.converted_code.append(generator.KEY_PRESSED.format(contents["key"]))
        elif _type == DRAW_TEXT:
            self.append_code(generator.DRAW_TEXT.format(contents["str"],
                                                        contents["pos"].split(",")[0],
                                                        contents["pos"].split(",")[1]))
        elif _type == SCREEN_CLEAR:
            self.append_code(generator.SCREEN_CLEAR)
        elif _type == DRAW_IMAGE:
            # TODO: 이미지 포지션 조정
            self.append_code(generator.DRAW_IMAGE.format(contents["path"],
                                                         "0", "0"))
        elif _type == VARIABLE_CHANGE:
            try:
                int(contents["value"])
                self.append_code("\t\t{} = {}".format(contents["name"], contents["value"]))
            except:
                self.append_code("\t\t{} = fr\"{}\"".format(contents["name"], contents["value"]))

    def get_code(self) -> str:
        return autopep8.fix_code("\n".join(self.converted_code + self.python_main_code))

    def append_code(self, item: str, syntax_indent: bool = True):
        if not syntax_indent:
            self.converted_code.append(item)
            return True

        if self.converted_code[-1].endswith(":") or self.converted_code[-1].startswith("\t\t\t"):
            self.converted_code.append(indent(1) + item)

        else:
            self.converted_code.append(item)


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
                self.add_to_code(f"{indent(1)}message_display(\"{contents['str']}\", "
                                 f"{int(contents['pos'].split(',')[0])}, "
                                 f"{int(contents['pos'].split(',')[1])})")

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
