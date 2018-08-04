import shutil
import platform

from os import environ, path


class MakePyEnv:

    def __init__(self, basedir, os=platform.system()):
        self.base_dir = basedir
        if os == "Windows":
            self.make_win()
        elif os == "Linux":
            self.make_linux()

    def make_win(self):
        shutil.copytree(environ["PYTHON"], path.join(self.base_dir, "python"))

    def make_linux(self):
        pass
