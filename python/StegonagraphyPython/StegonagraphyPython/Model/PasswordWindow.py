from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QInputDialog, QLineEdit, QFileDialog

me = '[PasswordWindow]'


class PasswordWindow(QWidget):
    submitted = pyqtSignal(str)

    def __init__(self):
        super().__init__(None, modal=True)
        self.pwd_clear = None
        self.password = self.getPass()

    def getPass(self):
        print('about to open a password dialog')
        self.pwd_clear, ok = QInputDialog.getText(self, "Attention", "Password?",
                                                  QLineEdit.Password, '')
        if self.pwd_clear and ok != '':
            print(me + self.pwd_clear)
            self.password = self.pwd_clear
            return self.pwd_clear
