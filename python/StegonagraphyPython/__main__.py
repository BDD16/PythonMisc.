"""
Main package for Steganography Application
"""

from PyQt5.QtWidgets import QApplication
from python.StegonagraphyPython.Views.MainWindow import MainWindow
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())