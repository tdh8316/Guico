import sys

import qdarkstyle
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QApplication

from core.code.executer import interpreter
from gui.window import Editor as MainWindow


if __name__ == "__main__":
    app = QApplication([])
    QFontDatabase().addApplicationFont(r"gui\resources\NanumBarunpenR.ttf")
    QFontDatabase().addApplicationFont(r"gui\resources\godoRounded L.ttf")

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setFont(QFont("나눔바른펜", 11))
    app.setWindowIcon(QIcon(r"gui\resources\icon.ico"))

    root = MainWindow()
    root.show()

    sys.exit(app.exec_())
