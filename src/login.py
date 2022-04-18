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
        self.navbar = QtWidgets.QFrame(self.bgwidget)
        self.navbar.setGeometry(QtCore.QRect(0, 0, 1211, 91))
        self.navbar.setStyleSheet("QFrame#navbar{\n"
                                  "    background-color: rgb(234, 216, 202);\n"
                                  "   \n"
                                  "    border-style: outset;\n"
                                  "    padding: 5px;\n"
                                  "}")
        self.navbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navbar.setObjectName("navbar")
        self.frame_2 = QtWidgets.QFrame(self.navbar)
        self.frame_2.setGeometry(QtCore.QRect(-10, -30, 1211, 51))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
                                   "    background-color: rgb(136, 179, 160);\n"
                                   "   \n"
                                   "    border-style: outset;\n"
                                   "    padding: 5px;\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Logo = QtWidgets.QLabel(self.navbar)
        self.Logo.setGeometry(QtCore.QRect(0, 0, 281, 121))
        self.Logo.setStyleSheet("font: 87 26pt \"Sansita\";\n"
                                "color : rgb(0, 0, 0) ")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("././img/logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo.setObjectName("Logo")
        self.berandaButton = QtWidgets.QPushButton(self.navbar)
        self.berandaButton.setGeometry(QtCore.QRect(350, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.berandaButton.setFont(font)
        self.berandaButton.setAutoFillBackground(False)
        self.berandaButton.setStyleSheet("QPushButton {\n"
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
        self.berandaButton.setCheckable(False)
        self.berandaButton.setObjectName("berandaButton")
        self.tanamanButton = QtWidgets.QPushButton(self.navbar)
        self.tanamanButton.setGeometry(QtCore.QRect(520, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.tanamanButton.setFont(font)
        self.tanamanButton.setStyleSheet("QPushButton {\n"
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
        self.tanamanButton.setCheckable(False)
        self.tanamanButton.setObjectName("tanamanButton")
        self.aboutButton = QtWidgets.QPushButton(self.navbar)
        self.aboutButton.setGeometry(QtCore.QRect(670, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.aboutButton.setFont(font)
        self.aboutButton.setStyleSheet("QPushButton {\n"
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
        self.aboutButton.setCheckable(False)
        self.aboutButton.setObjectName("aboutButton")
        self.searchButton = QtWidgets.QPushButton(self.navbar)
        self.searchButton.setGeometry(QtCore.QRect(930, 40, 31, 31))
        self.searchButton.setMouseTracking(False)
        self.searchButton.setAutoFillBackground(False)
        self.searchButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("././img/Search.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QtCore.QSize(31, 31))
        self.searchButton.setAutoDefault(True)
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(True)
        self.searchButton.setObjectName("searchButton")
        self.userButton = QtWidgets.QPushButton(self.navbar)
        self.userButton.setGeometry(QtCore.QRect(980, 35, 31, 41))
        self.userButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("././img/User.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton.setIcon(icon1)
        self.userButton.setIconSize(QtCore.QSize(31, 41))
        self.userButton.setFlat(True)
        self.userButton.setObjectName("userButton")
        self.cartButton = QtWidgets.QPushButton(self.navbar)
        self.cartButton.setGeometry(QtCore.QRect(1080, 30, 31, 51))
        self.cartButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("././img/Shopping Cart.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("././img/Shopping Cart.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cartButton.setIcon(icon2)
        self.cartButton.setIconSize(QtCore.QSize(31, 51))
        self.cartButton.setAutoExclusive(False)
        self.cartButton.setAutoDefault(True)
        self.cartButton.setFlat(True)
        self.cartButton.setObjectName("cartButton")
        self.notification = QtWidgets.QLabel(self.navbar)
        self.notification.setGeometry(QtCore.QRect(1030, 40, 31, 31))
        self.notification.setText("")
        self.notification.setPixmap(QtGui.QPixmap("././img/Doorbell.png"))
        self.notification.setScaledContents(True)
        self.notification.setObjectName("notification")

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
        self.berandaButton.setText(_translate("Dialog", "Beranda"))
        self.tanamanButton.setText(_translate("Dialog", "Tanaman"))
        self.aboutButton.setText(_translate("Dialog", "Tentang Kami"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())