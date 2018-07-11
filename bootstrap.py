import os
import sys
import json
from PyQt5.QtWidgets import *
from gui.node_editor_widget import NodeEditorWidget
from gui.node_scene import Scene
from gui.node_node import Node

NAME = "Guico"
_FILE_TYPES = f"{NAME} Script Files (*.tsv);;" \
               "All Files (*.*)"


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.filename = None

        self.set_window()

    def set_window(self):
        self.setWindowTitle(f"TakTurStudio {NAME}")
        self.initialize_menu()
        # create node editor widget
        editor = NodeEditorWidget(self)
        editor.scene.addHasBeenModifiedListener(self.changeTitle)
        self.setCentralWidget(editor)

        # status bar
        self.statusBar().showMessage("")
        self.status_mouse_pos = QLabel("")
        self.statusBar().addPermanentWidget(self.status_mouse_pos)
        editor.view.scenePosChanged.connect(self.onScenePosChanged)

        # set window properties
        self.setGeometry(200, 200, 800, 600)
        self.changeTitle()
        self.show()

    def initialize_menu(self):
        menu_bar = self.menuBar()
        fileMenu = menu_bar.addMenu('&File')
        fileMenu.addAction(self.set_action('&New', 'Ctrl+N', "Create new graph", self.onFileNew))
        fileMenu.addSeparator()
        fileMenu.addAction(self.set_action('&Open', 'Ctrl+O', "Open file", self.onFileOpen))
        fileMenu.addAction(self.set_action('&Save', 'Ctrl+S', "Save file", self.onFileSave))
        fileMenu.addAction(self.set_action('Save &As...', 'Ctrl+Shift+S', "Save file as...", self.onFileSaveAs))
        fileMenu.addSeparator()
        fileMenu.addAction(self.set_action('E&xit', 'Ctrl+Q', "Exit application", self.close))

        editMenu = menu_bar.addMenu('&Edit')
        editMenu.addAction(self.set_action('&Undo', 'Ctrl+Z', "Undo last operation", self.onEditUndo))
        editMenu.addAction(self.set_action('&Redo', 'Ctrl+Shift+Z', "Redo last operation", self.onEditRedo))
        editMenu.addSeparator()
        editMenu.addAction(self.set_action('Cu&t', 'Ctrl+X', "Cut to clipboard", self.onEditCut))
        editMenu.addAction(self.set_action('&Copy', 'Ctrl+C', "Copy to clipboard", self.onEditCopy))
        editMenu.addAction(self.set_action('&Paste', 'Ctrl+V', "Paste from clipboard", self.onEditPaste))
        editMenu.addSeparator()
        editMenu.addAction(self.set_action('&Delete', 'Del', "Delete selected item(s)", self.onEditDelete))

        leafMenu = menu_bar.addMenu('&Leaf')
        leafMenu.addAction(self.set_action('New leaf', "", "Make new leaf", self.onNewLeaf))

    def set_action(self, name, shortcut, tooltip, callback):
        act = QAction(name, self)
        act.setShortcut(shortcut)
        act.setToolTip(tooltip)
        act.triggered.connect(callback)
        return act

    def changeTitle(self):
        title = f"TakTurStudio {NAME} - "
        if self.filename is None:
            title += "New"
        else:
            title += os.path.basename(self.filename)

        if self.centralWidget().scene.has_been_modified:
            title += "*"

        self.setWindowTitle(title)

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def isModified(self):
        return self.centralWidget().scene.has_been_modified

    def maybeSave(self):
        if not self.isModified():
            return True

        res = QMessageBox.warning(self, "About to loose your work?",
                                  "The document has been modified.\n Do you want to save your changes?",
                                  QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
                                  )

        if res == QMessageBox.Save:
            return self.onFileSave()
        elif res == QMessageBox.Cancel:
            return False

        return True

    def onScenePosChanged(self, x, y):
        self.status_mouse_pos.setText("x:%d y:%d" % (x, y))

    def onFileNew(self):
        if self.maybeSave():
            self.centralWidget().scene.clear()
            self.filename = None
            self.changeTitle()

    def onFileOpen(self):
        if self.maybeSave():
            fname, filter = QFileDialog.getOpenFileName(self, f'{NAME} - Open')
            if fname == '':
                return
            if os.path.isfile(fname):
                self.centralWidget().scene.loadFromFile(fname)
                self.filename = fname
                self.changeTitle()

    def onFileSave(self):
        if self.filename is None: return self.onFileSaveAs()
        self.centralWidget().scene.saveToFile(self.filename)
        self.statusBar().showMessage("Successfully saved %s" % self.filename)
        self.changeTitle()
        return True

    def onFileSaveAs(self):
        fname, filter = QFileDialog.getSaveFileName(self, f'{NAME} - Save As')
        if fname == '':
            return False
        self.filename = fname
        self.onFileSave()
        return True

    def onEditUndo(self):
        self.centralWidget().scene.history.undo()

    def onEditRedo(self):
        self.centralWidget().scene.history.redo()

    def onEditDelete(self):
        self.centralWidget().scene.grScene.views()[0].deleteSelected()

    def onEditCut(self):
        data = self.centralWidget().scene.clipboard.serializeSelected(delete=True)
        str_data = json.dumps(data, indent=4)
        QApplication.instance().clipboard().setText(str_data)

    def onEditCopy(self):
        data = self.centralWidget().scene.clipboard.serializeSelected(delete=False)
        str_data = json.dumps(data, indent=4)
        QApplication.instance().clipboard().setText(str_data)

    def onEditPaste(self):
        raw_data = QApplication.instance().clipboard().text()

        try:
            data = json.loads(raw_data)
        except ValueError as e:
            print("Pasting of not valid json data!", e)
            return

        # check if the json data are correct
        if 'nodes' not in data:
            print("JSON does not contain any nodes!")
            return

        self.centralWidget().scene.clipboard.deserializeFromClipboard(data)

    def onNewLeaf(self):
        NodeEditorWidget.newLeaf()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    root = MainWindow()
    root.show()

    sys.exit(app.exec_())
