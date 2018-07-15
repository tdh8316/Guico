import sys

from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QApplication
import qdarkstyle

from gui.window import Editor
# from gui import theme

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase().addApplicationFont(r"gui\resources\NanumBarunpenR.ttf")
    QFontDatabase().addApplicationFont(r"gui\resources\GodoM.ttf")

    app.setStyleSheet(qdarkstyle.load_stylesheet())
    app.setFont(QFont("나눔바른펜", 11))
    app.setWindowIcon(QIcon(r"gui\resources\icon.ico"))

    root = Editor()
    root.show()

    sys.exit(app.exec_())
