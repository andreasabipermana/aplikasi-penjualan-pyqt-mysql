# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
import conndb


class laporan(QtWidgets.QWidget):
    def __init__(self):
        super(laporan,self).__init__()
        uic.loadUi("laporan.ui", self)
        self.setWindowTitle("Laporan")
        self.pushButtonLoad.clicked.connect(self.loadData)
        pass

    def getTotalPendapatan(self):
        baris = self.tableWidget.rowCount()
        total = 0
        for i in range(baris):
            total = total + int(self.tableWidget.item(i,3).text())
        return total

    def getTotalKeuntungan(self):
        baris = self.tableWidget.rowCount()
        total = 0
        for i in range(baris):
            total = total + int(self.tableWidget.item(i,4).text())
        return total

    def loadData(self):
        conn = conndb.conndb()
        strsql = "SELECT * FROM tbl_transaksi"
        result = conn.queryResult(strsql)
        print(result)
        row = 0
        self.tableWidget.setRowCount(len(result))
        for transaksi in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(transaksi[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(transaksi[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(transaksi[2])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(transaksi[3])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(transaksi[4])))
            row = row+1
        self.labelPenghasilan.setText("Rp. {0}".format(self.getTotalPendapatan()))
        self.labelKeuntungan.setText("Rp. {0}".format(self.getTotalKeuntungan()))

