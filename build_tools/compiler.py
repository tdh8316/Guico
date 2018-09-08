import datetime
import os
import shutil
import subprocess
import sys
import time
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPlainTextEdit, QMessageBox, QApplication

from build_tools.check_validity import CheckValidity
from build_tools.makeengine import build_engine_archive
from build_tools.parser.script_parser import Parse
from build_tools.parser.script_lexer import Lexer
from build_tools.parser.combiner import Combiner, CombinerTest

# from core.actions import on_file_save as save
from core.config import *
from build_tools.makefile import MakeTokenIntoPyCode, GuicoBuildError
from build_tools import makefile, packager
from core.execute import Execute, execute_manager

parent = None


def initialize(_parent):
    global parent
    parent = _parent
    makefile.initialize(parent)
    packager.initialize(parent)


def build(target, mode=None, run=False, test=False):
    if target is None:
        print("build_tools.makefile.GuicoBuildError: 지정되지 않은 타겟")
        return False
    start_time = time.time()
    QApplication.setOverrideCursor(Qt.WaitCursor)
    parent.log: QPlainTextEdit
    parent.dock_log.show()

    if mode == "py":
        # if not test:
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

        if test:
            print("Generated token:\n", array)

        # noinspection PyBroadException
        try:
            CheckValidity(array)
            python_code: str = MakeTokenIntoPyCode(array).get_code()
            if test:
                print("Created code:\n", python_code)

            with open(CONF["SOURCE_PATH"], "w", encoding="utf-8") as _source:
                _source.write(python_code)

            os.system(f"copy font.ttf " + "\"" + "\\".join(
                list(CONF["FILE_PATH"].split("/")[:-1])) + "\"") \
                if not os.path.isfile("\\".join(list(CONF["FILE_PATH"].split("/")[:-1])) + r'\font.ttf') \
                else None

            # Copy Guico Game Engine
            '''if not os.path.isdir("/".join(CONF["SOURCE_PATH"].replace("\\", "/").split("/")[0:-1]) + "/Engine/"):
                shutil.copytree("./Engine/",
                                "/".join(CONF["SOURCE_PATH"].replace("\\", "/").split("/")[0:-1]) + "/Engine/")'''
            if not os.path.isfile(os.path.join(os.path.dirname(CONF["SOURCE_PATH"]), "Engine.dll")):
                if not os.path.isfile("./Engine.dll"):
                    build_engine_archive("Engine.dll", "./Engine/")
                os.system(f"copy Engine.dll \"{os.path.join(os.path.dirname(CONF['SOURCE_PATH']), 'Engine.dll')}\"")
        except IndexError:
            traceback.print_exc()
            QMessageBox.information(None, f"{NAME} 컴파일 오류", f"{NAME} 규칙에 맞지 않는 부분이 있는 것 같습니다.")
            parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [실패].")
            return False
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(None, f"{NAME} - 처리되지 않은 예외", f"{e}\n{sys.exc_info()}")
            # if not test:
            parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [실패].")
            return False
        else:
            # if not test:
            parent.log.appendPlainText(f"{str(datetime.datetime.now()).split('.')[0]} 에 빌드 완료 [성공].")
            parent.log.appendPlainText("소요 시간: %0.3fs" % float(time.time() - start_time))
            QApplication.restoreOverrideCursor()
            # sys.path.append("\\".join(list(CONF["FILE_PATH"].split("/")[:-1])))
            if run:
                execute_manager.precess_start()

            if test:
                print(array)

        del start_time

        # os.system(f"start /B start cmd @cmd /k python {CONF['SOURCE_PATH']}")
