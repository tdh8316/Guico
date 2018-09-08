import logging

from pyqode.python.widgets import PyCodeEdit

logging.basicConfig(level=logging.ERROR)

from pyqode.python.backend import server

from core.config import *

logging.basicConfig()


class SpriteScriptEditor(PyCodeEdit):

    def __init__(self, parent=None):
        super(SpriteScriptEditor, self).__init__(parent)
        self.backend.start(server.__file__)

        self.setWindowTitle(f"{NAME} {self.__class__.__name__}")

    def showEvent(self, event):
        self.setWindowTitle(f"{NAME} {self.__class__.__name__} - {CONF['FILE_PATH']} [{CONF['CLASS_PATH']}]")
        super().showEvent(event)

    def focusOutEvent(self, event):
        print(self.__class__.__name__, "lost focus.")
        super().focusOutEvent(event)