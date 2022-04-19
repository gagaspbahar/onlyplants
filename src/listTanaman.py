# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listTanaman.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):
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

        # Gambar 1
        self.gambar1 = QtWidgets.QLabel(self.bgwidget)
        self.gambar1.setGeometry(QtCore.QRect(100, 150, 240, 240))
        self.gambar1.setText("")
        self.gambar1.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.gambar1.setScaledContents(True)
        self.gambar1.setObjectName("gambar1")

        # Gambar 2
        self.gambar2 = QtWidgets.QLabel(self.bgwidget)
        self.gambar2.setGeometry(QtCore.QRect(480, 150, 240, 240))
        self.gambar2.setText("")
        self.gambar2.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.gambar2.setScaledContents(True)
        self.gambar2.setObjectName("gambar2")

        # Gambar 3
        self.gambar3 = QtWidgets.QLabel(self.bgwidget)
        self.gambar3.setGeometry(QtCore.QRect(850, 150, 240, 240))
        self.gambar3.setText("")
        self.gambar3.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.gambar3.setScaledContents(True)
        self.gambar3.setObjectName("gambar3")

        # Gambar 4
        self.gambar4 = QtWidgets.QLabel(self.bgwidget)
        self.gambar4.setGeometry(QtCore.QRect(100, 460, 240, 240))
        self.gambar4.setText("")
        self.gambar4.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.gambar4.setScaledContents(True)
        self.gambar4.setObjectName("gambar4")

        # Gambar 5
        self.gambar5 = QtWidgets.QLabel(self.bgwidget)
        self.gambar5.setGeometry(QtCore.QRect(480, 460, 240, 240))
        self.gambar5.setText("")
        self.gambar5.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.gambar5.setScaledContents(True)
        self.gambar5.setObjectName("gambar5")

        # Gambar 6
        self.gambar6 = QtWidgets.QLabel(self.bgwidget)
        self.gambar6.setGeometry(QtCore.QRect(850, 460, 240, 240))
        self.gambar6.setText("")
        self.gambar6.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.gambar6.setScaledContents(True)
        self.gambar6.setObjectName("gambar6")

        # Label Kiri
        self.kiri = QtWidgets.QPushButton(self.bgwidget)
        self.kiri.setGeometry(QtCore.QRect(25, 410, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(40)
        self.kiri.setFont(font)
        self.kiri.setAutoFillBackground(False)
        self.kiri.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    text-align: center;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : #B1B6AF;\n"
"    }")
        self.kiri.setCheckable(False)
        self.kiri.setObjectName("kiri")

        # Label Kanan
        self.kanan = QtWidgets.QPushButton(self.bgwidget)
        self.kanan.setGeometry(QtCore.QRect(1125, 410, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(40)
        self.kanan.setFont(font)
        self.kanan.setAutoFillBackground(False)
        self.kanan.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    text-align: center;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : #B1B6AF;\n"
"    }")
        self.kanan.setCheckable(False)
        self.kanan.setObjectName("kanan")

        # Label 1
        self.tanaman1 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman1.setGeometry(QtCore.QRect(100, 400, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman1.setFont(font)
        self.tanaman1.setAutoFillBackground(False)
        self.tanaman1.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    text-align: center;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : #B1B6AF;\n"
"    }")
        self.tanaman1.setCheckable(False)
        self.tanaman1.setObjectName("tanaman1")

        # Label 2
        self.tanaman2 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman2.setGeometry(QtCore.QRect(480, 400, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman2.setFont(font)
        self.tanaman2.setAutoFillBackground(False)
        self.tanaman2.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    text-align: center;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : #B1B6AF;\n"
"    }")
        self.tanaman2.setCheckable(False)
        self.tanaman2.setObjectName("tanaman2")

        # Label 3
        self.tanaman3 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman3.setGeometry(QtCore.QRect(850, 400, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman3.setFont(font)
        self.tanaman3.setAutoFillBackground(False)
        self.tanaman3.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    text-align: center;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : #B1B6AF;\n"
"    }")
        self.tanaman3.setCheckable(False)
        self.tanaman3.setObjectName("tanaman3")

        # Label 4
        self.tanaman4 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman4.setGeometry(QtCore.QRect(100, 710, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman4.setFont(font)
        self.tanaman4.setAutoFillBackground(False)
        self.tanaman4.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    text-align: center;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : #B1B6AF;\n"
"    }")
        self.tanaman4.setCheckable(False)
        self.tanaman4.setObjectName("tanaman4")

        # Label 5
        self.tanaman5 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman5.setGeometry(QtCore.QRect(480, 710, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman5.setFont(font)
        self.tanaman5.setAutoFillBackground(False)
        self.tanaman5.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    text-align: center;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : #B1B6AF;\n"
"    }")
        self.tanaman5.setCheckable(False)
        self.tanaman5.setObjectName("tanaman5")

        # Label 6
        self.tanaman6 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman6.setGeometry(QtCore.QRect(850, 710, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman6.setFont(font)
        self.tanaman6.setAutoFillBackground(False)
        self.tanaman6.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : #B1B6AF;\n"
"    }")
        self.tanaman6.setCheckable(False)
        self.tanaman6.setObjectName("tanaman6")

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
        
        self.kiri.raise_()
        self.kanan.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tanamanButton.setText(_translate("Dialog", "Tanaman"))
        self.aboutButton.setText(_translate("Dialog", "Tentang Kami"))
        self.berandaButton.setText(_translate("Dialog", "Beranda"))
        self.kiri.setText(_translate("Dialog", "<"))
        self.kanan.setText(_translate("Dialog", ">"))
        self.tanaman1.setText(_translate("Dialog", "Nama Tanaman 1"))
        self.tanaman2.setText(_translate("Dialog", "Nama Tanaman 2"))
        self.tanaman3.setText(_translate("Dialog", "Nama Tanaman 3"))
        self.tanaman4.setText(_translate("Dialog", "Nama Tanaman 4"))
        self.tanaman5.setText(_translate("Dialog", "Nama Tanaman 5"))
        self.tanaman6.setText(_translate("Dialog", "Nama Tanaman 6"))

    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
