# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import conndb


class kasir(QtWidgets.QWidget):
    def __init__(self):
        super(kasir,self).__init__()
        uic.loadUi("kasir.ui", self)
        self.setWindowTitle("Kasir")
        self.getCombo()
        self.clearData()
        self.comboBoxNamaBarang.currentTextChanged.connect(self.loadData)
        self.lineEditVendor.setReadOnly(True)
        self.lineEditHargaBarang.setReadOnly(True)
        self.pushButtonTambahTransaksi.clicked.connect(self.tambahTransaksi)
        self.pushButtonBayar.clicked.connect(self.bayarTransaksi)
        pass

    def getCombo(self):
        self.comboBoxNamaBarang.clear()
        conn = conndb.conndb()
        strsql = "SELECT nama FROM tbl_barang"
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        for barang in result:
            self.comboBoxNamaBarang.addItems(barang)
            row = row+1


    def loadData(self):
        nama = self.comboBoxNamaBarang.currentText()
        conn = conndb.conndb()
        strsql = "SELECT * FROM tbl_barang WHERE `nama`='"+nama+"' "
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        for barang in result:
            self.lineEditVendor.setText(barang[3])
            self.lineEditHargaBarang.setText(str(barang[5]))

    def clearData(self):
        self.comboBoxNamaBarang.setCurrentIndex(-1)
        self.lineEditVendor.setText("")
        self.lineEditHargaBarang.setText("")
        self.lineEditJumlahBarang.setText("")

    def getTotal(self):
        baris = self.tableBarang.rowCount()
        total = 0
        for i in range(baris):
            total = total + int(self.tableBarang.item(i,4).text())
        return total

    def checkData(self, nama, harga_barang, jumlah_barang):
        data = 0
        baris = self.tableBarang.rowCount()
        for i in range(baris):
            if nama == self.tableBarang.item(i,0).text():
                data = 1
        return data

    def _tambahTransaksi(self,nama,vendor,harga_barang,jumlah_barang):
        data = self.checkData(nama, harga_barang, jumlah_barang)
        print(data)
        if data ==0:
            baris = self.tableBarang.rowCount()
            self.tableBarang.setRowCount(baris+1)
            self.tableBarang.setItem(baris,0,QtWidgets.QTableWidgetItem(nama))
            self.tableBarang.setItem(baris,1,QtWidgets.QTableWidgetItem(vendor))
            self.tableBarang.setItem(baris,2,QtWidgets.QTableWidgetItem(harga_barang))
            self.tableBarang.setItem(baris,3,QtWidgets.QTableWidgetItem(jumlah_barang))
            self.tableBarang.setItem(baris,4,QtWidgets.QTableWidgetItem(str(int(harga_barang)*int(jumlah_barang))))
        if data ==1:
            baris = self.tableBarang.rowCount()
            for i in range(baris):
                if nama == self.tableBarang.item(i,0).text():
                    magic = i
            jumlahold = self.tableBarang.item(magic,3).text()
            harga_barang = self.tableBarang.item(magic,2).text()
            self.tableBarang.setItem(magic, 3, QtWidgets.QTableWidgetItem(str(int(jumlahold)+int(jumlah_barang))))
            jumlahbaru = self.tableBarang.item(magic, 3).text()
            self.tableBarang.setItem(magic, 4, QtWidgets.QTableWidgetItem(str(int(harga_barang)*int(jumlahbaru))))

    def tambahTransaksi(self):
        nama = self.comboBoxNamaBarang.currentText()
        vendor = self.lineEditVendor.text()
        harga_barang = self.lineEditHargaBarang.text()
        jumlah_barang = self.lineEditJumlahBarang.text()
        self._tambahTransaksi(nama,vendor,harga_barang,jumlah_barang)
        self.clearData()

        self.labelTotal.setText("Rp. {0}".format(self.getTotal()))

    def getHargaBeli(self, nama):
        conn = conndb.conndb()
        strsql = "SELECT harga_beli FROM tbl_barang WHERE `nama`='"+nama+"' "
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        for barang in result:
            harga_beli = barang[0]
        return harga_beli
    def getHargaJual(self, nama):
        conn = conndb.conndb()
        strsql = "SELECT harga_jual FROM tbl_barang WHERE `nama`='"+nama+"' "
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        for barang in result:
            harga_jual = barang[0]
        return harga_jual

    def simpanTransaksi(self):
        banyakBarang = self.tableBarang.rowCount()
        for barang in range(banyakBarang):
            nama = self.tableBarang.item(barang, 0).text()
            jumlah_barang = str(int(self.tableBarang.item(barang, 3).text()))
            total = str(int(self.tableBarang.item(barang, 4).text()))
            harga_beli = self.getHargaBeli(nama)
            harga_jual = self.getHargaJual(nama)
            keuntungan = str((int(harga_jual)-int(harga_beli))*int(jumlah_barang))
            strsql = "INSERT INTO `tbl_transaksi` (`id`, `nama`, `jumlah_barang`, `total`, `keuntungan`) VALUES (NULL, '"+nama+"', '"+jumlah_barang+"', '"+total+"', '"+keuntungan+"') "
            conn = conndb.conndb()
            result = conn.queryExecute(strsql)
        QMessageBox.information(None, "Sukses","Data Berhasil di Tambahkan",QMessageBox.Ok)


    def bayarTransaksi(self):
        bayar = self.lineEditBayar.text()
        total = self.getTotal()
        kembalian = int(bayar)-int(total)
        if kembalian < 0:
            QMessageBox.critical(None, "Gagal","Uang Tidak Mencukupi",QMessageBox.Ok)
        if kembalian >= 0:
            self.labelKembalian.setText("Rp. {0}".format(kembalian))
            self.simpanTransaksi()




