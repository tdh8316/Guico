import os
import subprocess

from core.config import CONF


class Execute(object):

    def __init__(self):
        self.process = None

    def precess_start(self):
        self.process = subprocess.Popen(
            f"cd {os.path.dirname(CONF['SOURCE_PATH']) } "
            f"&& "
            f"{os.environ['PYTHON']} \"{CONF['SOURCE_PATH']}\"",
            shell=True,
            start_new_session=True,
            stdout=subprocess.PIPE)

    def is_process_running(self) -> bool:
        return (self.process.poll() is None
                if self.process is not None
                else False)


execute_manager = Execute()
