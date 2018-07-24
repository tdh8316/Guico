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
        print(f"\n{'=' * 50}\n{CONF['FILE_NAME']} Has started.\n{'=' * 50}")
        self.code = code

        for code in self.code:
            if code[0] == PRINT:
                self.print(code[1]["str"])

        print(f"\n{'=' * 50}\n{CONF['FILE_NAME']} Completed successfully.\n{'=' * 50}\n")

    @staticmethod
    def print(str_1: str, *args):
        print(str_1.replace("\\n", "\n"), end=str())


def interpreter(target, mode=None):
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
            BuildToPython(code=array)
        except Exception as e:
            QMessageBox.critical(None, f"{NAME} - 처리되지 않은 예외", f"{e}\n{sys.exc_info()}")
            parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [실패].")
        else:
            parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [성공].")
            subprocess.Popen(["python", CONF["SOURCE_PATH"]], shell=True, start_new_session=True)
        # os.system(f"start /B start cmd @cmd /k python {CONF['SOURCE_PATH']}")
