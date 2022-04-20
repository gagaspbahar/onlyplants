# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/checkout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import time
from PyQt5 import QtCore, QtGui, QtWidgets
from modalItemKeranjang import Ui_Form
from modalPesananBerlangsung import modalPesananBerlangsung
import database.db_api as db_api

class Ui_Checkout(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        Form.setMinimumSize(QtCore.QSize(1200, 800))
        Form.setMaximumSize(QtCore.QSize(1200, 800))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet("background: #FFFFFF;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1181, 920))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_2.setStyleSheet("background: #88B3A0;\n"
"border-bottom-left-radius: 8px ;\n"
"border-bottom-right-radius: 8px ;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setMaximumSize(QtCore.QSize(1060, 5))
        self.line_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_2.setStyleSheet("/* Line 1 */\n"
"\n"
"position: absolute;\n"
"width: 1240px;\n"
"height: 0px;\n"
"left: 25px;\n"
"top: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.totalHarga = QtWidgets.QLabel(self.widget_2)
        self.totalHarga.setMinimumSize(QtCore.QSize(0, 50))
        self.totalHarga.setMaximumSize(QtCore.QSize(16777215, 50))
        self.totalHarga.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.totalHarga.setStyleSheet("/* Order ID : XXXXXXX */\n"
"\n"
"position: absolute;\n"
"width: 151px;\n"
"height: 24px;\n"
"left: 1104px;\n"
"top: 16px;\n"
"\n"
"font-family: \'Sansita\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"/* identical to box height */\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.totalHarga.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalHarga.setObjectName("totalHarga")
        self.verticalLayout_3.addWidget(self.totalHarga)
        self.gridLayout.addWidget(self.widget_2, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setMinimumSize(QtCore.QSize(275, 30))
        self.label_10.setMaximumSize(QtCore.QSize(276, 30))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("/* Rectangle 3 */\n"
"\n"
"position: absolute;\n"
"width: 342px;\n"
"height: 25px;\n"
"left: 80px;\n"
"top: 227px;\n"
"\n"
"background: #B1B6AF;\n"
"border-radius: 8px;\n"
"\n"
"\n"
"/* Daftar cartButton Pemesanan */\n"
"\n"
"position: absolute;\n"
"width: 236px;\n"
"height: 24px;\n"
"left: 144px;\n"
"top: 228px;\n"
"\n"
"font-family: \'Sansita\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 24px;\n"
"/* identical to box height */\n"
"\n"
"color: #000000;")
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 1, 1, 1)
        
        # Navigation Bar
        self.navbar = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.navbar.setMinimumSize(QtCore.QSize(0, 91))
        self.navbar.setMaximumSize(QtCore.QSize(16777215, 91))
        self.navbar.setStyleSheet("QFrame#navbar{\n"
"    background-color: rgb(234, 216, 202);\n"
"   \n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}")
        self.navbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navbar.setObjectName("navbar")
        
        self.Logo = QtWidgets.QLabel(self.navbar)
        self.Logo.setGeometry(QtCore.QRect(0, 0, 281, 121))
        self.Logo.setStyleSheet("font: 87 26pt \"Sansita\";\n"
"background-color : transparent ")
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
        self.frame_2 = QtWidgets.QFrame(self.navbar)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1181, 21))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"    background-color: rgb(136, 179, 160);\n"
"   \n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.search = QtWidgets.QPushButton(self.navbar)
        self.search.setGeometry(QtCore.QRect(980, 40, 31, 31))
        self.search.setMouseTracking(False)
        self.search.setAutoFillBackground(False)
        self.search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("././img/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon)
        self.search.setAutoDefault(True)
        self.search.setDefault(False)
        self.search.setFlat(True)
        self.search.setObjectName("search")
        self.userButton = QtWidgets.QPushButton(self.navbar)
        self.userButton.setGeometry(QtCore.QRect(1030, 35, 31, 41))
        self.userButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("././img/User.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton.setIcon(icon1)
        self.userButton.setIconSize(QtCore.QSize(30, 30))
        self.userButton.setFlat(True)
        self.userButton.setObjectName("userButton")
        self.notification = QtWidgets.QPushButton(self.navbar)
        self.notification.setGeometry(QtCore.QRect(1080, 40, 31, 31))
        self.notification.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("././img/Doorbell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notification.setIcon(icon2)
        self.notification.setIconSize(QtCore.QSize(30, 30))
        self.notification.setAutoDefault(True)
        self.notification.setFlat(True)
        self.notification.setObjectName("notification")
        self.cartButton = QtWidgets.QPushButton(self.navbar)
        self.cartButton.setGeometry(QtCore.QRect(1130, 30, 31, 51))
        self.cartButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("././img/Shopping Cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cartButton.setIcon(icon3)
        self.cartButton.setIconSize(QtCore.QSize(40, 40))
        self.cartButton.setAutoExclusive(False)
        self.cartButton.setAutoDefault(True)
        self.cartButton.setFlat(True)
        self.cartButton.setObjectName("cartButton")

        self.gridLayout.addWidget(self.navbar, 0, 0, 1, 3)
        self.widget_9 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_9.setMinimumSize(QtCore.QSize(100, 20))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget_9.setObjectName("widget_9")
        self.gridLayout.addWidget(self.widget_9, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.konfirmasiPengajuan = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.konfirmasiPengajuan.setMinimumSize(QtCore.QSize(344, 30))
        self.konfirmasiPengajuan.setMaximumSize(QtCore.QSize(344, 30))
        self.konfirmasiPengajuan.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.konfirmasiPengajuan.setStyleSheet("/* Frame 4 */\n"
"QPushButton {\n"
"position: absolute;\n"
"width: 351px;\n"
"height: 45px;\n"
"left: 1014px;\n"
"top: 976px;\n"
"\n"
"background: #769D8A;\n"
"border-radius: 8px;\n"
"\n"
"\n"
"/* Konfirmasi Pengajuan Penyewaan */\n"
"\n"
"position: absolute;\n"
"width: 273px;\n"
"height: 24px;\n"
"left: 39px;\n"
"top: 11px;\n"
"\n"
"font-family: \'Sansita\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"/* identical to box height */\n"
"\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color : black;\n"
"}\n"
"\n"
"")
        self.konfirmasiPengajuan.setDefault(False)
        self.konfirmasiPengajuan.setObjectName("konfirmasiPengajuan")
        self.gridLayout.addWidget(self.konfirmasiPengajuan, 7, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 5, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setStyleSheet("/* Pesanan Anda */\n"
"\n"
"position: absolute;\n"
"width: 170px;\n"
"height: 36px;\n"
"left: 74px;\n"
"top: 174px;\n"
"\n"
"font-family: \'Sansita\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 36px;\n"
"/* identical to box height */\n"
"\n"
"color: #000000;\n"
"\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(275, 30))
        self.label_5.setMaximumSize(QtCore.QSize(276, 30))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("/* Rectangle 3 */\n"
"\n"
"position: absolute;\n"
"width: 342px;\n"
"height: 25px;\n"
"left: 80px;\n"
"top: 227px;\n"
"\n"
"background: #B1B6AF;\n"
"border-radius: 8px;\n"
"\n"
"\n"
"/* Daftar cartButton Pemesanan */\n"
"\n"
"position: absolute;\n"
"width: 236px;\n"
"height: 24px;\n"
"left: 144px;\n"
"top: 228px;\n"
"\n"
"font-family: \'Sansita\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 24px;\n"
"/* identical to box height */\n"
"\n"
"color: #000000;")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.slotPesananBerlangsung = QtWidgets.QVBoxLayout()
        self.slotPesananBerlangsung.setObjectName("slotPesananBerlangsung")
        self.gridLayout.addLayout(self.slotPesananBerlangsung, 10, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 75))
        self.widget.setStyleSheet("background: #88B3A0;\n"
"border-top-left-radius: 8px ;\n"
"border-top-right-radius: 8px ;")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.namacartButton = QtWidgets.QWidget(self.widget)
        self.namacartButton.setMinimumSize(QtCore.QSize(0, 40))
        self.namacartButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.namacartButton.setObjectName("namacartButton")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.namacartButton)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.namaItem = QtWidgets.QLabel(self.namacartButton)
        self.namaItem.setStyleSheet("/* Order ID : XXXXXXX */\n"
"\n"
"position: absolute;\n"
"width: 151px;\n"
"height: 24px;\n"
"left: 1104px;\n"
"top: 16px;\n"
"\n"
"font-family: \'Sansita\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"/* identical to box height */\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.namaItem.setObjectName("namaItem")
        self.horizontalLayout_6.addWidget(self.namaItem)
        self.orderId = QtWidgets.QLabel(self.namacartButton)
        self.orderId.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.orderId.setBaseSize(QtCore.QSize(10000, 0))
        self.orderId.setStyleSheet("/* Order ID : XXXXXXX */\n"
"\n"
"position: absolute;\n"
"width: 151px;\n"
"height: 24px;\n"
"left: 1104px;\n"
"top: 16px;\n"
"\n"
"font-family: \'Sansita\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 20px;\n"
"line-height: 24px;\n"
"/* identical to box height */\n"
"\n"
"color: #000000;\n"
"\n"
"")
        self.orderId.setObjectName("orderId")
        self.horizontalLayout_6.addWidget(self.orderId)
        self.verticalLayout_2.addWidget(self.namacartButton)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setMinimumSize(QtCore.QSize(1068, 0))
        self.line.setMaximumSize(QtCore.QSize(1068, 5))
        self.line.setStyleSheet("/* Line 1 */\n"
"\n"
"position: absolute;\n"
"width: 1240px;\n"
"height: 0px;\n"
"left: 25px;\n"
"top: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollArea_2.setStyleSheet("background: #88B3A0;\n")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1090, 500))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 3, 1, 1, 1)
        self.widget_10 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_10.setMinimumSize(QtCore.QSize(100, 20))
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget_10.setObjectName("widget_10")
        self.gridLayout.addWidget(self.widget_10, 9, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.totalHarga.setText(_translate("Form", "Total Harga: Rp 3.000.000,-"))
        self.label_10.setText(_translate("Form", "Pesanan yang Sedang Berlangsung"))
        self.berandaButton.setText(_translate("Form", "Beranda"))
        self.tanamanButton.setText(_translate("Form", "Tanaman"))
        self.aboutButton.setText(_translate("Form", "Tentang Kami"))
        self.konfirmasiPengajuan.setText(_translate("Form", "Konfirmasi Pengajuan Sewa"))
        self.label.setText(_translate("Form", "Pesanan Anda"))
        self.label_5.setText(_translate("Form", "Daftar Keranjang Pemesanan"))
        self.namaItem.setText(_translate("Form", "Nama Item"))
        self.orderId.setText(_translate("Form", "Order Id: "))
        
#     def adjustScrollArea_handler(self, event: QtGui.QMouseEvent) -> None:
#         event.accept()
#         print("terjadi")
#         if self.verticalLayout_6 is not None:
#                 QtCore.QTimer.singleShot(0, self.scrollArea_2.adjustSize).
        
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        self.setupUi(self)

    def inisial(self, conn, idPelanggan):
            currentOrderNumber = db_api.getOrderTableLength(conn) - 1
            self.removeIsiKeranjang()
            self.removePesananWidgets()
            # self.handleAddKeranjang(conn, currentOrderNumber)
            self.handleAddPesanan(conn, idPelanggan)
            
    def handleAddKeranjang(self, conn, orderNumber):
                db_api.viewKeranjang(conn)
                listItem = db_api.getKeranjang(conn, orderNumber)
                totalPrice = 0
                count = 1
                orderID = 0
                for description in listItem:
                        keranjang = Ui_Form()
                        FormKeranjang = QtWidgets.QWidget()
                        descrip = list(description)
                        orderID = descrip[1]
                        keranjang.setupUi(FormKeranjang)
                        keranjang.setDescription(FormKeranjang, count,descrip[2], descrip[3], descrip[4], descrip[5], descrip[6])
                        count+=1
                        totalPrice += descrip[6]
                        self.verticalLayout_6.addWidget(FormKeranjang)
                self.totalHarga.setText("Total Harga: Rp" + str(totalPrice))
                self.orderId.setText("Order Id: "+ str(orderID))

    def handleAddPesanan(self, conn, idPelanggan):
                listPesanan = db_api.getPesananAktif(conn, idPelanggan)
                for orders in listPesanan:
                        pesanan = modalPesananBerlangsung()
                        ord = list(orders)
                        FormPesanan = QtWidgets.QWidget()
                        pesanan.setupUi(FormPesanan)
                        pesanan.OrderID.setText("Order Number: "+ str(ord[1]))
                        self.slotPesananBerlangsung.addWidget(FormPesanan)
            
    def konfirmasiPesanan_handler(self, conn, orderNumber, idPelanggan):
                self.removeIsiKeranjang()
                self.removePesananWidgets()
                db_api.updateStatus(conn, orderNumber, "waiting for approval")
                self.handleAddPesanan(conn, idPelanggan)
        
    def removePesananWidgets(self):
        try:    
                if (self.slotPesananBerlangsung is not None):  
                        while (self.slotPesananBerlangsung.count()):
                                child = self.slotPesananBerlangsung.takeAt(0)
                                if child.widget() is not None:
                                        child.widget().deleteLater()
            
        except:
                print("remove from pesanan totally failed, hope it works")
                
    def removeIsiKeranjang(self):
        try:    
                if (self.verticalLayout_6 is not None):  
                        while (self.verticalLayout_6.count()):
                                child = self.verticalLayout_6.takeAt(0)
                                if child.widget() is not None:
                                        child.widget().deleteLater()
                self.orderId.setText("Order Id : -")
                self.totalHarga.setText("Total Harga: Rp 0")
        except:
                print("remove from keranjang totally failed, hope it works")
if __name__ == "__main__":
        
        database = r".\src\database\onlyplants.db"
        conn = db_api.create_connection(database)
        currentOrderNumber = db_api.getOrderTableLength(conn)
        db_api.viewPemesanan(conn)
        db_api.viewPesananAktif(conn)
        db_api.viewKeranjang(conn)

        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Checkout()
        ui.setupUi(Form)
        ui.handleAddKeranjang(conn, currentOrderNumber)
        ui.konfirmasiPengajuan.clicked.connect(lambda: ui.konfirmasiPesanan_handeler(conn,1,1))
        Form.show()
        sys.exit(app.exec_())
