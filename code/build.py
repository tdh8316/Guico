import autopep8

from core.config import *


class BuildToPython:

    def __init__(self, code):
        # print(f"{NAME}Build::Python:{code}")
        self.code = code
        self.output: list = []

        self.generate_code()

        print(f"{NAME}Build::Python:Completed", )
        CONF["SOURCE_PATH"] = str(CONF["FILE_NAME"]).split("/")[-1].split(".")[0] + ".py"
        with open(CONF["SOURCE_PATH"], "w", encoding="utf-8") as _source:
            _source.write(autopep8.fix_code("\n".join(self.output)))

    def generate_code(self):
        for code in self.code:
            code_type = code[0]
            code_content = code[1]

            if code_type == ENTRY_POINT:
                pass
            elif code_type == PRINT:
                self.add_to_code(self.print(code_content["str"]))
            elif code_type == WINDOW_NEW:
                self.add_to_code(open(SOURCE_PATH+"pygame_window.py").read())

    def add_to_code(self, line):
        self.output.append(line)

    def print(self, str_1: str, option=str()):
        try:
            int(eval(str_1))
        except ValueError and NameError and SyntaxError:
            return "print(\"" + str_1 + "\", " + f"end=\"{option}\")"
        else:
            return f"print({str_1}, end=\"{option}\")"
