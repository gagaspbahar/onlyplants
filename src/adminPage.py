# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UI_adminPage(QtWidgets.QWidget):
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

        # Button add tanaman
        self.addTanaman = QtWidgets.QPushButton(self.bgwidget)
        self.addTanaman.setGeometry(QtCore.QRect(140, 310, 371, 201))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(14)
        self.addTanaman.setFont(font)
        self.addTanaman.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 8px;\n"
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
        self.addTanaman.setCheckable(False)
        self.addTanaman.setObjectName("addTanaman")
        
        # Button edit tanaman
        self.editTanaman = QtWidgets.QPushButton(self.bgwidget)
        self.editTanaman.setGeometry(QtCore.QRect(700, 310, 371, 201))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(14)
        self.editTanaman.setFont(font)
        self.editTanaman.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 8px;\n"
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
        self.editTanaman.setCheckable(False)
        self.editTanaman.setObjectName("editTanaman")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.berandaButton.setText(_translate("Dialog", "Beranda"))
        self.tanamanButton.setText(_translate("Dialog", "Tanaman"))
        self.aboutButton.setText(_translate("Dialog", "Tentang Kami"))
        self.addTanaman.setText(_translate("Dialog", "Tambahkan Tanaman"))
        self.editTanaman.setText(_translate("Dialog", "Edit Tanaman"))

    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UI_adminPage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
