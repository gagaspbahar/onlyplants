# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomescreen.ui'
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
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.bgwidget.setMinimumSize(QtCore.QSize(1200, 800))
        self.bgwidget.setMaximumSize(QtCore.QSize(1200, 800))
        self.bgwidget.setAutoFillBackground(False)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
                                    "background-color: rgb(234, 216, 202);}")
        self.bgwidget.setObjectName("bgwidget")
        self.WelcomeTo = QtWidgets.QLabel(self.bgwidget)
        self.WelcomeTo.setGeometry(QtCore.QRect(440, 200, 321, 101))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.WelcomeTo.setFont(font)
        self.WelcomeTo.setStyleSheet("font: 87 40pt \"Sansita\";\n"
                                     "color : rgb(0, 0, 0) ")
        self.WelcomeTo.setScaledContents(False)
        self.WelcomeTo.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeTo.setWordWrap(False)
        self.WelcomeTo.setObjectName("WelcomeTo")
        self.Logo = QtWidgets.QLabel(self.bgwidget)
        self.Logo.setGeometry(QtCore.QRect(440, 300, 371, 111))
        self.Logo.setStyleSheet("font: 87 26pt \"Sansita\";\n"
                                "color : rgb(0, 0, 0) ")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("././img/logo.png"))
        self.Logo.setScaledContents(False)
        self.Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo.setObjectName("Logo")
        self.registerButton = QtWidgets.QPushButton(self.bgwidget)
        self.registerButton.setGeometry(QtCore.QRect(440, 420, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(11)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {\n"
                                        "    \n"
                                        "    border: 2px solid #555;\n"
                                        "    border-radius: 15px;\n"
                                        "    border-style: outset;\n"
                                        "    background-color : rgb(136, 179, 160);\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    color : white;\n"
                                        "     background-color : rgb(85, 170, 127);\n"
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
        #when clicked open register window
        self.loginButton = QtWidgets.QPushButton(self.bgwidget)
        self.loginButton.setGeometry(QtCore.QRect(630, 420, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.loginButton.setMouseTracking(False)
        self.loginButton.setStyleSheet("QPushButton {\n"
                                    "    \n"
                                    "    border: 2px solid #555;\n"
                                    "    border-radius: 15px;\n"
                                    "    border-style: outset;\n"
                                    "    background-color : rgb(136, 179, 160);\n"
                                    "    padding: 5px;\n"
                                    "    }\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    color : white;\n"
                                    "     background-color : rgb(85, 170, 127)\n"
                                    "    }\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    border-style: inset;\n"
                                    "    background: qradialgradient(\n"
                                    "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                    "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                    "        );\n"
                                    "    }")
        self.loginButton.setCheckable(False)
        self.loginButton.setObjectName("loginButton")
        # when login button is clicked open login window
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(750, 180, 531, 721))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 87 40pt \"Sansita\";\n"
                                "color : rgb(0, 0, 0) ")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("././img/mumei.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(0, -40, 321, 671))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 87 40pt \"Sansita\";\n"
                                "color : rgb(0, 0, 0) ")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("././img/vertVines.png"))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.WelcomeTo.setText(_translate("Dialog", "Welcome To "))
        self.registerButton.setText(_translate("Dialog", "Register"))
        self.loginButton.setText(_translate("Dialog", "Login"))
    
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
