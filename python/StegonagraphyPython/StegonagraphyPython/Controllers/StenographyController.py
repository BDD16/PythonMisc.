"""
StenographyController.py
Handles when the Stenography button has been clicked
"""
import binascii
import sys, os
import traceback

import StegonagraphyPython.Model.cryptoutils as crypto_tools
from StegonagraphyPython.Model import HidingAnImage
from PyQt5.QtWidgets import QPushButton, QMessageBox
from StegonagraphyPython.Controllers.BaseController import BaseController
from StegonagraphyPython.Model.FileBrowserWindow import FileBrowserWindow
from StegonagraphyPython.Model.PasswordWindow import PasswordWindow
from PIL import Image

sys.path.insert(0, '../Model')
sys.path.insert(1, '../Views')

me = '[StenographyController]'

BIG_ENDIAN = True


# noinspection PyAttributeOutsideInit
class StenographyController(BaseController):

    def __init__(self, view, HiddenImageButton: QPushButton, ShownImageButon: QPushButton,
                 PassWordProtectedButton: QPushButton, GoTime: QPushButton):
        super().__init__(view)
        self.hiddenButton = HiddenImageButton
        self.showButton = ShownImageButon
        self.protection = PassWordProtectedButton
        self.go_baby_go = GoTime

        # Create class variables
        self.showPath = None
        self.hiddenPath = None
        self.password = None

        self.view = view
        self.RegisterFunctions()

    def RegisterFunctions(self):
        self.hiddenButton.clicked.connect(self.ClickedTheHiddenPathButton)
        self.showButton.clicked.connect(self.ClickedTheShowPathButton)
        self.protection.clicked.connect(self.ProtectTheHiddenImage)
        self.go_baby_go.clicked.connect(self.letsDoThis)

    def ClickedTheShowPathButton(self):
        self.showPath = FileBrowserWindow()

    def ClickedTheHiddenPathButton(self):
        self.hiddenPath = FileBrowserWindow()

    def ProtectTheHiddenImage(self):
        self.password = PasswordWindow()

    def letsDoThis(self):
        if self.showPath is None or self.showPath == '':
            print("made it here")
            QMessageBox.question(self.view, 'Attention: ', 'Please insert a Public Photo File Path',
                                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            return

        if self.hiddenPath is None or self.hiddenPath == '':
            QMessageBox.question(self.view, 'Attention: ', 'Please insert a Public Photo File Path',
                                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            return

        if self.password is None or self.password == '':
            # No need to use pycryptodome
            notice = QMessageBox.question(self.view, 'Notice: ', 'Watermark will not be password protected',
                                          QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
            if notice == QMessageBox.Cancel:
                return
        else:
            crypt = crypto_tools.CryptoTools()
            print(crypt)
            print(self.password.password)
            hash_value = crypt.Sha256(bytes(self.password.password.encode()))
            print(hash_value)
            notice = QMessageBox.question(self.view, "Info: ", "We are about to Hide some data within a publicly seen "
                                                               "image",
                                          QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
            if notice == QMessageBox.Ok:
                print('about to open the hidden path')
                fd = open(os.path.abspath(self.hiddenPath.filePath), 'rb')
                print("opening the hidden path")
                loadedBytes = fd.read()
                print("reading the file")
                fd.close()
                print("closed the file")

                result = crypt.AesCbcEncrypt(hash_value, hash_value[:16],
                                             loadedBytes)

                print(result)

                tmp_Filefd = open("./TmpFileSP", 'wb+')
                tmp_Filefd.write(result)
                tmp_Filefd.close()
                self.hiddenPath = "./TmpFileSP"
        try:
            self.CallerToStegonagrphyModel(self.hiddenPath.filePath, self.showPath.filePath)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=5, file=sys.stdout)
        # Clean up the Temporary Encrypted File
        if self.hiddenPath == "./TmpFileSP":
            os.remove("./TmpFileSP")

        try:
            data = self.CallerToStegonagraphyModel_Extract("./MVC_mergedImage.png")
            #fd = open("./EXTRACTED.png", 'wb+')
            #fd.write(data)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=5, file=sys.stdout)

    def CallerToStegonagrphyModel(self, hideThis: str, toBeSeen: str) -> object:
        # Merge_TheTwo_Images
        NI = HidingAnImage.Merge(Image.open(toBeSeen), Image.open(hideThis), BIG_ENDIAN)
        NI.save('./MVC_mergedImage.png')

    def CallerToStegonagraphyModel_Extract(self, extractFromThis: any) -> object:
        data = HidingAnImage.UnMerge(Image.open(extractFromThis))
        return data
