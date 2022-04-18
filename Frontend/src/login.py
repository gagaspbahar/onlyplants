# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        Dialog.setMinimumSize(QtCore.QSize(1200, 800))
        Dialog.setMaximumSize(QtCore.QSize(1200, 800))
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setEnabled(True)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.bgwidget.setMinimumSize(QtCore.QSize(1200, 800))
        self.bgwidget.setMaximumSize(QtCore.QSize(1200, 800))
        self.bgwidget.setAutoFillBackground(False)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color: white;}")
        self.bgwidget.setObjectName("bgwidget")
        self.loginframe = QtWidgets.QFrame(self.bgwidget)
        self.loginframe.setGeometry(QtCore.QRect(330, 190, 531, 401))
        self.loginframe.setStyleSheet("QFrame#loginframe{\n"
"    background-color: rgb(244, 208, 185);\n"
"    border: 0px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}")
        self.loginframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginframe.setObjectName("loginframe")
        self.usernamebox = QtWidgets.QLineEdit(self.loginframe)
        self.usernamebox.setGeometry(QtCore.QRect(30, 60, 471, 51))
        self.usernamebox.setStyleSheet("QLineEdit#usernamebox{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.usernamebox.setText("")
        self.usernamebox.setObjectName("usernamebox")
        self.usernamebox_2 = QtWidgets.QLineEdit(self.loginframe)
        self.usernamebox_2.setGeometry(QtCore.QRect(30, 170, 471, 51))
        self.usernamebox_2.setStyleSheet("QLineEdit#usernamebox_2{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.usernamebox_2.setText("")
        self.usernamebox_2.setObjectName("usernamebox_2")
        self.QPushButton_3 = QtWidgets.QPushButton(self.loginframe)
        self.QPushButton_3.setGeometry(QtCore.QRect(190, 300, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(11)
        self.QPushButton_3.setFont(font)
        self.QPushButton_3.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    background-color : rgb(136, 179, 160);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : white;\n"
"    background-color : rgb(85, 170, 127)\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.QPushButton_3.setCheckable(False)
        self.QPushButton_3.setObjectName("QPushButton_3")
        self.label_2 = QtWidgets.QLabel(self.loginframe)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 81, 16))
        self.label_2.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.loginframe)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label_3.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.loginframe)
        self.label_5.setGeometry(QtCore.QRect(170, 360, 161, 20))
        self.label_5.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_5.setObjectName("label_5")
        self.daftarButton = QtWidgets.QPushButton(self.loginframe)
        self.daftarButton.setGeometry(QtCore.QRect(320, 354, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(12)
        font.setUnderline(True)
        self.daftarButton.setFont(font)
        self.daftarButton.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    text-decoration: underline;\n"
"    background-color : rgb(244, 208, 185);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : white;\n"
"    text-decoration: underline; \n"
"    }")
        self.daftarButton.setCheckable(False)
        self.daftarButton.setObjectName("daftarButton")
        self.navbar = QtWidgets.QFrame(self.bgwidget)
        self.navbar.setGeometry(QtCore.QRect(-10, 0, 1211, 91))
        self.navbar.setStyleSheet("QFrame#navbar{\n"
"    background-color: rgb(234, 216, 202);\n"
"   \n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}")
        self.navbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navbar.setObjectName("navbar")
        self.frame_5 = QtWidgets.QFrame(self.navbar)
        self.frame_5.setGeometry(QtCore.QRect(10, -30, 1451, 51))
        self.frame_5.setStyleSheet("QFrame{\n"
"    background-color: rgb(136, 179, 160);\n"
"   \n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.Logo_4 = QtWidgets.QLabel(self.navbar)
        self.Logo_4.setGeometry(QtCore.QRect(0, 0, 281, 121))
        self.Logo_4.setStyleSheet("font: 87 26pt \"Sansita\";\n"
"color : rgb(0, 0, 0) ")
        self.Logo_4.setText("")
        self.Logo_4.setPixmap(QtGui.QPixmap("././img/logo.png"))
        self.Logo_4.setScaledContents(True)
        self.Logo_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo_4.setObjectName("Logo_4")
        self.berandaButton_3 = QtWidgets.QPushButton(self.navbar)
        self.berandaButton_3.setGeometry(QtCore.QRect(350, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.berandaButton_3.setFont(font)
        self.berandaButton_3.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : rgb(53, 78, 59);\n"
"    background-color :  rgb(234, 216, 202);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : white;\n"
"    }")
        self.berandaButton_3.setCheckable(False)
        self.berandaButton_3.setObjectName("berandaButton_3")
        self.tanamanButton_3 = QtWidgets.QPushButton(self.navbar)
        self.tanamanButton_3.setGeometry(QtCore.QRect(520, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.tanamanButton_3.setFont(font)
        self.tanamanButton_3.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color :  rgb(53, 78, 59);\n"
"    background-color :  rgb(234, 216, 202);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : white;\n"
"    }")
        self.tanamanButton_3.setCheckable(False)
        self.tanamanButton_3.setObjectName("tanamanButton_3")
        self.aboutButton_3 = QtWidgets.QPushButton(self.navbar)
        self.aboutButton_3.setGeometry(QtCore.QRect(670, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.aboutButton_3.setFont(font)
        self.aboutButton_3.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : rgb(53, 78, 59);\n"
"    background-color :  rgb(234, 216, 202);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : white;\n"
"    }")
        self.aboutButton_3.setCheckable(False)
        self.aboutButton_3.setObjectName("aboutButton_3")
        self.search_3 = QtWidgets.QLabel(self.navbar)
        self.search_3.setGeometry(QtCore.QRect(930, 40, 31, 31))
        self.search_3.setText("")
        self.search_3.setPixmap(QtGui.QPixmap("././img/Search.png"))
        self.search_3.setScaledContents(True)
        self.search_3.setObjectName("search_3")
        self.account_3 = QtWidgets.QLabel(self.navbar)
        self.account_3.setGeometry(QtCore.QRect(980, 35, 31, 41))
        self.account_3.setText("")
        self.account_3.setPixmap(QtGui.QPixmap("././img/User.png"))
        self.account_3.setScaledContents(True)
        self.account_3.setObjectName("account_3")
        self.notification_3 = QtWidgets.QLabel(self.navbar)
        self.notification_3.setGeometry(QtCore.QRect(1030, 40, 31, 31))
        self.notification_3.setText("")
        self.notification_3.setPixmap(QtGui.QPixmap("././img/Doorbell.png"))
        self.notification_3.setScaledContents(True)
        self.notification_3.setObjectName("notification_3")
        self.keranjang_3 = QtWidgets.QLabel(self.navbar)
        self.keranjang_3.setGeometry(QtCore.QRect(1080, 30, 31, 51))
        self.keranjang_3.setText("")
        self.keranjang_3.setPixmap(QtGui.QPixmap("././img/Shopping Cart.png"))
        self.keranjang_3.setScaledContents(True)
        self.keranjang_3.setObjectName("keranjang_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.QPushButton_3.setText(_translate("Dialog", "Masuk"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_5.setText(_translate("Dialog", "Belum memiliki akun ?"))
        self.daftarButton.setText(_translate("Dialog", "Daftar"))
        self.berandaButton_3.setText(_translate("Dialog", "Beranda"))
        self.tanamanButton_3.setText(_translate("Dialog", "Tanaman"))
        self.aboutButton_3.setText(_translate("Dialog", "Tentang Kami"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())