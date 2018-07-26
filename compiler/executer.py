import datetime
import os
import subprocess
import sys

from PyQt5.QtWidgets import QPlainTextEdit, QMessageBox

from compiler.parser.script_parser import Parse
from compiler.parser.script_lexer import Lexer
from compiler.parser.combiner import Combiner

# from core.actions import on_file_save as save
from core.config import *
from compiler.build import BuildToPython
from compiler import build

parent = None


def initialize(_parent):
    global parent
    parent = _parent
    build.initialize(parent)


class ConvertToC:

    def __init__(self, code):
        pass


class PromptlyExecute:

    def __init__(self, code):
        print(f"\n{'=' * 50}\n{CONF['FILE_PATH']} Has started.\n{'=' * 50}")
        self.code = code

        for code in self.code:
            if code[0] == PRINT:
                self.print(code[1]["str"])

        print(f"\n{'=' * 50}\n{CONF['FILE_PATH']} Completed successfully.\n{'=' * 50}\n")

    @staticmethod
    def print(str_1: str, *args):
        print(str_1.replace("\\n", "\n"), end=str())


def interpreter(target, mode=None, run=False, test=False):
    parent.log: QPlainTextEdit

    if mode is None:
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

            array = Combiner(raw_scr, connector).combine()

            # print(array)
        else:
            array = parser.get_token()[0]

        # print(array)

        PromptlyExecute(array)

    elif mode == "py":
        if not test:
            parent.log.appendPlainText(f"\n{str(datetime.datetime.now()).split('.')[0]} 에 빌드 시작.")
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

            array = Combiner(raw_scr, connector).combine()

            # print(array)
        else:
            array = parser.get_token()[0]

        # noinspection PyBroadException
        try:
            python_code = BuildToPython(code=array).get_code()
            CONF[
                "SOURCE_PATH"
            ] = os.path.join(
                "/".join(
                    list(CONF["FILE_PATH"].split("/")[:-1])),
                (CONF["FILE_PATH"].split("/")[-1].split(".")[0] + ".py"))
            with open(CONF["SOURCE_PATH"], "w", encoding="utf-8") as _source:
                _source.write("\n".join(python_code))
            os.system(f"copy NanumBarunpenR.ttf " + "\"" + "\\".join(
                list(CONF["FILE_PATH"].split("/")[:-1])) + "\"") \
                if not os.path.isfile("\\".join(list(CONF["FILE_PATH"].split("/")[:-1]))+r'\NanumBarunpenR.ttf') \
                else None
        except Exception as e:
            QMessageBox.critical(None, f"{NAME} - 처리되지 않은 예외", f"{e}\n{sys.exc_info()}")
            if not test:
                parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [실패].")
        else:
            if not test:
                parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [성공].")
            # sys.path.append("\\".join(list(CONF["FILE_PATH"].split("/")[:-1])))
            if run:
                subprocess.Popen(f".\\python\\python.exe \"{CONF['SOURCE_PATH']}\"", shell=True, start_new_session=True)
        # os.system(f"start /B start cmd @cmd /k python {CONF['SOURCE_PATH']}")
