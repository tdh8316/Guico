from core.config import *
from build_tools.packager.python_environment import MakePyEnv


def packaging_windows(bsd):
    print(f"{CONF['SOURCE_PATH']} 에 대한 패키징 시작...")
    MakePyEnv(basedir=bsd)
