from collections import OrderedDict
from gui.node.serializable import Serializable
from PyQt5.QtWidgets import *

from gui.node import leaf_attribute


class QDMNodeContentWidget(QWidget, Serializable):

    def __init__(self, node, title, parent=None):
        super().__init__(parent)

        self.node = node
        self.title = title
        self.type = title

        if self.type == "Branch":
            leaf_attribute.content_if(self)
        elif self.type == "Print":
            leaf_attribute.content_print(self)

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value

    def serialize(self):
        return OrderedDict([

        ])

    def deserialize(self, data, hashmap={}):
        return False
