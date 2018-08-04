import shutil
import platform

from os import environ, path

from core.config import CONF


class MakePyEnv:

    def __init__(self, basedir, os=platform.system()):
        self.base_dir = basedir
        if os == "Windows":
            self.make_win()
        elif os == "Linux":
            self.make_linux()

    def make_win(self):
        shutil.copytree("/".join(environ["PYTHON"].split("\\")[0:-1]), path.join(self.base_dir, "Binaries"))
        shutil.copy(CONF["SOURCE_PATH"], path.join(self.base_dir, "Binaries",
                                                   CONF["SOURCE_PATH"].split("\\")[-1].split(".")[0]))

    def make_linux(self):
        pass
