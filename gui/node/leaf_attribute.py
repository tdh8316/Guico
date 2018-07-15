from PyQt5.QtWidgets import *


def content_print(self):
    self.layout = QVBoxLayout()
    self.textbox = QDMTextEdit("")  # 그 텍스트박스 그거임
    # self.wdg_label = QLabel(self.title)  # 그거 종류 그 뭐냐 하여튼 그거

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.layout)
    # self.layout.addWidget(self.wdg_label)
    self.layout.addWidget(self.textbox)


def content_if(self):
    self.layout = QVBoxLayout()
    # self.wdg_label = QLabel(self.title)  # 그거 종류 그 뭐냐 하여튼 그거

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.layout)
    # self.layout.addWidget(self.wdg_label)=


class QDMTextEdit(QPlainTextEdit):
    def focusInEvent(self, event):
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)
