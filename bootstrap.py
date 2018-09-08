print("01. Importing core libraries")

import os
import sys
import json
import atexit
import argparse
import traceback
import subprocess

from core.config import *

print(f"02. Importing {NAME} libraries")
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox
from gui.utils import styles
from core.user.environment import Composition
from core.exception_handler import report_unhandled_exception

sys.path.append("./Engine")
# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = report_unhandled_exception
print("03. Installed exception hook")


def launch_window():
    print(f"Revision {VERSION} {EDITION} edition [{TEAM} | {AUTHOR}]")
    QFontDatabase().addApplicationFont(r"font.ttf")

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

    styles.apply(app)
    app.setFont(QFont("나눔바른펜", 11))
    try:
        from gui.window import MainForm
        root = MainForm()
        # splash.finish(root)
        root.show()
        app.exec_()
    except Exception as e:
        atexit.register(report_unhandled_exception, traceback.format_exc())
        print(e)


def main():
    # TODO: unstable exit with unknown error with 0xC0000409:
    # see https://stackoverflow.com/questions/12827305/pyqt-application-close-with-error

    app.setWindowIcon(QIcon(r"gui\resources\icon.ico"
                            if os.path.isfile(r"gui\resources\icon.ico")
                            else r"icon.ico"))

    # if not os.path.isfile(os.environ['PYTHON']):
    # sys.exit("PYTHON NOT FOUND.")
    print("04. Detecting Python [", end=str())
    if RELEASE:
        if os.path.isfile(PREF_FILE):
            os.environ["PYTHON"] = json.loads(open(PREF_FILE).read())["python"]
        else:
            try:
                os.environ["PYTHON"] = "".join(list(subprocess.check_output("where python").decode("utf8"))[0:-2])
            except:
                pass
            Composition.launch()

            try:
                os.environ["PYTHON"]
            except KeyError:
                QMessageBox.information(None, f"{NAME} 실행 거부됨",
                                        f"{NAME} 실행에 필요한 필수 구성이 완료되지 않았습니다.")
                sys.exit(-1)

            os.mkdir(TMP_PATH)
            with open(PREF_FILE, "w") as p:
                p.write(json.dumps({"python": os.environ["PYTHON"]}, indent=4))
    else:
        os.environ["PYTHON"] = "python"
    print(os.environ["PYTHON"] + "]")

    print("05. Checking dependency [", end=str())

    try:
        subprocess.check_output("python -c \"import pygame\"", shell=True) == b""
        print("Done]")
    except subprocess.CalledProcessError:
        print("ERROR]")
        print("  05-1. Installing pygame")
        subprocess.Popen([os.environ["PYTHON"], "-m", "pip", "install", "pygame"]).wait()

    print("06. Using plugins [", end=str())
    from core import config
    if os.path.isdir(PLUGIN_DIR):
        config.USE_PLUGINS = True

    # Disable plugins
    config.USE_PLUGINS = False
    print(f"{config.USE_PLUGINS}]")

    del config

    print(f"07. Running {NAME} on {sys.platform}")
    launch_window()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--use-white-theme", help="프로그램 색상을 흰색으로 변경합니다.", action="store_true")
    args = parser.parse_args()
    if args.use_white_theme:
        CONF["THEME"] = "WHITE"
    app = QApplication(sys.argv)
    app.setApplicationName(NAME)
    app.setApplicationVersion(VERSION)

    main()
    print("07. Terminating all process")
