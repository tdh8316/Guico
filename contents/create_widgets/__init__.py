from contents.create_widgets.draw_image import content_DRAW_IMAGE
from contents.create_widgets.draw_text import content_DRAW_TEXT, content_SCREEN_CLEAR
from contents.create_widgets.key_input import (content_KEY_INPUT,
                                               content_KEY_NOT_INPUT)
from contents.create_widgets.sprite_utils import *
from contents.create_widgets.variable_change import (content_VARIABLE_DEFINE,
                                                     content_VARIABLE_PLUS)
from contents.create_widgets.window_new import content_WINDOW_NEW
from gui.widgets.customized import CodeEditWithDisableError

NODE_CONTENTS = None


def content_PYTHON_NATIVE(self):
    self.layout = QVBoxLayout()
    self.textbox = CodeEditWithDisableError()  # 그 텍스트박스 그거임
    # self.wdg_label = QLabel(self.title)  # 그거 종류 그 뭐냐 하여튼 그거

    self.layout.setContentsMargins(0, 0, 0, 0)
    self.setLayout(self.layout)
    # self.layout.addWidget(self.wdg_label)
    self.layout.addWidget(self.textbox)
