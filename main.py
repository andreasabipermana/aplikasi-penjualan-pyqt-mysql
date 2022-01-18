# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, uic
import user_management as um
import login
import tentang
import barang as b
import vendor as v
import kasir as ks
import laporan as l

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("main.ui",self)
        self.setWindowTitle("Berlian Motor")
        self.logout()
        self.actionUser_Management.triggered.connect(self.usermgt)
        self.actionData_Barang.triggered.connect(self.barang)
        self.actionData_Vendor.triggered.connect(self.vendor)
        self.actionLogin.triggered.connect(self.login)
        self.actionLogout.triggered.connect(self.logout)
        self.actionAplikasi.triggered.connect(self.tentang)
        self.actionAplikasi_Kasir.triggered.connect(self.kasir)
        self.actionLaporan_Keuangan.triggered.connect(self.laporan)

    def logout(self):
        self.menuAdmin.setEnabled(False)
        self.menuKasir.setEnabled(False)
        self.menuLaporan.setEnabled(False)

    def login(self):
        self.lg = login.login()
        self.lg.exec()
        result = self.lg.result
        self.logout()
        if result == "ad":
            self.menuAdmin.setEnabled(True)
            self.menuLaporan.setEnabled(True)
        if result == "ks":
            self.menuKasir.setEnabled(True)

    def usermgt(self):
        self.umw = um.user_management()
        self.mdiArea.addSubWindow(self.umw)
        self.umw.show()

    def barang(self):
        self.br = b.barang()
        self.mdiArea.addSubWindow(self.br)
        self.br.show()

    def vendor(self):
        self.vn = v.vendor()
        self.mdiArea.addSubWindow(self.vn)
        self.vn.show()

    def laporan(self):
        self.lp = l.laporan()
        self.mdiArea.addSubWindow(self.lp)
        self.lp.show()

    def kasir(self):
        self.ksr = ks.kasir()
        self.mdiArea.addSubWindow(self.ksr)
        self.ksr.show()

    def tentang(self):
        self.tn = tentang.tentang()
        self.tn.exec()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
