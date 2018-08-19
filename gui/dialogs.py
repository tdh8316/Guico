from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# from gui.widgets.tree_combobox import TreeComboBox
# from contents.leaf_types import getLeafTypeModel
from gui.widgets.tree_selector import QBasedTreeSelector
# from gui.widgets.script_widget import TabScriptWidget
from gui.widgets.customized import VariableNameEdit
from core import script_variables
from core.config import *

parent = None


def initialize(_parent):
    global parent
    parent = _parent


class OpenSourceLicense(QDialog):

    def __init__(self, parent=None):
        super(OpenSourceLicense, self).__init__(parent)
        self.setWindowFlags(Qt.Popup)

        layout = QFormLayout(self)
        textbox = QPlainTextEdit()
        textbox.setPlainText(OPEN_SOURCE_LICENSE)
        textbox.setReadOnly(True)
        textbox.setFixedWidth(720)
        textbox.setFixedHeight(640)
        layout.addRow(textbox)

        self.setLayout(layout)
        self.show()


class ActivateKey(QDialog):

    def __init__(self, parent=None):
        super(ActivateKey, self).__init__(parent)

        self.setWindowTitle(f"{NAME} 테스터 인증 키 입력")

        layout = QFormLayout(self)
        _input = QLineEdit()
        # noinspection SpellCheckingInspection
        _input.setInputMask(">0000-0000-AAAA-AAAA;_")
        layout.addRow(_input)

        self.setLayout(layout)
        self.show()


class NewVariable(QDialog):

    def __init__(self, parent=None):
        super(NewVariable, self).__init__(parent)
        self.setWindowTitle(f"{NAME} - 새로운 변수")
        self.setFixedSize(320, 160)

        self.layout = QGridLayout()
        self.var_name = VariableNameEdit()
        self.var_value = QLineEdit()
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.create_widget()

    def create_widget(self):
        self.layout.addWidget(QLabel("변수 이름:"), 0, 0)
        self.layout.addWidget(self.var_name, 0, 1)
        self.layout.addWidget(QLabel("값:"), 1, 0)
        self.layout.addWidget(self.var_value, 1, 1)
        self.layout.addWidget(self.buttons, 2, 1)
        self.setLayout(self.layout)

    def reject(self):
        super().reject()

    def accept(self):
        script_variables.globals[self.var_name.text()] = self.var_value.text()
        parent.attribute_widget.buildVariablesGlobals(script_variables.globals)
        super().accept()

    @staticmethod
    def setattr(parent=None):
        _win = NewVariable(parent)
        _exec = _win.exec_()


class setLeafType(QDialog):

    def __init__(self, parent):
        global isDoubleClicked
        QDialog.__init__(self, parent)

        isDoubleClicked = False

        self.types = TabScriptWidget()
        self.setWindowTitle(f"{NAME} - 새 잎 만들기")
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(480, 240)

        self.base_layout = QFormLayout(self)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.create_widgets()

        self.vbox.addWidget(self.types)
        self.hbox.addWidget(self.buttons)

        self.base_layout.addRow(self.vbox)
        self.base_layout.addRow(self.hbox)

        self.setLayout(self.base_layout)

    def create_widgets(self):
        # self.types = TreeComboBox(self)
        # self.types.resize(240, 30)
        # self.types.currentIndexChanged.connect(self.change)
        # self.types.setFont(QFont("맑은 고딕", 9))
        # self.types.setModel(getLeafTypeModel())
        # self.types.click.connect(self.doubleClickEvent)

        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def selectedType(self):
        for ix in self.types.selectedIndexes():
            return ix.data(Qt.DisplayRole)

    def doubleClickEvent(self):
        global isDoubleClicked
        isDoubleClicked = True
        if self.selectedType() in ALL_LEAF_TYPES:
            self.accept()

    def change(self):
        if self.types.currentText() not in ALL_LEAF_TYPES:
            self.types.showPopup()

    @staticmethod
    def get(parent=None):
        global isDoubleClicked
        _win = setLeafType(parent)
        result = _win.exec_()
        data = _win.selectedType()
        if data in ALL_LEAF_TYPES:
            return data, result == QDialog.Accepted
        else:
            if isDoubleClicked:
                return None, False
            return "CANCELED", False

    @staticmethod
    def make(parent=None):
        global isDoubleClicked
        setLeafType(parent).exec_()
