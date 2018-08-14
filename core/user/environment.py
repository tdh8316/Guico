import os
import json
import subprocess
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from core.config import *


class Composition(QWizard):

    def __init__(self, parent=None):
        super(Composition, self).__init__(parent)
        self.setOption(QWizard.NoCancelButton)

        self.setWindowTitle(f"{NAME} 환경 구성")
        self.setFont(QFont("맑은 고딕"))

        self.addPage(PythonPage(self))

        self.resize(640, 480)

        self.finished.connect(self.finish)

    @staticmethod
    def launch():
        Composition().exec_()

    @staticmethod
    def finish():
        try:
            os.environ["PYTHON"]
        except KeyError:
            QMessageBox.information(None, f"{NAME} 실행 거부됨",
                                    f"{NAME} 실행에 필요한 필수 구성이 완료되지 않았습니다.")
            sys.exit(-1)

        if not os.path.isfile(os.path.join(os.environ["PYTHON"])):
            del os.environ["PYTHON"]


class PythonPage(QWizardPage):

    def __init__(self, parent=None):
        super(PythonPage, self).__init__(parent)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def initializePage(self):
        try:
            self.label_python = QLabel(f"{os.environ['PYTHON']}")
        except KeyError:
            self.label_python = QLabel("Cannot find python")

        self.button_python = QPushButton("Choose Python...")
        self.button_python.clicked.connect(self.setDefaultPython)

        self.layout.addWidget(QLabel("Current python :"), 0, 0)
        self.layout.addWidget(self.label_python, 0, 1)
        self.layout.addWidget(self.button_python, 0, 2)

    def setDefaultPython(self):
        f, filt = QFileDialog.getOpenFileName(self, f"{NAME} choose default python", '', "Python (python.exe)")
        if f != "":
            if b"Python" in subprocess.check_output(f"{f} -V"):
                py_res = (str(subprocess.check_output(f"{f} -V").decode("utf8")).split(" ")[1]).split(".")
                py_res[-1] = list(py_res[-1])[0]
                if int(py_res[0]) < 3 or int(py_res[1]) < 3:
                    QMessageBox.information(None, "N/A", "Requires Python 3.4 or later.")
                    self.label_python.setText("Requires Python 3.4 or later however your python is " + ".".join(py_res))
                else:
                    os.environ["PYTHON"] = f
                    self.label_python.setText(f + f'[{".".join(py_res)}]')
            else:
                self.label_python.setText("선택된 파일에서 올바른 구성 요소를 찾지 못했습니다.")
