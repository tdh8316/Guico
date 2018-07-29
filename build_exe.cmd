@ECHO OFF

pyinstaller bootstrap.py -F  -i gui\resource\icon.ico -w --hidden-import PyQt5.sip
pause
