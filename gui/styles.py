from os.path import join, dirname, abspath

from PyQt5.QtGui import QPalette, QColor

from core.config import *


def _apply_base_theme(app):
    app.setStyle('Fusion')

    with open(_STYLESHEET) as stylesheet:
        app.setStyleSheet(stylesheet.read())


def apply(app):
    global _STYLESHEET
    if CONF["THEME"] == "WHITE":
        _STYLESHEET = join(dirname(abspath(__file__)), 'white.css')
        white(app)
    else:
        _STYLESHEET = join(dirname(abspath(__file__)), 'dark.css')
        dark(app)


def dark(app):
    _apply_base_theme(app)

    darkPalette = QPalette()

    # base
    darkPalette.setColor(QPalette.WindowText, QColor(241, 241, 241))
    darkPalette.setColor(QPalette.Button, QColor(45, 45, 48))
    darkPalette.setColor(QPalette.Light, QColor(180, 180, 180))
    darkPalette.setColor(QPalette.Midlight, QColor(90, 90, 90))
    darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
    darkPalette.setColor(QPalette.Text, QColor(241, 241, 241))
    darkPalette.setColor(QPalette.BrightText, QColor(241, 241, 241))
    darkPalette.setColor(QPalette.ButtonText, QColor(241, 241, 241))
    darkPalette.setColor(QPalette.Base, QColor(27, 27, 28))
    darkPalette.setColor(QPalette.Window, QColor(37, 37, 38))
    darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
    darkPalette.setColor(QPalette.Highlight, QColor(51, 51, 52))
    darkPalette.setColor(QPalette.HighlightedText, QColor(241, 241, 241))
    darkPalette.setColor(QPalette.Link, QColor(56, 252, 196))
    darkPalette.setColor(QPalette.AlternateBase, QColor(37, 37, 38))
    darkPalette.setColor(QPalette.ToolTipBase, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.ToolTipText, QColor(180, 180, 180))

    # disabled
    darkPalette.setColor(QPalette.Disabled, QPalette.WindowText,
                         QColor(127, 127, 127))
    darkPalette.setColor(QPalette.Disabled, QPalette.Text,
                         QColor(127, 127, 127))
    darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                         QColor(127, 127, 127))
    darkPalette.setColor(QPalette.Disabled, QPalette.Highlight,
                         QColor(80, 80, 80))
    darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                         QColor(127, 127, 127))

    app.setPalette(darkPalette)


def white(app):
    _apply_base_theme(app)

    whitePalette = QPalette()

    # base
    whitePalette.setColor(QPalette.WindowText, QColor(0, 0, 0))
    whitePalette.setColor(QPalette.Button, QColor(255, 255, 255))
    whitePalette.setColor(QPalette.Light, QColor(180, 180, 180))
    whitePalette.setColor(QPalette.Midlight, QColor(41, 57, 86))
    whitePalette.setColor(QPalette.Dark, QColor(241, 241, 241))
    whitePalette.setColor(QPalette.Text, QColor(0, 0, 0))
    whitePalette.setColor(QPalette.BrightText, QColor(0, 0, 0))
    whitePalette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
    whitePalette.setColor(QPalette.Base, QColor(245, 245, 245))
    whitePalette.setColor(QPalette.Window, QColor(238, 238, 242))
    whitePalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
    whitePalette.setColor(QPalette.Highlight, QColor(201, 222, 245))
    whitePalette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    whitePalette.setColor(QPalette.Link, QColor(56, 252, 196))
    whitePalette.setColor(QPalette.AlternateBase, QColor(255, 255, 255))
    whitePalette.setColor(QPalette.ToolTipBase, QColor(53, 53, 53))
    whitePalette.setColor(QPalette.ToolTipText, QColor(180, 180, 180))

    app.setPalette(whitePalette)
