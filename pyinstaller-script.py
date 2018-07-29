#!c:\python36\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PyInstaller==3.3.1','console_scripts','pyinstaller'
__requires__ = 'PyInstaller==3.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PyInstaller==3.3.1', 'console_scripts', 'pyinstaller')()
    )
