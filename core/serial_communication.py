try:
    # noinspection PyUnresolvedReferences
    from gui.node.content_widget import QDMNodeContentWidget
except ImportError:
    pass

from collections import OrderedDict
from contents.default import *


# noinspection PyMethodFirstArgAssignment
class Serial(object):
    def __init__(self, parent):
        self.parent: QDMNodeContentWidget = parent

    def serialize(self):
        self = self.parent

        if self.type == PRINT:
            return OrderedDict([("str", self.textbox.toPlainText())])
        elif self.type == DRAW_TEXT:
            return OrderedDict(
                [("str", self.textbox.text()), ("pos", self.position.text())]
            )
        elif self.type == WINDOW_NEW:
            return OrderedDict(
                [
                    # ("str", self.textbox.text()),
                    ("size", self._win_size.text())
                ]
            )
        elif self.type == KEY_INPUT:
            return OrderedDict([("key", self.key.currentText())])
        elif self.type == DRAW_IMAGE:
            return OrderedDict(
                [
                    ("path", self.image_path.WhereIsImage()),
                    ("pos", self.position.text()),
                ]
            )
        elif self.type == VARIABLE_DEFINE:
            return OrderedDict(
                [
                    ("name", self.var_name.textToVariableName()),
                    ("value", self.var_value.text()),
                ]
            )
        elif self.type == VARIABLE_PLUS:
            return OrderedDict(
                [
                    ("name", self.var_name.textToVariableName()),
                    ("value", self.var_value.text()),
                ]
            )
        elif self.type == ADD_GROUP:
            return OrderedDict(
                [("name", self.sprite_name.text()), ("group", self.group_name.text())]
            )
        elif self.type == DETECT_COLLISION:
            return OrderedDict([("1", self.group1.text()), ("2", self.group2.text())])
        elif self.type == DRAW_GROUP:
            return OrderedDict([("name", self.sprite_name.text())])
        elif self.type == PYTHON_NATIVE:
            return OrderedDict([("str", self.textbox.toPlainText())])

        return OrderedDict([])

    def deserialize(self, data, hashmap=None):
        self = self.parent

        if hashmap is None:
            hashmap = {}

        if self.type == PRINT:
            self.textbox.setPlainText(data["str"])
        elif self.type == DRAW_TEXT:
            self.textbox.setText(data["str"])
            self.position.setText(data["pos"])
        elif self.type == DRAW_IMAGE:
            self.image_path.setPath(data["path"])
            self.position.setText(data["pos"])
        elif self.type == WINDOW_NEW:
            self._win_size.setText(data["size"])
        elif self.type == KEY_INPUT:
            self.key.setCurrentText(data["key"])
            self.node.title = f"[{data['key']}] {KEY_INPUT}"
        elif self.type == VARIABLE_DEFINE:
            self.var_name.setVariableNameFromText(data["name"])
            self.var_value.setText(data["value"])
            # self.position.setText(data["pos"])
        elif self.type == VARIABLE_PLUS:
            self.var_name.setVariableNameFromText(data["name"])
            self.var_value.setText(data["value"])
        elif self.type == ADD_GROUP:
            self.sprite_name.setText(data["name"])
            self.group_name.setText(data["group"])
        elif self.type == DETECT_COLLISION:
            self.group1.setText(data["1"])
            self.group2.setText(data["2"])
        elif self.type == DRAW_GROUP:
            self.sprite_name.setText(data["name"])
        elif self.type == PYTHON_NATIVE:
            self.textbox.appendPlainText(data["str"])
