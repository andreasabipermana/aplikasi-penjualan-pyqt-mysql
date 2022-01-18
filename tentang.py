# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic


class tentang(QtWidgets.QDialog):
    def __init__(self):
        super(tentang,self).__init__()
        uic.loadUi("tentang.ui", self)
        self.setWindowTitle("Tentang")
        pass
