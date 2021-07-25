from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QPushButton

me = '[FileBrowserWindow]'


class FileBrowserWindow(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__(None, modal=True)
        self.filePath = None
        self.file = self.getFile()

    def getFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Image Files (*.png);; "
                                                                                             "Image Files (*.jpeg);;"
                                                                                             "Image Files (*.tiff);",
                                                  options=options)
        self.filePath = fileName

        print(me + self.filePath)
        return self.filePath
