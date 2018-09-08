import logging

from pyqode.python.widgets import PyCodeEdit

logging.basicConfig(level=logging.ERROR)

from pyqode.python.backend import server

from core.config import NAME

logging.basicConfig()


class SpriteScriptEditor(PyCodeEdit):

    def __init__(self, parent=None, *args):
        super(SpriteScriptEditor, self).__init__(parent)
        self.backend.start(server.__file__)

        self.setWindowTitle(f"{NAME} plugin::{self.__class__.__name__}")

        print(*args)


# if __name__ != "__main__":
# SpriteScriptEditor().show()

def main(parent, *args) -> SpriteScriptEditor:
    return SpriteScriptEditor(parent, *args)
