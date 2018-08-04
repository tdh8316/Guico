import os
import sys
import time

import qdarkstyle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, QProgressBar

# from build_tools.compiler import interpreter
from gui.window import MainForm
from core.config import *
from gui import theme


COMPILE_TEST = False

# TODO: pygame 입력 이벤트 구현하기
# TODO: 프로젝트 기능 구현하기


def launch_window():
    app = QApplication([])
    QFontDatabase().addApplicationFont(r"NanumBarunpenR.ttf")
    app.setFont(QFont("나눔바른펜", 11))
    # QFontDatabase().addApplicationFont(r"gui\resources\godoRounded L.ttf")

    splash_pm = QPixmap("gui/resources/splash.png")
    splash = QSplashScreen(splash_pm, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(100)
    progressBar.setGeometry(0, splash_pm.height() - 25, splash_pm.width() + 50, 100)
    splash.setFont(QFont("나눔바른펜", 17))
    splash.setWindowTitle(" ".join([NAME, VERSION]))
    splash.showMessage(f"{AUTHOR}'s {NAME} {VERSION}", Qt.AlignTop | Qt.AlignCenter, Qt.white)
    splash.show()

    for i in range(90):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.025:
            app.processEvents()

        # Simulate something that takes time
    time.sleep(1.25)

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setWindowIcon(QIcon(r"gui\resources\icon.ico"))

    root = MainForm()
    root.show()
    splash.finish(root)

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
