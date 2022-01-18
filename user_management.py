# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import conndb


class user_management(QtWidgets.QWidget):
    def __init__(self):
        super(user_management,self).__init__()
        uic.loadUi("user_management.ui", self)
        self.setWindowTitle("User Management")
        self.pushButtonLoad.clicked.connect(self.loadData)
        self.clearData()
        self.pushButtonSave.setEnabled(False)
        self.pushButtonSave.clicked.connect(self.saveData)
        self.pushButtonDelete.clicked.connect(self.deleteData)
        self.pushButtonClear.clicked.connect(self.clearData)
        self.pushButtonAdd.clicked.connect(self.addData)
        self.tableWidget.clicked.connect(self.getItem)
        pass

    def getItem(self):
        self.pushButtonAdd.setEnabled(False)
        self.pushButtonSave.setEnabled(True)
        row = self.tableWidget.currentRow()
        print(str(row))
        rowItemUsername = self.tableWidget.item(row, 1).text()
        rowItemFullname = self.tableWidget.item(row, 2).text()
        rowItemPassword = self.tableWidget.item(row, 3).text()
        rowItemGroup = self.tableWidget.item(row, 4).text()

        self.lineEditUser.setText(rowItemUsername)
        self.lineEditFullName.setText(rowItemFullname)
        self.lineEditPassword.setText(rowItemPassword)
        self.comboBoxGroup.setCurrentText(rowItemGroup)

    def clearData(self):
        self.lineEditUser.setText("")
        self.lineEditFullName.setText("")
        self.lineEditPassword.setText("")
        self.comboBoxGroup.setCurrentIndex(-1);
        self.pushButtonAdd.setEnabled(True)
        self.pushButtonSave.setEnabled(False)

    def addData(self):
        username = self.lineEditUser.text()
        fullname = self.lineEditFullName.text()
        password = self.lineEditPassword.text()
        group = self.comboBoxGroup.currentText()
        strsql = "INSERT INTO `tbl_user` (`id`, `username`, `full_name`, `password`, `group`) VALUES (NULL, '"+username+"', '"+fullname+"', '"+password+"', '"+group+"') "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Tambahkan",QMessageBox.Ok)
        self.loadData()


    def deleteData(self):
        username = self.lineEditUser.text()
        strsql = "DELETE FROM tbl_user WHERE `username`='"+username+"' "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Hapus",QMessageBox.Ok)
        self.loadData()

    def saveData(self):
        username = self.lineEditUser.text()
        fullname = self.lineEditFullName.text()
        password = self.lineEditPassword.text()
        group = self.comboBoxGroup.currentText()
        strsql = "UPDATE tbl_user SET `full_name`='"+fullname+"', `password`='"+password+"', `group`='"+group+"' WHERE `username`='"+username+"' "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Simpan",QMessageBox.Ok)
        self.loadData()


    def loadData(self):
        conn = conndb.conndb()
        strsql = "SELECT * FROM tbl_user"
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        self.tableWidget.setRowCount(len(result))
        for user in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(user[3]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(user[4]))
            row = row+1
        self.clearData()
