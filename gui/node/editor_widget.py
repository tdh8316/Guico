from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.node.edge import Edge, EDGE_TYPE_BEZIER
from leaf_content.default import *
from gui.node.scene import Scene
from gui.node.node import Node
from gui.node.graphics_view import QDMGraphicsView

from core import actions


class NodeEditorWidget(QWidget):
    def __init__(self, parent=None):
        super(NodeEditorWidget, self).__init__(parent)
        self.layout = QVBoxLayout()
        actions.set_editor(self)

        self.initUI()

    def initUI(self):
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # crate graphics scene
        self.scene = Scene()
        # self.grScene = self.scene.grScene

        # self.addNodes()
        self.add_default_node()

        # create graphics view
        self.view = QDMGraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

    def addNodes(self):
        node1 = Node(self.scene, "", inputs=[0,], outputs=[1], types=DRAW_TEXT)
        #node2 = Node(self.scene, "", inputs=[0,], outputs=[1])
        node3 = Node(self.scene, "", inputs=[0,], outputs=[1])
        node1.setPos(-350, -250)
        #node2.setPos(-75, 0)
        node3.setPos(200, -150)

    def add_default_node(self):
        self.entryNode = Node(self.scene, inputs=[], outputs=[1], types=ENTRY_POINT)
        self.entryNode.setPos(-250, -250)

        self.initwindowNode = Node(self.scene, inputs=[0], outputs=[1], types=WINDOW_NEW)
        self.entryNode.setPos(-250, 0)

        Edge(self.scene, self.entryNode.outputs[0], self.initwindowNode.inputs[0], edge_type=EDGE_TYPE_BEZIER)
