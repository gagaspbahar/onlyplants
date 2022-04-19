# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(QtWidgets.QWidget):
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
        self.loginframe.setGeometry(QtCore.QRect(310, 140, 571, 611))
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
        self.emailBox = QtWidgets.QLineEdit(self.loginframe)
        self.emailBox.setGeometry(QtCore.QRect(30, 60, 501, 41))
        self.emailBox.setStyleSheet("QLineEdit#emailBox{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.emailBox.setText("")
        self.emailBox.setObjectName("emailBox")
        self.registerButton = QtWidgets.QPushButton(self.loginframe)
        self.registerButton.setGeometry(QtCore.QRect(190, 550, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(11)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-radius: 15px;\n"
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
        self.registerButton.setCheckable(False)
        self.registerButton.setObjectName("registerButton")
        self.label_3 = QtWidgets.QLabel(self.loginframe)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 81, 16))
        self.label_3.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.loginframe)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 101, 16))
        self.label_4.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_4.setObjectName("label_4")
        self.namaBox = QtWidgets.QLineEdit(self.loginframe)
        self.namaBox.setGeometry(QtCore.QRect(30, 130, 501, 41))
        self.namaBox.setStyleSheet("QLineEdit#namaBox{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.namaBox.setText("")
        self.namaBox.setObjectName("namaBox")
        self.label_5 = QtWidgets.QLabel(self.loginframe)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 81, 16))
        self.label_5.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.loginframe)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 81, 16))
        self.label_6.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_6.setObjectName("label_6")
        self.passwordBox = QtWidgets.QLineEdit(self.loginframe)
        self.passwordBox.setGeometry(QtCore.QRect(30, 270, 501, 41))
        self.passwordBox.setStyleSheet("QLineEdit#passwordBox{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.passwordBox.setText("")
        self.passwordBox.setObjectName("passwordBox")
        self.label_7 = QtWidgets.QLabel(self.loginframe)
        self.label_7.setGeometry(QtCore.QRect(30, 320, 101, 16))
        self.label_7.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_7.setObjectName("label_7")
        self.telpBox = QtWidgets.QLineEdit(self.loginframe)
        self.telpBox.setGeometry(QtCore.QRect(30, 340, 501, 41))
        self.telpBox.setStyleSheet("QLineEdit#telpBox{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.telpBox.setText("")
        self.telpBox.setObjectName("telpBox")
        self.label_8 = QtWidgets.QLabel(self.loginframe)
        self.label_8.setGeometry(QtCore.QRect(30, 390, 81, 21))
        self.label_8.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_8.setObjectName("label_8")
        self.addressBox = QtWidgets.QLineEdit(self.loginframe)
        self.addressBox.setGeometry(QtCore.QRect(30, 410, 501, 41))
        self.addressBox.setStyleSheet("QLineEdit#addressBox{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.addressBox.setText("")
        self.addressBox.setObjectName("addressBox")
        self.usernameBox = QtWidgets.QLineEdit(self.loginframe)
        self.usernameBox.setGeometry(QtCore.QRect(30, 200, 501, 41))
        self.usernameBox.setStyleSheet("QLineEdit#usernameBox{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.usernameBox.setText("")
        self.usernameBox.setObjectName("usernameBox")
        self.posBox = QtWidgets.QLineEdit(self.loginframe)
        self.posBox.setGeometry(QtCore.QRect(30, 480, 501, 41))
        self.posBox.setStyleSheet("QLineEdit#posBox{\n"
"    background-color: white;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
"}")
        self.posBox.setText("")
        self.posBox.setObjectName("posBox")
        self.label_9 = QtWidgets.QLabel(self.loginframe)
        self.label_9.setGeometry(QtCore.QRect(30, 460, 81, 21))
        self.label_9.setStyleSheet("font: 12pt \"Sansita\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.bgwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 110, 151, 31))
        self.label_10.setStyleSheet("font: 16pt \"Sansita\";")
        self.label_10.setObjectName("label_10")

        # Navigation bar
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
        self.berandaButton.setGeometry(QtCore.QRect(350, 35, 95, 40))
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
        self.tanamanButton.setGeometry(QtCore.QRect(525, 35, 110, 40))
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
        self.aboutButton.setGeometry(QtCore.QRect(710, 35, 150, 40))
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
        self.searchButton.setGeometry(QtCore.QRect(980, 40, 31, 31))
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
        self.userButton.setGeometry(QtCore.QRect(1030, 35, 31, 41))
        self.userButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("././img/User.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton.setIcon(icon1)
        self.userButton.setIconSize(QtCore.QSize(31, 41))
        self.userButton.setFlat(True)
        self.userButton.setObjectName("userButton")
        self.notification = QtWidgets.QLabel(self.navbar)
        self.notification.setGeometry(QtCore.QRect(1080, 40, 31, 31))
        self.notification.setText("")
        self.notification.setPixmap(QtGui.QPixmap("././img/Doorbell.png"))
        self.notification.setScaledContents(True)
        self.notification.setObjectName("notification")
        self.cartButton = QtWidgets.QPushButton(self.navbar)
        self.cartButton.setGeometry(QtCore.QRect(1130, 30, 31, 51))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.registerButton.setText(_translate("Dialog", "Daftar"))
        self.label_3.setText(_translate("Dialog", "Email"))
        self.label_4.setText(_translate("Dialog", "Nama Lengkap"))
        self.label_5.setText(_translate("Dialog", "Username"))
        self.label_6.setText(_translate("Dialog", "Password"))
        self.label_7.setText(_translate("Dialog", "Nomor Telepon"))
        self.label_8.setText(_translate("Dialog", "Alamat"))
        self.label_9.setText(_translate("Dialog", "Kode Pos"))
        self.label_10.setText(_translate("Dialog", "Form Registrasi"))
        self.berandaButton.setText(_translate("Dialog", "Beranda"))
        self.tanamanButton.setText(_translate("Dialog", "Tanaman"))
        self.aboutButton.setText(_translate("Dialog", "Tentang Kami"))

    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
