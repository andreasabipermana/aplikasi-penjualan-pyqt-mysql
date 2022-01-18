# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget

import conndb

class login(QtWidgets.QDialog):
    def __init__(self):
        super(login,self).__init__()
        uic.loadUi("login.ui", self)
        self.setWindowTitle("Login")
        self.pushButtonLogin.clicked.connect(self.login)
        pass

    def login(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        conn = conndb.conndb()
        strsql = "SELECT `username`, `group` FROM `tbl_user` WHERE `username`='"+username+"' AND `password`='"+password+"' "
        result = conn.queryResult(strsql)
        if len(result) == 1:
            if result[0][1]=="ad":
                result = "ad"
                self.result = result
                self.close()
            elif result[0][1]=="ks":
                result = "ks"
                self.result = result
                self.close()
        if len(result) == 0:
            QMessageBox.critical(None, "Login Gagal","Username atau password salah !",QMessageBox.Cancel)


