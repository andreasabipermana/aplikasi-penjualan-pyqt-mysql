# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import conndb

class vendor(QtWidgets.QWidget):
    def __init__(self):
        super(vendor,self).__init__()
        uic.loadUi("vendor.ui", self)
        self.setWindowTitle("Data Vendor")
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
        rowItemKode = self.tableWidget.item(row, 1).text()
        rowItemNamaVendor = self.tableWidget.item(row, 2).text()
        self.lineEditKode.setText(rowItemKode)
        self.lineEditNamaVendor.setText(rowItemNamaVendor)


    def clearData(self):
        self.lineEditNamaVendor.setText("")
        self.lineEditKode.setText("")
        self.pushButtonAdd.setEnabled(True)
        self.pushButtonSave.setEnabled(False)

    def addData(self):
        nama = self.lineEditNamaVendor.text()
        kode = self.lineEditKode.text()
        strsql = "INSERT INTO `tbl_vendor` (`id`, kode, `nama`) VALUES (NULL, '"+kode+"', '"+nama+"') "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Tambahkan",QMessageBox.Ok)
        self.loadData()


    def deleteData(self):
        kode = self.lineEditKode.text()
        strsql = "DELETE FROM tbl_vendor WHERE `kode`='"+kode+"' "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Hapus",QMessageBox.Ok)
        self.loadData()

    def saveData(self):
        nama = self.lineEditNamaVendor.text()
        kode = self.lineEditKode.text()
        strsql = "UPDATE tbl_vendor SET `nama`='"+nama+"' WHERE `kode`='"+kode+"' "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Simpan",QMessageBox.Ok)
        self.loadData()


    def loadData(self):
        conn = conndb.conndb()
        strsql = "SELECT * FROM tbl_vendor"
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        self.tableWidget.setRowCount(len(result))
        for vendor in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(vendor[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(vendor[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(vendor[2]))
            row = row+1
        self.clearData()
