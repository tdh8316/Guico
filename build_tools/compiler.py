import datetime
import os
import shutil
import subprocess
import sys

from PyQt5.QtWidgets import QPlainTextEdit, QMessageBox

from build_tools.check_validity import CheckValidity
from build_tools.parser.script_parser import Parse
from build_tools.parser.script_lexer import Lexer
from build_tools.parser.combiner import Combiner, CombinerTest

# from core.actions import on_file_save as save
from core.config import *
from build_tools.makefile import MakeTokenIntoPyCode
from build_tools import makefile, packager

parent = None


def initialize(_parent):
    global parent
    parent = _parent
    makefile.initialize(parent)
    packager.initialize(parent)


def build(target, mode=None, run=False, test=False):
    parent.log: QPlainTextEdit

    if mode == "py":
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

            array = CombinerTest(raw_scr, connector).combine()
                    # Combiner(raw_scr, connector).combine() if not test else CombinerTest(raw_scr, connector).combine()

            # print(array)
        else:
            array = parser.get_token()[0]

        # noinspection PyBroadException
        try:
            CheckValidity(array)
            python_code: str = MakeTokenIntoPyCode(array).get_code()
            if test:
                print(python_code)
            CONF[
                "SOURCE_PATH"
            ] = os.path.join(
                "/".join(
                    list(CONF["FILE_PATH"].split("/")[:-1])),
                (CONF["FILE_PATH"].split("/")[-1].split(".")[0] + ".py"))
            with open(CONF["SOURCE_PATH"], "w", encoding="utf-8") as _source:
                _source.write(python_code)
            os.system(f"copy NanumBarunpenR.ttf " + "\"" + "\\".join(
                list(CONF["FILE_PATH"].split("/")[:-1])) + "\"") \
                if not os.path.isfile("\\".join(list(CONF["FILE_PATH"].split("/")[:-1])) + r'\NanumBarunpenR.ttf') \
                else None
            # Copy Guico Game Engine
            if not os.path.isdir("/".join(CONF["SOURCE_PATH"].replace("\\", "/").split("/")[0:-1]) + "/Engine/"):
                shutil.copytree("./Engine/",
                                "/".join(CONF["SOURCE_PATH"].replace("\\", "/").split("/")[0:-1]) + "/Engine/")
        except Exception as e:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(None, f"{NAME} - 처리되지 않은 예외", f"{e}\n{sys.exc_info()}")
            if not test:
                parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [실패].")
        else:
            if not test:
                parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [성공].")
            # sys.path.append("\\".join(list(CONF["FILE_PATH"].split("/")[:-1])))
            if run:
                subprocess.Popen(f"{os.environ['PYTHON']} \"{CONF['SOURCE_PATH']}\"", shell=True,
                                 start_new_session=True)

            if test:
                print(array)

        # os.system(f"start /B start cmd @cmd /k python {CONF['SOURCE_PATH']}")
