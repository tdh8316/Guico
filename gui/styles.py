from os.path import join, dirname, abspath

from qtpy.QtGui import QPalette, QColor

_STYLESHEET = join(dirname(abspath(__file__)), 'style.css')
""" str: Main stylesheet. """


def _apply_base_theme(app):
    """ Apply base theme to the application.

        Args:
            app (QApplication): QApplication instance.
    """
    app.setStyle('Fusion')

    with open(_STYLESHEET) as stylesheet:
        app.setStyleSheet(stylesheet.read())


def dark(app):
    """ Apply Dark Theme to the Qt application instance.

        Args:
            app (QApplication): QApplication instance.
    """

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
