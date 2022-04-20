from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel, QDialogButtonBox

class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        grid_layout = self.layout()

        qt_msgboxex_icon_label = self.findChild(QLabel, "qt_msgboxex_icon_label")
        qt_msgboxex_icon_label.deleteLater()

        qt_msgbox_label = self.findChild(QLabel, "qt_msgbox_label")
        qt_msgbox_label.setAlignment(Qt.AlignCenter)
        grid_layout.removeWidget(qt_msgbox_label)

        qt_msgbox_buttonbox = self.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
        grid_layout.removeWidget(qt_msgbox_buttonbox)

        grid_layout.addWidget(qt_msgbox_label, 0, 0, alignment=Qt.AlignCenter)
        grid_layout.addWidget(qt_msgbox_buttonbox, 1, 0, alignment=Qt.AlignCenter)

def messageBoxLoginBerhasil():
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 200))
    messageBox.setMaximumSize(QtCore.QSize(400, 200))
    messageBox.setText("Login berhasil!")
    messageBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
    messageBox.setWindowTitle("Login Berhasil")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.exec()

def messageBoxLoginGagal(LoggedInId, username, password):
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 200))
    messageBox.setMaximumSize(QtCore.QSize(400, 200))
    messageBox.setText("Login gagal!")
    messageBox.setWindowTitle("Login Gagal")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Critical)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    if (username == ""):
        messageBox.setDetailedText("Username tidak boleh kosong!")
    elif (password == ""):
        messageBox.setDetailedText("Password tidak boleh kosong!")
    else :
        messageBox.setDetailedText("Username atau password salah")
    messageBox.exec()

def messageBoxRegisterBerhasil(username):
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 400))
    messageBox.setMaximumSize(QtCore.QSize(400, 400))
    messageBox.setText("Registrasi berhasil!<br>")
    messageBox.setInformativeText(username + " berhasil terdaftar.<br> Silahkan login untuk melanjutkan.")
    messageBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
    messageBox.setWindowTitle("Registrasi Berhasil")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.exec()

def messageBoxRegisterGagal():
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 200))
    messageBox.setMaximumSize(QtCore.QSize(400, 200))
    messageBox.setText("Register gagal!")
    messageBox.setWindowTitle("Registrasi gagal")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Critical)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.setDetailedText("Tidak boleh ada data yang kosong!")
    messageBox.exec()

def messageBoxAddTanamanBerhasil(nama):
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 400))
    messageBox.setMaximumSize(QtCore.QSize(400, 400))
    messageBox.setText("Tambah tanaman berhasil!")
    messageBox.setInformativeText(nama + " berhasil ditambahkan.")
    messageBox.setWindowTitle("Tambah Tanaman Berhasil")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Information)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.exec()

def messageBoxAddTanamanGagal() :
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 200))
    messageBox.setMaximumSize(QtCore.QSize(400, 200))
    messageBox.setText("Tambah tanaman gagal!")
    messageBox.setWindowTitle("Tambah tanaman gagal")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Critical)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.setDetailedText("Tidak boleh ada data yang kosong!")
    messageBox.exec()

def messageBoxEditTanamanGagal() :
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 200))
    messageBox.setMaximumSize(QtCore.QSize(400, 200))
    messageBox.setText("Edit tanaman gagal!")
    messageBox.setWindowTitle("Edit tanaman gagal")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Critical)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.setDetailedText("Tidak boleh ada data yang kosong!")
    messageBox.exec()

def messageBoxEditTanamanBerhasil(nama):
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 400))
    messageBox.setMaximumSize(QtCore.QSize(400, 400))
    messageBox.setText("Edit tanaman berhasil!")
    messageBox.setInformativeText("Data" + nama + " berhasil diedit.")
    messageBox.setWindowTitle("Edit Tanaman Berhasil")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Information)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.exec()

def messageBoxTambahKeranjangBerhasil():
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 400))
    messageBox.setMaximumSize(QtCore.QSize(400, 400))
    messageBox.setText("Tambah keranjang berhasil!")
    messageBox.setInformativeText("Tanaman berhasil ditambahkan ke keranjang.")
    messageBox.setWindowTitle("Tambah Keranjang Berhasil")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Information)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.exec()

def messageBoxTambahKeranjangGagal(jumlah, stok, mulaisewa, kembalisewa):
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 400))
    messageBox.setMaximumSize(QtCore.QSize(400, 400))
    messageBox.setText("Tambah keranjang gagal!")
    messageBox.setWindowTitle("Tambah Keranjang Gagal")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Critical)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    if (jumlah > stok) :
        messageBox.setDetailedText("Jumlah tanaman yang ditambahkan melebihi stok.")
    elif (mulaisewa > kembalisewa) :
        messageBox.setDetailedText("Tanggal sewa tidak valid. Tanggal pengembalian tidak dapat melebihi tanggal mulai sewa.")
    messageBox.exec()

def messageBoxCheckoutBerhasil():
    messageBox = MessageBox()
    messageBox.setMinimumSize(QtCore.QSize(400, 200))
    messageBox.setMaximumSize(QtCore.QSize(400, 200))
    messageBox.setText("Checkout berhasil!")
    messageBox.setWindowTitle("Checkout Berhasil")
    messageBox.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    messageBox.setIcon(QtWidgets.QMessageBox.Information)
    messageBox.setStyleSheet("background-color: rgb(255, 255, 255);")
    messageBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
    messageBox.exec()

class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        self.setIcon(QtGui.QIcon("./img/eyeclose.png"))

    def mouseReleaseEvent(self, event):
        super(PushButton, self).mouseReleaseEvent(event)
        self.setIcon(
            QtGui.QIcon("./img/eyeopen.png" if self.isChecked() else "./img/eyeclose.png"))