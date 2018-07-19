import sys

import qdarkstyle
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QApplication

from code.executer import interpreter
from gui.window import Editor as MainWindow
from core.config import *


COMPILE_TEST = False


if COMPILE_TEST:
    interpreter('multinode.gvs')


def main():
    # TODO: unstable exit with unknown error with 0xC0000409:
    # see https://stackoverflow.com/questions/12827305/pyqt-application-close-with-error
    if COMPILE_TEST:
        return
    if RELEASE:
        sys.exit(0) \
            if len(sys.argv) == 1 else None
    app = QApplication([])
    QFontDatabase().addApplicationFont(r"gui\resources\NanumBarunpenR.ttf")
    # QFontDatabase().addApplicationFont(r"gui\resources\godoRounded L.ttf")

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setFont(QFont("나눔바른펜", 11))
    app.setWindowIcon(QIcon(r"gui\resources\icon.ico"))

    root = MainWindow()
    root.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    print(f"{NAME} {VERSION} [{TEAM} | {AUTHOR}]")
    main()
