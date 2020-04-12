from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class _View(QGraphicsView):
    scenePosChanged = pyqtSignal(int, int)

    def __init__(self, grScene, x, y, parent=None):
        super().__init__(parent)
        self.grScene = grScene
        self.setScene(self.grScene)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setBackgroundBrush(QColor("#FFFFFF"))
        self.setSceneRect(0, 0, x, y)

        self.setFixedSize(x, y)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        last_scene_mouse_position = self.mapToScene(event.pos())
        self.scenePosChanged.emit(
            int(last_scene_mouse_position.x()), int(last_scene_mouse_position.y())
        )


class View(QWidget):
    def __init__(self, x, y, parent=None):
        super(View, self).__init__(parent)
        self.w = x // 2
        self.h = y // 2
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, self.w, self.h)
        self.view = _View(self.scene, self.w, self.h, self)
        self.layout = QVBoxLayout()
        self.pos_label = QLabel()
        self.pos_label.setText("0,0")
        self.pos_label.setAlignment(Qt.AlignCenter)

        self.initUI()

    def initUI(self):
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # crate graphics scene
        # self.grScene = self.scene.grScene
        # create graphics view
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.pos_label)
