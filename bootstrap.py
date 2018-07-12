import sys
from PyQt5.QtWidgets import QApplication

from gui.window import Editor


if __name__ == "__main__":
    app = QApplication(sys.argv)

    root = Editor()
    root.show()

    sys.exit(app.exec_())
