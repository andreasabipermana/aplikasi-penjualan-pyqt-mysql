# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import conndb


class barang(QtWidgets.QWidget):
    def __init__(self):
        super(barang,self).__init__()
        uic.loadUi("barang.ui", self)
        self.setWindowTitle("Data Barang")
        self.pushButtonLoad.clicked.connect(self.loadData)
        self.clearData()
        self.getCombo()
        self.pushButtonSave.setEnabled(False)
        self.pushButtonSave.clicked.connect(self.saveData)
        self.pushButtonDelete.clicked.connect(self.deleteData)
        self.pushButtonClear.clicked.connect(self.clearData)
        self.pushButtonAdd.clicked.connect(self.addData)
        self.tableWidget.clicked.connect(self.getItem)
        pass

    def getCombo(self):
        self.comboBoxVendor.clear()
        conn = conndb.conndb()
        strsql = "SELECT nama FROM tbl_vendor"
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        for barang in result:
            self.comboBoxVendor.addItems(barang)
            row = row+1
        self.clearData()


    def getItem(self):
        self.pushButtonAdd.setEnabled(False)
        self.pushButtonSave.setEnabled(True)
        row = self.tableWidget.currentRow()
        print(str(row))
        rowItemKode = self.tableWidget.item(row, 1).text()
        rowItemNamaBarang = self.tableWidget.item(row, 2).text()
        rowItemVendor = self.tableWidget.item(row, 3).text()
        rowItemHargaBeli = self.tableWidget.item(row, 4).text()
        rowItemHargaJual = self.tableWidget.item(row, 5).text()

        self.lineEditKode.setText(rowItemKode)
        self.lineEditNamaBarang.setText(rowItemNamaBarang)
        self.comboBoxVendor.setCurrentText(rowItemVendor)
        self.lineEditHargaBeli.setText(rowItemHargaBeli)
        self.lineEditHargaJual.setText(rowItemHargaJual)

    def clearData(self):
        self.lineEditKode.setText("")
        self.lineEditNamaBarang.setText("")
        self.comboBoxVendor.setCurrentIndex(-1)
        self.lineEditHargaBeli.setText("")
        self.lineEditHargaJual.setText("")
        self.pushButtonAdd.setEnabled(True)
        self.pushButtonSave.setEnabled(False)

    def addData(self):
        kode = self.lineEditKode.text()
        nama = self.lineEditNamaBarang.text()
        vendor = self.comboBoxVendor.currentText()
        harga_beli = self.lineEditHargaBeli.text()
        harga_jual = self.lineEditHargaJual.text()
        strsql = "INSERT INTO `tbl_barang` (`id`, `kode`, `nama`, `vendor`, `harga_beli`, `harga_jual`) VALUES (NULL, '"+kode+"', '"+nama+"', '"+vendor+"', '"+harga_beli+"', '"+harga_jual+"') "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Tambahkan",QMessageBox.Ok)
        self.loadData()


    def deleteData(self):
        kode = self.lineEditKode.text()
        strsql = "DELETE FROM tbl_barang WHERE `kode`='"+kode+"' "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Hapus",QMessageBox.Ok)
        self.loadData()

    def saveData(self):
        kode = self.lineEditKode.text()
        nama = self.lineEditNamaBarang.text()
        vendor = self.comboBoxVendor.currentText()
        harga_beli = self.lineEditHargaBeli.text()
        harga_jual = self.lineEditHargaJual.text()
        strsql = "UPDATE tbl_barang SET `nama`='"+nama+"', `vendor`='"+vendor+"', `harga_beli`='"+harga_beli+"', `harga_jual`='"+harga_jual+"' WHERE `kode`='"+kode+"' "
        conn = conndb.conndb()
        result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Simpan",QMessageBox.Ok)
        self.loadData()


    def loadData(self):
        conn = conndb.conndb()
        strsql = "SELECT * FROM tbl_barang"
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        self.tableWidget.setRowCount(len(result))
        for barang in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(barang[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(barang[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(barang[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(barang[3]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(barang[4])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(barang[5])))
            row = row+1
        self.clearData()
