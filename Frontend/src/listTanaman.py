# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listTanaman.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 240, 240))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 150, 240, 240))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(850, 150, 240, 240))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 460, 240, 240))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.bgwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 460, 240, 240))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.bgwidget)
        self.label_8.setGeometry(QtCore.QRect(850, 460, 240, 240))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
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
        self.Logo_4 = QtWidgets.QLabel(self.navbar)
        self.Logo_4.setGeometry(QtCore.QRect(0, 0, 281, 121))
        self.Logo_4.setStyleSheet("font: 87 26pt \"Sansita\";\n"
"color : rgb(0, 0, 0) ")
        self.Logo_4.setText("")
        self.Logo_4.setPixmap(QtGui.QPixmap("././img/logo.png"))
        self.Logo_4.setScaledContents(True)
        self.Logo_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo_4.setObjectName("Logo_4")
        self.tanamanButton_4 = QtWidgets.QPushButton(self.navbar)
        self.tanamanButton_4.setGeometry(QtCore.QRect(520, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.tanamanButton_4.setFont(font)
        self.tanamanButton_4.setStyleSheet("QPushButton {\n"
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
        self.tanamanButton_4.setCheckable(False)
        self.tanamanButton_4.setObjectName("tanamanButton_4")
        self.aboutButton_4 = QtWidgets.QPushButton(self.navbar)
        self.aboutButton_4.setGeometry(QtCore.QRect(670, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.aboutButton_4.setFont(font)
        self.aboutButton_4.setStyleSheet("QPushButton {\n"
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
        self.aboutButton_4.setCheckable(False)
        self.aboutButton_4.setObjectName("aboutButton_4")
        self.searchButton_3 = QtWidgets.QPushButton(self.navbar)
        self.searchButton_3.setGeometry(QtCore.QRect(930, 40, 31, 31))
        self.searchButton_3.setMouseTracking(False)
        self.searchButton_3.setAutoFillBackground(False)
        self.searchButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("././img/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton_3.setIcon(icon)
        self.searchButton_3.setIconSize(QtCore.QSize(31, 31))
        self.searchButton_3.setAutoDefault(True)
        self.searchButton_3.setDefault(False)
        self.searchButton_3.setFlat(True)
        self.searchButton_3.setObjectName("searchButton_3")
        self.userButton_3 = QtWidgets.QPushButton(self.navbar)
        self.userButton_3.setGeometry(QtCore.QRect(980, 35, 31, 41))
        self.userButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("././img/User.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton_3.setIcon(icon1)
        self.userButton_3.setIconSize(QtCore.QSize(31, 41))
        self.userButton_3.setFlat(True)
        self.userButton_3.setObjectName("userButton_3")
        self.cartButton_3 = QtWidgets.QPushButton(self.navbar)
        self.cartButton_3.setGeometry(QtCore.QRect(1080, 30, 31, 51))
        self.cartButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("././img/Shopping Cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("././img/Shopping Cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cartButton_3.setIcon(icon2)
        self.cartButton_3.setIconSize(QtCore.QSize(31, 51))
        self.cartButton_3.setAutoExclusive(False)
        self.cartButton_3.setAutoDefault(True)
        self.cartButton_3.setFlat(True)
        self.cartButton_3.setObjectName("cartButton_3")
        self.notification_4 = QtWidgets.QLabel(self.navbar)
        self.notification_4.setGeometry(QtCore.QRect(1030, 40, 31, 31))
        self.notification_4.setText("")
        self.notification_4.setPixmap(QtGui.QPixmap("././img/Doorbell.png"))
        self.notification_4.setScaledContents(True)
        self.notification_4.setObjectName("notification_4")
        self.berandaButton = QtWidgets.QPushButton(self.navbar)
        self.berandaButton.setGeometry(QtCore.QRect(370, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(15)
        self.berandaButton.setFont(font)
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
        self.tanaman1 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman1.setGeometry(QtCore.QRect(150, 400, 141, 31))
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
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : blue;\n"
"    }")
        self.tanaman1.setCheckable(False)
        self.tanaman1.setObjectName("tanaman1")
        self.tanaman1_2 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman1_2.setGeometry(QtCore.QRect(530, 400, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman1_2.setFont(font)
        self.tanaman1_2.setAutoFillBackground(False)
        self.tanaman1_2.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : blue;\n"
"    }")
        self.tanaman1_2.setCheckable(False)
        self.tanaman1_2.setObjectName("tanaman1_2")
        self.tanaman1_3 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman1_3.setGeometry(QtCore.QRect(900, 400, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman1_3.setFont(font)
        self.tanaman1_3.setAutoFillBackground(False)
        self.tanaman1_3.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : blue;\n"
"    }")
        self.tanaman1_3.setCheckable(False)
        self.tanaman1_3.setObjectName("tanaman1_3")
        self.tanaman1_4 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman1_4.setGeometry(QtCore.QRect(150, 710, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman1_4.setFont(font)
        self.tanaman1_4.setAutoFillBackground(False)
        self.tanaman1_4.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : blue;\n"
"    }")
        self.tanaman1_4.setCheckable(False)
        self.tanaman1_4.setObjectName("tanaman1_4")
        self.tanaman1_5 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman1_5.setGeometry(QtCore.QRect(530, 710, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman1_5.setFont(font)
        self.tanaman1_5.setAutoFillBackground(False)
        self.tanaman1_5.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : blue;\n"
"    }")
        self.tanaman1_5.setCheckable(False)
        self.tanaman1_5.setObjectName("tanaman1_5")
        self.tanaman1_6 = QtWidgets.QPushButton(self.bgwidget)
        self.tanaman1_6.setGeometry(QtCore.QRect(900, 710, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.tanaman1_6.setFont(font)
        self.tanaman1_6.setAutoFillBackground(False)
        self.tanaman1_6.setStyleSheet("QPushButton {\n"
"    border: 0px solid #555;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    color : black;\n"
"    background-color :  white;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color : blue;\n"
"    }")
        self.tanaman1_6.setCheckable(False)
        self.tanaman1_6.setObjectName("tanaman1_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tanamanButton_4.setText(_translate("Dialog", "Tanaman"))
        self.aboutButton_4.setText(_translate("Dialog", "Tentang Kami"))
        self.berandaButton.setText(_translate("Dialog", "Beranda"))
        self.tanaman1.setText(_translate("Dialog", "Nama Tanaman"))
        self.tanaman1_2.setText(_translate("Dialog", "Nama Tanaman"))
        self.tanaman1_3.setText(_translate("Dialog", "Nama Tanaman"))
        self.tanaman1_4.setText(_translate("Dialog", "Nama Tanaman"))
        self.tanaman1_5.setText(_translate("Dialog", "Nama Tanaman"))
        self.tanaman1_6.setText(_translate("Dialog", "Nama Tanaman"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
