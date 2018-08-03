import os
import sys

import qdarkstyle
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QApplication

# from build_tools.compiler import interpreter
from gui.window import Editor as MainWindow
from core.config import *
from gui import theme


COMPILE_TEST = False

# TODO: pygame 입력 이벤트 구현하기
# TODO: 프로젝트 기능 구현하기


def launch_window():
    app = QApplication([])
    QFontDatabase().addApplicationFont(r"NanumBarunpenR.ttf")
    # QFontDatabase().addApplicationFont(r"gui\resources\godoRounded L.ttf")

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setFont(QFont("나눔바른펜", 11))
    app.setWindowIcon(QIcon(r"gui\resources\icon.ico"))

    root = MainWindow()
    root.show()

    if COMPILE_TEST:
        root.hide()
        interpreter('docs/example_pygame.gvs', mode="py", run=True, test=True)
        sys.exit(0)

    return app.exec_()


def main():
    # TODO: unstable exit with unknown error with 0xC0000409:
    # see https://stackoverflow.com/questions/12827305/pyqt-application-close-with-error
    if COMPILE_TEST:
        return

    if not os.path.isfile(os.environ['PYTHON']):
        sys.exit("PYTHON NOT FOUND.")

    return launch_window()


if __name__ == "__main__":
    os.environ['PYTHON'] = ".\\python\\python.exe"
    print(f"{NAME} {VERSION} [{TEAM} | {AUTHOR}]")
    sys.exit(main())
