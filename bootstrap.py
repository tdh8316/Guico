import os
import sys
import time

import qdarkstyle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QSplashScreen, QProgressBar

# from build_tools.compiler import interpreter
from gui.widgets.gif import MovieSplashScreen
from gui.window import MainForm
from core.config import *
from gui import theme

sys.path.append("./Engine")


COMPILE_TEST = False

# TODO: pygame 입력 이벤트 구현하기
# TODO: 프로젝트 기능 구현하기


def launch_window():
    app = QApplication([])
    QFontDatabase().addApplicationFont(r"NanumBarunpenR.ttf")
    # QFontDatabase().addApplicationFont(r"gui\resources\godoRounded L.ttf")

    '''splash = MovieSplashScreen(QMovie("gui/resources/splash.gif"
                                      if os.path.isfile("gui/resources/splash.gif")
                                      else "splash.gif"))
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)

    splash.setFont(QFont("나눔바른펜", 17))
    splash.setWindowTitle(" ".join([NAME, VERSION]))
    # splash.showMessage(f"{AUTHOR}'s {NAME} {VERSION}", alignment=Qt.AlignTop | Qt.AlignCenter, color=Qt.white)

    splash.setWindowIcon(QIcon(r"gui\resources\icon.ico"))

    splash.show()

    for i in range(31):
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

        # Simulate something that takes time'''

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setFont(QFont("나눔바른펜", 11))
    app.setWindowIcon(QIcon(r"gui\resources\icon.ico"
                      if os.path.isfile(r"gui\resources\icon.ico")
                      else r"icon.ico"))

    root = MainForm()
    # splash.finish(root)
    root.show()

    if COMPILE_TEST:
        root.hide()
        # interpreter('docs/example_pygame.gvs', mode="py", run=True, test=True)
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
