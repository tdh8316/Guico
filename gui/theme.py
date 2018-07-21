def load() -> str():
    return """
    QsciScintilla#editor {
                         border: none;
                         border-top: 2px solid #007ACC;
                 }

                QToolButton {
                    background: transparent;
                    border-radius: 0px;
                    padding: 1px;
                    border: none;
                }

                QToolButton:hover {
                    background: white;
                }

                QToolButton:pressed {
                    background: #007ACC;
                }

                QToolButton:checked {
                    background: #007ACC;
                }

                QToolButton:disabled {
                    background: transparent;
                }

                 QToolButton::menu-button {
                     color: black;
                 }

             QGroupBox {
                 background-color: none;
                 border: none;
                 font: bold;
                 border-radius: 0px;
                 margin-top: 5ex; /* leave space at the top for the title */
             }

             QGroupBox::title {
                 padding-left: 8px;
                 subcontrol-origin: margin;
                 subcontrol-position: top left; /* position at the top left */
                 background-color: none;
             }

             QComboBox {
                 color: #003366;
                 border-top: transparent;
                 border-right: transparent;
                 border-left: transparent;
                 border-bottom: 1px solid #007ACC;
                 border-radius: 0px;
                 padding: 2px 2px 2px 3px;
             }

             QComboBox:disabled {
                 color: gray;
             }

             QComboBox:editable {
                 background: white;
             }

             QComboBox:!editable, QComboBox::drop-down:editable {
                  background: lightgrey;
                  border-radius: 0px;
             }

             /* QComboBox gets the "on" state when the popup is open */
             QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                 background: darkgray;
             }

             QComboBox:on { /* shift the text when the popup opens */
             
             }

             QComboBox::drop-down {
                 subcontrol-origin: padding;
                 subcontrol-position: top right;
                 width: 15px;
                 border: none;
             }

             QComboBox::down-arrow {
                 image: url(Resources/style/images/downarrow.png);
             }

             QComboBox::down-arrow:on { /* shift the arrow when popup is open */
                 top: 1px;
                 left: 0px;
             }

             QComboBox QAbstractItemView {
                 border: 1px solid lightgray;
                 selection-background-color: #2B2BFF;
             }

             QComboBox QAbstractItemView::item {
                 min-height: 25px;
             }

        QTabWidget::pane { /* The tab widget frame */
             border-top: none;
        }

        QTabWidget#settingsTab::pane { /* The tab widget frame */
             border-top: 1px solid #007ACC;
             position: absolute;
        }

        QTabWidget::pane#buildTab { /* The tab widget frame */
             border-top: 2px solid #007ACC;
        }

        QTabWidget::pane#sideBottomTab { /* The tab widget frame */
             border-top: 2px solid #007ACC;
        }

        QTabWidget::tab-bar {
             left: 0px; /* move to the right by 0px */
        }

        QTabWidget#sideBottomTab::tab-bar {
             left: 0px; /* move to the right by 0px */
        }

        QTabWidget#settingsTab::tab-bar {
             left: 10px; /* move to the right by 0px */
        }

        /* Style the tab using the tab sub-control. Note that
             it reads QTabBar _not_ QTabWidget */
        QTabBar::tab {
             background: none;
             border: none;
             min-width: 24ex;
             min-height: 5ex;
             padding: 2px;
             padding-left: 5px;
             padding-right: 5px;
        }

        QTabBar::tab:hover {
             background: #70A7DC;
             color: black;
        }

        QTabBar::tab:selected{
             background: #007ACC;
             color: white;
        }

        QTabBar::tab:!selected {
             margin-top: 0px; /* make non-selected tabs look smaller */
        }

        QTabBar::tab:first {
             border-left: none;
         }

        QTabBar::tab:only-one {
             border-left: none;
        }

        QTabBar::tear {
             image: url(Resources/style/images/tear.png);
        }

        QTabBar::scroller { /* the width of the scroll buttons */
             width: 20px;
        }

        QTabBar QToolButton { /* the scroll buttons are tool buttons */
             border-image: url(Resources/style/images/scrollbutton.png) 2;

        }

        QTabBar QToolButton::right-arrow { /* the arrow mark in the tool buttons */
             image: url(Resources/style/images/Arrow Right.png);
        }

        QTabBar QToolButton::left-arrow {
             image: url(Resources/style/images/Arrow Left.png);
        }


        QTabBar::close-button {
             image: url(Resources/style/images/close1.png)

         }

        QTabBar::close-button:hover {
             image: url(Resources/style/images/close-hover.png)
        }

        QTabBar::close-button:pressed {
             image: url(Resources/style/images/close-pressed.png)
        }

        QToolBar {
            border: none;
            background-color: transparent;
        }

        QToolBar QToolButton {
            border: 1px solid transparent;
            background: transparent;
            padding: 1px;
        }

        QToolBar QToolButton:hover:enabled { /* when selected using mouse or keyboard */
             background-color: white;
        }

        QToolBar QToolButton:pressed:enabled {
             background-color: #007ACC;
        }

        QToolBar QToolButton:disabled {
             background-color: transparent;
        }

        QToolBar QToolButton:checked {
             background-color: #007ACC;
        }

        QStatusBar {
             background: transparent;
        }

        QStatusBar::item {
             border-radius: 3px;
        }

        QToolTip {
             color: white;
             border: none;
             opacity: 200;
             border-radius: 3px;
             background: #333333;
        }

        QMenuBar {
             background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                           stop:0 lightgray, stop:1 darkgray);
        }

        QMenuBar {
             background-color: #F0F0F0;
             
        }

        QMenuBar::item {
             spacing: 3px; /* spacing between menu bar items */
             padding: 3px 8px;
             background: none;
             border-radius: 0px;
        }

        QMenuBar::item:selected { /* when selected using mouse or keyboard */
             background: rgba(255, 0, 0, 80);
        }

        QMenuBar::item:pressed {
             background: rgba(255, 0, 0, 80);
        }

        QMenu {
             background: #E6E6E6;
             padding: 2px;
        }

        QMenu::item {
             padding: 5px 30px 5px 30px;
             border: none;
        }

        QMenu::item:selected:enabled {
             border-color: none;
             background: #FAFAFA;
        }

        QMenu::separator {
             height: 1px;
             background-color: lightgrey;
        }

        QMenu::indicator {
             width: 13px;
             height: 13px;
        }

        QListView {
             show-decoration-selected: 1; /* make the selection span the entire width of the view */
        }

        QListView::item:selected:!active {
             color: black;
             border: 1px solid white;
             background: lightgray;
        }

        QListView::item:selected:active {
             color: white;
             background: #337BFF;
        }

         QHeaderView::section {
             background: none;
             color: black;
             padding-left: 2px;
             border: none;
             border-bottom: 1px solid lightgray;
             height: 20px;
         }

         QHeaderView::section:checked
         {
             background-color: red;
         }

         /* style the sort indicator */
         QHeaderView::down-arrow {
             image: url(Resources/style/images/downarrow.png);
         }

         QHeaderView::up-arrow {
             image: url(Resources/style/images/uparrow.png);
         }


        QTreeView {
             show-decoration-selected: 1; /* make the selection span the entire width of the view */
             background: #E6E6E6;
             border: none;
        }

        QTreeView#sidebarItem {
             border: none;
             show-decoration-selected: 1; /* make the selection span the entire width of the view */
             background: #E6E6E6;
        }

        QTreeView::item:selected:!active {
             font: bold 20px;
             color: black;
             background: lightgrey;}

        QTreeView::item:selected:active {
             font: bold 20px;
             color: white;
             background: grey;
        }

        QTreeView::item:hover {
             border: none;
             background: #CCCCCC;
        }

        QSlider::groove:horizontal {
             border: 1px inset #999999;
             height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
             background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                 stop:0 #B3B3B3, stop:1 #FFFFFF);
             margin: 2px 7px 0 7px;
             border-radius: 5px;
        }

        QSlider::handle:horizontal {
             background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                                 stop:0 #D2D2D2, stop:1 #C3C3C3);
             border: 1px solid #5c5c5c;
             width: 18px;
             margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
             border-radius: 3px;
        }

        QScrollBar:vertical{
            padding-left: 0px;
            padding-right: 1px;
            border-left-width: 1px;
            background: #f1f1f1;
            width: 12px;
        }

        QScrollBar:horizontal{
            padding-top: 0px;
            padding-bottom: 1px;
            border-top-width: 1px;
            border-style:solid;
            border: none;
            background: #E7E7E7;
            height: 10px;
        }

        QScrollBar::handle:vertical{
            margin-top: 15px;
            margin-bottom: 15px;
            background: #B2B8BE;
            border-radius: 0px;
            border: 1px solid #FFFFFF;
            min-height: 30px;
        }

        QScrollBar::handle:horizontal{
            margin-left: 15px;
            margin-right: 15px;
            background: #B2B8BE;
            border-radius: 0px;
            border: none;
            min-width: 30px;
        }

        QScrollBar::handle:hover{
            background: #6F767D;
        }

        QScrollBar::handle:pressed{
            background: #141414;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical,
        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical,
        QScrollBar::add-line:horizontal,
        QScrollBar::sub-line:horizontal,
        QScrollBar::add-page:horizontal,
        QScrollBar::sub-page:horizontal{
            background: none;
            border: none;
        }
        
        QScrollBar::add-line:vertical:pressed,
        QScrollBar::sub-line:vertical:pressed,
        QScrollBar::add-page:vertical:pressed,
        QScrollBar::sub-page:vertical:pressed,
        QScrollBar::add-line:horizontal:pressed,
        QScrollBar::sub-line:horizontal:pressed,
        QScrollBar::add-page:horizontal:pressed,
        QScrollBar::sub-page:horizontal:pressed{
            background: lightgrey;
            border: none;
        }

        QScrollBar::up-arrow:vertical {
          border: none;
          width: 10px;
          height: 10px;
          margin-left: 0px;
          image: url(Resources/style/images/uparrow.png);
        }

        QScrollBar::down-arrow:vertical {
          border: none;
          width: 10px;
          height: 10px;
          margin-left: 0px;
          image: url(Resources/style/images/downarrow.png);
        }

        QScrollBar::left-arrow:horizontal {
          border: none;
          width: 10px;
          height: 10px;
          image: url(Resources/style/images/leftarrow.png);
        }

        QScrollBar::right-arrow:horizontal {
          border: none;
          width: 10px;
          height: 10px;
          image: url(Resources/style/images/rightarrow.png);
        }

        QPushButton {
            min-width: 70px;
            min-height: 20px;
            color: black;
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #F1F1F1, stop: 1 #DFDFDF);
            border-radius: 2px;
            border: 1px solid #A8A8A8;
        }

        QPushButton:hover {
            border: 1px solid #AAAAAA;
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #F1F1F1, stop: 1 #F0F0F0);
        }

        QPushButton:pressed {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #D7D7D7, stop: 1 #BDBDBD);
            padding-top: 2px;
            border: 1px solid #A1A1A1;
        }

        QPushButton:checked {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #D7D7D7, stop: 1 #BDBDBD);
            padding-top: 2px;
            border: 1px solid #A1A1A1;
        }

        QPushButton:disabled {
            color: black;
            background: #FFFFFF;
        }

         QSplitter::handle {
             background: none;
         }

         QSplitter::handle:horizontal {
             width: 5px;
             background: #E6E6E6;
         }

         QSplitter::handle:vertical {
             height: 5px;
             background: lightgray;
         }

         QSplitter::handle:hover {
             background: lightgray;
         }

         QSplitter::handle:pressed {
             background: gray;
         }

         QLineEdit {
             border: 1px solid lightgrey;
             min-height: 20px;
             border-radius: 0px;
             padding: 0 4px;
             background: none;
         }

         QLineEdit:disabled {
             border: 1px solid lightgray;
         }
"""

def qdarkstyle_load() -> str():
    return """QToolTip {
    border: 1px solid #76797C;
    background-color: #5A7566;
    color: white;
    padding: 0px;                /*remove padding, for fix combobox tooltip.*/
    opacity: 200;
}

QWidget {
    color: #eff0f1;
    background-color: #31363b;
    selection-background-color: #3daee9;
    selection-color: #eff0f1;
    background-clip: border;
    border-image: none;
    border: 0px transparent black;
    outline: 0;
}

QWidget:item:hover {
    background-color: #18465d;
    color: #eff0f1;
}

QWidget:item:selected {
    background-color: #18465d;
}

QCheckBox {
    spacing: 5px;
    outline: none;
    color: #eff0f1;
    margin-bottom: 2px;
}

QCheckBox:disabled {
    color: #76797C;
}

QCheckBox::indicator,
QGroupBox::indicator {
    width: 18px;
    height: 18px;
}

QGroupBox::indicator {
    margin-left: 2px;
}

QCheckBox::indicator:unchecked,
QGroupBox::indicator:unchecked {
    image: url(:/qss_icons/rc/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:hover,
QCheckBox::indicator:unchecked:focus,
QCheckBox::indicator:unchecked:pressed,
QGroupBox::indicator:unchecked:hover,
QGroupBox::indicator:unchecked:focus,
QGroupBox::indicator:unchecked:pressed {
    border: none;
    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);
}

QCheckBox::indicator:checked,
QGroupBox::indicator:checked {
    image: url(:/qss_icons/rc/checkbox_checked.png);
}

QCheckBox::indicator:checked:hover,
QCheckBox::indicator:checked:focus,
QCheckBox::indicator:checked:pressed,
QGroupBox::indicator:checked:hover,
QGroupBox::indicator:checked:focus,
QGroupBox::indicator:checked:pressed {
    border: none;
    image: url(:/qss_icons/rc/checkbox_checked_focus.png);
}

QCheckBox::indicator:indeterminate {
    image: url(:/qss_icons/rc/checkbox_indeterminate.png);
}

QCheckBox::indicator:indeterminate:focus,
QCheckBox::indicator:indeterminate:hover,
QCheckBox::indicator:indeterminate:pressed {
    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);
}

QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled {
    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);
}

QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled {
    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);
}

QRadioButton {
    spacing: 5px;
    outline: none;
    color: #eff0f1;
    margin-bottom: 2px;
}

QRadioButton:disabled {
    color: #76797C;
}

QRadioButton::indicator {
    width: 21px;
    height: 21px;
}

QRadioButton::indicator:unchecked {
    image: url(:/qss_icons/rc/radio_unchecked.png);
}

QRadioButton::indicator:unchecked:hover,
QRadioButton::indicator:unchecked:focus,
QRadioButton::indicator:unchecked:pressed {
    border: none;
    outline: none;
    image: url(:/qss_icons/rc/radio_unchecked_focus.png);
}

QRadioButton::indicator:checked {
    border: none;
    outline: none;
    image: url(:/qss_icons/rc/radio_checked.png);
}

QRadioButton::indicator:checked:hover,
QRadioButton::indicator:checked:focus,
QRadioButton::indicator:checked:pressed {
    border: none;
    outline: none;
    image: url(:/qss_icons/rc/radio_checked_focus.png);
}

QRadioButton::indicator:checked:disabled {
    outline: none;
    image: url(:/qss_icons/rc/radio_checked_disabled.png);
}

QRadioButton::indicator:unchecked:disabled {
    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);
}

QMenuBar {
    background-color: #31363b;
    color: #eff0f1;
}

QMenuBar::item {
    background: transparent;
}

QMenuBar::item:selected {
    background: transparent;
    border: 1px solid #76797C;
}

QMenuBar::item:pressed {
    border: 1px solid #76797C;
    background-color: #3daee9;
    color: #eff0f1;
    margin-bottom: -1px;
    padding-bottom: 1px;
}

QMenu {
    border: 1px solid #76797C;
    color: #eff0f1;
    margin: 2px;
}

QMenu::icon {
    margin: 5px;
}

QMenu::item {
    padding: 5px 30px 5px 30px;
    border: 1px solid transparent;
    /* reserve space for selection border */
}

QMenu::item:selected {
    color: #eff0f1;
}

QMenu::separator {
    height: 2px;
    background: lightblue;
    margin-left: 10px;
    margin-right: 5px;
}

QMenu::indicator {
    width: 18px;
    height: 18px;
}


/* non-exclusive indicator = check box style indicator
   (see QActionGroup::setExclusive) */

QMenu::indicator:non-exclusive:unchecked {
    image: url(:/qss_icons/rc/checkbox_unchecked.png);
}

QMenu::indicator:non-exclusive:unchecked:selected {
    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);
}

QMenu::indicator:non-exclusive:checked {
    image: url(:/qss_icons/rc/checkbox_checked.png);
}

QMenu::indicator:non-exclusive:checked:selected {
    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);
}


/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */

QMenu::indicator:exclusive:unchecked {
    image: url(:/qss_icons/rc/radio_unchecked.png);
}

QMenu::indicator:exclusive:unchecked:selected {
    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);
}

QMenu::indicator:exclusive:checked {
    image: url(:/qss_icons/rc/radio_checked.png);
}

QMenu::indicator:exclusive:checked:selected {
    image: url(:/qss_icons/rc/radio_checked_disabled.png);
}

QMenu::right-arrow {
    margin: 5px;
    image: url(:/qss_icons/rc/right_arrow.png)
}

QWidget:disabled {
    color: #454545;
    background-color: #31363b;
}

QAbstractItemView {
    alternate-background-color: #31363b;
    color: #eff0f1;
    border: 1px solid #3A3939;
    border-radius: 2px;
}

QWidget:focus,
QMenuBar:focus {
    border: 1px solid #3daee9;
}

QTabWidget:focus,
QCheckBox:focus,
QRadioButton:focus,
QSlider:focus {
    border: none;
}

QLineEdit {
    background-color: #232629;
    padding: 5px;
    border-style: solid;
    border: 1px solid #76797C;
    border-radius: 2px;
    color: #eff0f1;
}

QAbstractItemView QLineEdit {
    padding: 0;
}

QGroupBox {
    border: 1px solid #76797C;
    border-radius: 2px;
    margin-top: 20px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 10px;
}

QAbstractScrollArea {
    border-radius: 2px;
    border: 1px solid #76797C;
    background-color: transparent;
}

QScrollBar:horizontal {
    height: 15px;
    margin: 3px 15px 3px 15px;
    border: 1px transparent #2A2929;
    border-radius: 4px;
    background-color: #2A2929;
}

QScrollBar::handle:horizontal {
    background-color: #605F5F;
    min-width: 5px;
    border-radius: 4px;
}

QScrollBar::add-line:horizontal {
    margin: 0px 3px 0px 3px;
    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
    width: 10px;
    height: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
    margin: 0px 3px 0px 3px;
    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,
QScrollBar::add-line:horizontal:on {
    border-image: url(:/qss_icons/rc/right_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal:hover,
QScrollBar::sub-line:horizontal:on {
    border-image: url(:/qss_icons/rc/left_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal,
QScrollBar::down-arrow:horizontal {
    background: none;
}

QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {
    background: none;
}

QScrollBar:vertical {
    background-color: #2A2929;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border: 1px transparent #2A2929;
    border-radius: 4px;
}

QScrollBar::handle:vertical {
    background-color: #605F5F;
    min-height: 5px;
    border-radius: 4px;
}

QScrollBar::sub-line:vertical {
    margin: 3px 0px 3px 0px;
    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical {
    margin: 3px 0px 3px 0px;
    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,
QScrollBar::sub-line:vertical:on {
    border-image: url(:/qss_icons/rc/up_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical:hover,
QScrollBar::add-line:vertical:on {
    border-image: url(:/qss_icons/rc/down_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical,
QScrollBar::down-arrow:vertical {
    background: none;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: none;
}

QTextEdit {
    background-color: #232629;
    color: #eff0f1;
    border: 1px solid #76797C;
}

QPlainTextEdit {
    background-color: #232629;
    ;
    color: #eff0f1;
    border-radius: 2px;
    border: 1px solid #76797C;
}

QHeaderView::section {
    background-color: #76797C;
    color: #eff0f1;
    padding: 5px;
    border: 1px solid #76797C;
}

QSizeGrip {
    image: url(:/qss_icons/rc/sizegrip.png);
    width: 12px;
    height: 12px;
}

QMainWindow::separator {
    background-color: #31363b;
    color: white;
    padding-left: 4px;
    spacing: 2px;
    border: 1px dashed #76797C;
}

QMainWindow::separator:hover {
    background-color: #787876;
    color: white;
    padding-left: 4px;
    border: 1px solid #76797C;
    spacing: 2px;
}

QMenu::separator {
    height: 1px;
    background-color: #76797C;
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}

QFrame {
    border-radius: 2px;
    border: 1px solid #76797C;
}

QFrame[frameShape="0"] {
    border-radius: 2px;
    border: 1px transparent #76797C;
}

QStackedWidget {
    border: 1px transparent black;
}

QToolBar {
    border: 1px transparent #393838;
    background: 1px solid #31363b;
    font-weight: bold;
}

QToolBar::handle:horizontal {
    image: url(:/qss_icons/rc/Hmovetoolbar.png);
}

QToolBar::handle:vertical {
    image: url(:/qss_icons/rc/Vmovetoolbar.png);
}

QToolBar::separator:horizontal {
    image: url(:/qss_icons/rc/Hsepartoolbar.png);
}

QToolBar::separator:vertical {
    image: url(:/qss_icons/rc/Vsepartoolbar.png);
}

QToolButton#qt_toolbar_ext_button {
    background: #58595a
}

QPushButton {
    color: #eff0f1;
    background-color: #31363b;
    border-width: 1px;
    border-color: #76797C;
    border-style: solid;
    padding: 5px;
    border-radius: 2px;
    outline: none;
}

QPushButton:disabled {
    background-color: #31363b;
    border-width: 1px;
    border-color: #454545;
    border-style: solid;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 2px;
    color: #454545;
}

QPushButton:focus {
    background-color: #3daee9;
    color: white;
}

QPushButton:pressed {
    background-color: #3daee9;
    padding-top: -15px;
    padding-bottom: -17px;
}

QComboBox {
    selection-background-color: #3daee9;
    border-style: solid;
    border: 1px solid #76797C;
    border-radius: 2px;
    padding: 5px;
    min-width: 75px;
}

QPushButton:checked {
    background-color: #76797C;
    border-color: #6A6969;
}

QComboBox:hover,
QPushButton:hover,
QAbstractSpinBox:hover,
QLineEdit:hover,
QTextEdit:hover,
QPlainTextEdit:hover,
QAbstractView:hover,
QTreeView:hover {
    border: 1px solid #3daee9;
    color: #eff0f1;
}

QComboBox:on {
    padding-top: 3px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}

QComboBox QAbstractItemView {
    background-color: #232629;
    border-radius: 2px;
    border: 1px solid #76797C;
    selection-background-color: #18465d;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    image: url(:/qss_icons/rc/down_arrow_disabled.png);
}

QComboBox::down-arrow:on,
QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus {
    image: url(:/qss_icons/rc/down_arrow.png);
}

QAbstractSpinBox {
    padding: 5px;
    border: 1px solid #76797C;
    background-color: #232629;
    color: #eff0f1;
    border-radius: 2px;
    min-width: 75px;
}

QAbstractSpinBox:up-button {
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center right;
}

QAbstractSpinBox:down-button {
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center left;
}

QAbstractSpinBox::up-arrow,
QAbstractSpinBox::up-arrow:disabled,
QAbstractSpinBox::up-arrow:off {
    image: url(:/qss_icons/rc/up_arrow_disabled.png);
    width: 10px;
    height: 10px;
}

QAbstractSpinBox::up-arrow:hover {
    image: url(:/qss_icons/rc/up_arrow.png);
}

QAbstractSpinBox::down-arrow,
QAbstractSpinBox::down-arrow:disabled,
QAbstractSpinBox::down-arrow:off {
    image: url(:/qss_icons/rc/down_arrow_disabled.png);
    width: 10px;
    height: 10px;
}

QAbstractSpinBox::down-arrow:hover {
    image: url(:/qss_icons/rc/down_arrow.png);
}

QLabel {
    border: 0px solid black;
}

QTabWidget {
    border: 0px transparent black;
}

QTabWidget::pane {
    border: 1px solid #76797C;
    padding: 5px;
    margin: 0px;
}

QTabWidget::tab-bar {
    /* left: 5px; move to the right by 5px */
}

QTabBar {
    qproperty-drawBase: 0;
    border-radius: 3px;
}

QTabBar:focus {
    border: 0px transparent black;
}

QTabBar::close-button {
    image: url(:/qss_icons/rc/close.png);
    background: transparent;
}

QTabBar::close-button:hover {
    image: url(:/qss_icons/rc/close-hover.png);
    background: transparent;
}

QTabBar::close-button:pressed {
    image: url(:/qss_icons/rc/close-pressed.png);
    background: transparent;
}


/* TOP TABS */

QTabBar::tab:top {
    color: #eff0f1;
    border: 1px solid #76797C;
    border-bottom: 1px transparent black;
    background-color: #31363b;
    padding: 5px;
    min-width: 50px;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
}

QTabBar::tab:top:selected {
    color: #eff0f1;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-bottom: 2px solid #3daee9;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
}

QTabBar::tab:top:!selected:hover {
    background-color: #3daee9;
}


/* BOTTOM TABS */

QTabBar::tab:bottom {
    color: #eff0f1;
    border: 1px solid #76797C;
    border-top: 1px transparent black;
    background-color: #31363b;
    padding: 5px;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
    min-width: 50px;
}

QTabBar::tab:bottom:selected {
    color: #eff0f1;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-top: 2px solid #3daee9;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
}

QTabBar::tab:bottom:!selected:hover {
    background-color: #3daee9;
}


/* LEFT TABS */

QTabBar::tab:left {
    color: #eff0f1;
    border: 1px solid #76797C;
    border-left: 1px transparent black;
    background-color: #31363b;
    padding: 5px;
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
    min-height: 50px;
}

QTabBar::tab:left:selected {
    color: #eff0f1;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-left: 2px solid #3daee9;
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
}

QTabBar::tab:left:!selected:hover {
    background-color: #3daee9;
}


/* RIGHT TABS */

QTabBar::tab:right {
    color: #eff0f1;
    border: 1px solid #76797C;
    border-right: 1px transparent black;
    background-color: #31363b;
    padding: 5px;
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
    min-height: 50px;
}

QTabBar::tab:right:selected {
    color: #eff0f1;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-right: 2px solid #3daee9;
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
}

QTabBar::tab:right:!selected:hover {
    background-color: #3daee9;
}

QTabBar QToolButton::right-arrow:enabled {
    image: url(:/qss_icons/rc/right_arrow.png);
}

QTabBar QToolButton::left-arrow:enabled {
    image: url(:/qss_icons/rc/left_arrow.png);
}

QTabBar QToolButton::right-arrow:disabled {
    image: url(:/qss_icons/rc/right_arrow_disabled.png);
}

QTabBar QToolButton::left-arrow:disabled {
    image: url(:/qss_icons/rc/left_arrow_disabled.png);
}

QDockWidget {
    background: #31363b;
    border: 1px solid #403F3F;
    titlebar-close-icon: url(:/qss_icons/rc/close.png);
    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);
}

QDockWidget::close-button,
QDockWidget::float-button {
    border: 1px solid transparent;
    border-radius: 2px;
    background: transparent;
}

QDockWidget::close-button:hover,
QDockWidget::float-button:hover {
    background: rgba(255, 255, 255, 10);
}

QDockWidget::close-button:pressed,
QDockWidget::float-button:pressed {
    padding: 1px -1px -1px 1px;
    background: rgba(255, 255, 255, 10);
}

QTreeView,
QListView {
    border: 1px solid #76797C;
    background-color: #232629;
}

QTreeView:branch:selected,
QTreeView:branch:hover {
    background: url(:/qss_icons/rc/transparent.png);
}

QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(:/qss_icons/rc/transparent.png);
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(:/qss_icons/rc/transparent.png);
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(:/qss_icons/rc/transparent.png);
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    image: url(:/qss_icons/rc/branch_closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
    image: url(:/qss_icons/rc/branch_open.png);
}

QTreeView::branch:has-children:!has-siblings:closed:hover,
QTreeView::branch:closed:has-children:has-siblings:hover {
    image: url(:/qss_icons/rc/branch_closed-on.png);
}

QTreeView::branch:open:has-children:!has-siblings:hover,
QTreeView::branch:open:has-children:has-siblings:hover {
    image: url(:/qss_icons/rc/branch_open-on.png);
}

QListView::item:!selected:hover,
QTreeView::item:!selected:hover {
    background: #18465d;
    outline: 0;
    color: #eff0f1
}

QListView::item:selected:hover,
QTreeView::item:selected:hover {
    background: #287399;
    color: #eff0f1;
}

QTreeView::indicator:checked,
QListView::indicator:checked {
    image: url(:/qss_icons/rc/checkbox_checked.png);
}

QTreeView::indicator:unchecked,
QListView::indicator:unchecked {
    image: url(:/qss_icons/rc/checkbox_unchecked.png);
}

QTreeView::indicator:indeterminate,
QListView::indicator:indeterminate {
    image: url(:/qss_icons/rc/checkbox_indeterminate.png);
}

QTreeView::indicator:checked:hover,
QTreeView::indicator:checked:focus,
QTreeView::indicator:checked:pressed,
QListView::indicator:checked:hover,
QListView::indicator:checked:focus,
QListView::indicator:checked:pressed {
    image: url(:/qss_icons/rc/checkbox_checked_focus.png);
}

QTreeView::indicator:unchecked:hover,
QTreeView::indicator:unchecked:focus,
QTreeView::indicator:unchecked:pressed,
QListView::indicator:unchecked:hover,
QListView::indicator:unchecked:focus,
QListView::indicator:unchecked:pressed {
    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);
}

QTreeView::indicator:indeterminate:hover,
QTreeView::indicator:indeterminate:focus,
QTreeView::indicator:indeterminate:pressed,
QListView::indicator:indeterminate:hover,
QListView::indicator:indeterminate:focus,
QListView::indicator:indeterminate:pressed {
    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);
}

QSlider::groove:horizontal {
    border: 1px solid #565a5e;
    height: 4px;
    background: #565a5e;
    margin: 0px;
    border-radius: 2px;
}

QSlider::handle:horizontal {
    background: #232629;
    border: 1px solid #565a5e;
    width: 16px;
    height: 16px;
    margin: -8px 0;
    border-radius: 9px;
}

QSlider::groove:vertical {
    border: 1px solid #565a5e;
    width: 4px;
    background: #565a5e;
    margin: 0px;
    border-radius: 3px;
}

QSlider::handle:vertical {
    background: #232629;
    border: 1px solid #565a5e;
    width: 16px;
    height: 16px;
    margin: 0 -8px;
    border-radius: 9px;
}

QToolButton {
    background-color: transparent;
    border: 1px transparent #76797C;
    border-radius: 2px;
    margin: 3px;
    padding: 5px;
}

QToolButton[popupMode="1"] {
    /* only for MenuButtonPopup */
    padding-right: 20px;
    /* make way for the popup button */
    border: 1px #76797C;
    border-radius: 5px;
}

QToolButton[popupMode="2"] {
    /* only for InstantPopup */
    padding-right: 10px;
    /* make way for the popup button */
    border: 1px #76797C;
}

QToolButton:hover,
QToolButton::menu-button:hover {
    background-color: transparent;
    border: 1px solid #3daee9;
    padding: 5px;
}

QToolButton:checked,
QToolButton:pressed,
QToolButton::menu-button:pressed {
    background-color: #3daee9;
    border: 1px solid #3daee9;
    padding: 5px;
}


/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */

QToolButton::menu-indicator {
    image: url(:/qss_icons/rc/down_arrow.png);
    top: -7px;
    left: -2px;
    /* shift it a bit */
}


/* the subcontrols below are used only in the MenuButtonPopup mode */

QToolButton::menu-button {
    border: 1px transparent #76797C;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* 16px width + 4px for border = 20px allocated above */
    width: 16px;
    outline: none;
}

QToolButton::menu-arrow {
    image: url(:/qss_icons/rc/down_arrow.png);
}

QToolButton::menu-arrow:open {
    border: 1px solid #76797C;
}

QPushButton::menu-indicator {
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    left: 8px;
}

QTableView {
    border: 1px solid #76797C;
    gridline-color: #31363b;
    background-color: #232629;
}

QTableView,
QHeaderView {
    border-radius: 0px;
}

QTableView::item:pressed,
QListView::item:pressed,
QTreeView::item:pressed {
    background: #18465d;
    color: #eff0f1;
}

QTableView::item:selected:active,
QTreeView::item:selected:active,
QListView::item:selected:active {
    background: #287399;
    color: #eff0f1;
}

QHeaderView {
    background-color: #31363b;
    border: 1px transparent;
    border-radius: 0px;
    margin: 0px;
    padding: 0px;
}

QHeaderView::section {
    background-color: #31363b;
    color: #eff0f1;
    padding: 5px;
    border: 1px solid #76797C;
    border-radius: 0px;
    text-align: center;
}

QHeaderView::section::vertical::first,
QHeaderView::section::vertical::only-one {
    border-top: 1px solid #76797C;
}

QHeaderView::section::vertical {
    border-top: transparent;
}

QHeaderView::section::horizontal::first,
QHeaderView::section::horizontal::only-one {
    border-left: 1px solid #76797C;
}

QHeaderView::section::horizontal {
    border-left: transparent;
}

QHeaderView::section:checked {
    color: white;
    background-color: #334e5e;
}


/* style the sort indicator */

QHeaderView::down-arrow {
    image: url(:/qss_icons/rc/down_arrow.png);
}

QHeaderView::up-arrow {
    image: url(:/qss_icons/rc/up_arrow.png);
}

QTableCornerButton::section {
    background-color: #31363b;
    border: 1px transparent #76797C;
    border-radius: 0px;
}

QToolBox {
    padding: 5px;
    border: 1px transparent black;
}

QToolBox::tab {
    color: #eff0f1;
    background-color: #31363b;
    border: 1px solid #76797C;
    border-bottom: 1px transparent #31363b;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QToolBox::tab:selected {
    /* italicize selected tabs */
    font: italic;
    background-color: #31363b;
    border-color: #3daee9;
}

QStatusBar::item {
    border: 0px transparent dark;
}

QFrame[height="3"],
QFrame[width="3"] {
    background-color: #76797C;
}

QSplitter::handle {
    border: 1px dashed #76797C;
}

QSplitter::handle:hover {
    background-color: #787876;
    border: 1px solid #76797C;
}

QSplitter::handle:horizontal {
    width: 1px;
}

QSplitter::handle:vertical {
    height: 1px;
}

QProgressBar {
    border: 1px solid #76797C;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #05B8CC;
}

QDateEdit {
    selection-background-color: #3daee9;
    border-style: solid;
    border: 1px solid #3375A3;
    border-radius: 2px;
    padding: 1px;
    min-width: 75px;
}

QDateEdit:on {
    padding-top: 3px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}

QDateEdit QAbstractItemView {
    background-color: #232629;
    border-radius: 2px;
    border: 1px solid #3375A3;
    selection-background-color: #3daee9;
}

QDateEdit::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QDateEdit::down-arrow {
    image: url(:/qss_icons/rc/down_arrow_disabled.png);
}

QDateEdit::down-arrow:on,
QDateEdit::down-arrow:hover,
QDateEdit::down-arrow:focus {
    image: url(:/qss_icons/rc/down_arrow.png);
}
"""