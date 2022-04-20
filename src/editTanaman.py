# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editTanaman.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import database.db_api as db_api
import Widgets

data = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola','Antigua & Deps',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize',
    'Benin', 'Bhutan', 'Bolivia', 'Bosnia Herzegovina', 'Botswana',
    'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon',
    'Canada', 'Cape Verde', 'Central African Rep', 'Chad', 'Chile', 'China',
    'Colombia', 'Comoros', 'Congo', 'Congo {Democratic Rep}', 'Costa Rica',
    'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti',
    'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt',
    'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
    'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany',
    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau',
    'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia',
    'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica',
    'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North',
    'Korea South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
    'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
    'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
    'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco',
    'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 
    'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan',
    'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
    'Poland', 'Portugal', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda',
    'St Kitts & Nevis', 'St Lucia', 'Saint Vincent & the Grenadines',
    'Samoa', 'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal',
    'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
    'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland',
    'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga',
    'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda',
    'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
    'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam',
    'Yemen', 'Zambia', 'Zimbabwe'
    ]

class UI_editTanaman(QtWidgets.QWidget):
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

        # Gambar Tanaman
        self.gambarTanaman = QtWidgets.QLabel(self.bgwidget)
        self.gambarTanaman.setGeometry(QtCore.QRect(80, 190, 231, 231))
        self.gambarTanaman.setText("")
        self.gambarTanaman.setPixmap(QtGui.QPixmap("././img/placeholderPlant.png"))
        self.gambarTanaman.setScaledContents(True)
        self.gambarTanaman.setObjectName("gambarTanaman")

        # Label Stok tanaman
        self.stokLabel = QtWidgets.QLabel(self.bgwidget)
        self.stokLabel.setGeometry(QtCore.QRect(360, 420, 200, 31))
        self.stokLabel.setStyleSheet("font: 16pt \"Sansita\";")
        self.stokLabel.setObjectName("stokLabel")

        # Label Harga tanaman
        self.hargaLabel = QtWidgets.QLabel(self.bgwidget)
        self.hargaLabel.setGeometry(QtCore.QRect(360, 460, 200, 31))
        self.hargaLabel.setStyleSheet("font: 16pt \"Sansita\";")
        self.hargaLabel.setObjectName("hargaLabel")

        # Label Domisili
        self.domisiliLabel = QtWidgets.QLabel(self.bgwidget)
        self.domisiliLabel.setGeometry(QtCore.QRect(360, 500, 200, 31))
        self.domisiliLabel.setStyleSheet("font: 16pt \"Sansita\";")
        self.domisiliLabel.setObjectName("domisiliLabel")

        # Label Edit (1)
        self.edit1Label = QtWidgets.QLabel(self.bgwidget)
        self.edit1Label.setGeometry(QtCore.QRect(725, 430, 21, 21))
        self.edit1Label.setText("")
        self.edit1Label.setPixmap(QtGui.QPixmap("././img/Edit.png"))
        self.edit1Label.setScaledContents(True)
        self.edit1Label.setObjectName("edit1Label")

        # Label Edit (2)
        self.edit2Label = QtWidgets.QLabel(self.bgwidget)
        self.edit2Label.setGeometry(QtCore.QRect(725, 470, 21, 21))
        self.edit2Label.setText("")
        self.edit2Label.setPixmap(QtGui.QPixmap("././img/Edit.png"))
        self.edit2Label.setScaledContents(True)
        self.edit2Label.setObjectName("edit2Label")

        # Label Edit (3)
        self.edit3Label = QtWidgets.QLabel(self.bgwidget)
        self.edit3Label.setGeometry(QtCore.QRect(725, 510, 21, 21))
        self.edit3Label.setText("")
        self.edit3Label.setPixmap(QtGui.QPixmap("././img/Edit.png"))
        self.edit3Label.setScaledContents(True)
        self.edit3Label.setObjectName("edit3Label")

        # Label Edit (4)
        self.edit4Label = QtWidgets.QLabel(self.bgwidget)
        self.edit4Label.setGeometry(QtCore.QRect(960, 350, 21, 21))
        self.edit4Label.setText("")
        self.edit4Label.setPixmap(QtGui.QPixmap("././img/Edit.png"))
        self.edit4Label.setScaledContents(True)
        self.edit4Label.setObjectName("edit4Label")

        # Label Edit (5)
        self.edit5Label = QtWidgets.QLabel(self.bgwidget)
        self.edit5Label.setGeometry(QtCore.QRect(210, 430, 21, 21))
        self.edit5Label.setText("")
        self.edit5Label.setPixmap(QtGui.QPixmap("././img/Edit.png"))
        self.edit5Label.setScaledContents(True)
        self.edit5Label.setObjectName("edit5Label")

        # Label Edit (6)
        self.edit6Label = QtWidgets.QLabel(self.bgwidget)
        self.edit6Label.setGeometry(QtCore.QRect(40, 140, 21, 21))
        self.edit6Label.setText("")
        self.edit6Label.setPixmap(QtGui.QPixmap("././img/Edit.png"))
        self.edit6Label.setScaledContents(True)
        self.edit6Label.setObjectName("edit6Label")

        # Button Simpan perubahan
        self.simpanPerubahanButton = QtWidgets.QPushButton(self.bgwidget)
        self.simpanPerubahanButton.setGeometry(QtCore.QRect(490, 590, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(11)
        self.simpanPerubahanButton.setFont(font)
        self.simpanPerubahanButton.setStyleSheet("QPushButton {\n"
"    \n"
"    border: 0px solid #555;\n"
"    border-radius: 8px;\n"
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
        self.simpanPerubahanButton.setCheckable(False)
        self.simpanPerubahanButton.setObjectName("simpanPerubahanButton")

        # Button Redirect
        self.RedirectButton = QtWidgets.QPushButton(self.bgwidget)
        self.RedirectButton.setGeometry(QtCore.QRect(8, 100, 75, 25))
        self.RedirectButton.setObjectName("RedirectButton")
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(9)
        self.RedirectButton.setFont(font)
        self.RedirectButton.setStyleSheet("QPushButton {\n"
"    \n"
"    border: 0px solid #555;\n"
"    border-radius: 8px;\n"
"    border-style: outset;\n"
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
        self.RedirectButton.setCheckable(False)
        self.RedirectButton.setText("< Kembali")
        self.RedirectButton.setObjectName("RedirectButton")

        # Upload File Button
        self.uploadFileButton = QtWidgets.QPushButton(self.bgwidget)
        self.uploadFileButton.setGeometry(QtCore.QRect(160, 420, 51, 41))
        self.uploadFileButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("././img/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadFileButton.setIcon(icon)
        self.uploadFileButton.setIconSize(QtCore.QSize(30, 30))
        self.uploadFileButton.setFlat(True)
        self.uploadFileButton.setObjectName("uploadFileButton")

        # Line Edit Nama
        self.namaEdit = QtWidgets.QLineEdit(self.bgwidget)
        self.namaEdit.setGeometry(QtCore.QRect(80, 120, 261, 51))
        font.setStrikeOut(False)
        font.setKerning(True)
        self.namaEdit.setStyleSheet("background-color: rgba(155,255,255,0);\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 22pt \"Sansita\";\n"
";")
        self.namaEdit.setFont(font)
        self.namaEdit.setObjectName("namaEdit")

        # Text Edit Deskripsi
        self.deskripsiEdit = QtWidgets.QLineEdit(self.bgwidget)
        self.deskripsiEdit.setGeometry(QtCore.QRect(360, 190, 581, 221))
        font = QtGui.QFont()
        font.setFamily("Sansita")
        font.setPointSize(16)
        self.deskripsiEdit.setFont(font)
        self.deskripsiEdit.setStyleSheet("background-color : #769D8A;")
        self.deskripsiEdit.setObjectName("deskripsiEdit")

        # Line Edit Stok
        self.stokEdit = QtWidgets.QLineEdit(self.bgwidget)
        self.stokEdit.setGeometry(QtCore.QRect(580, 420, 141, 31))
        self.stokEdit.setStyleSheet("background-color: #769D8A;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
";")
        self.stokEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.onlyInt = QtGui.QIntValidator()
        self.stokEdit.setValidator(self.onlyInt)
        self.stokEdit.setObjectName("stokEdit")

        # Line Edit Harga
        self.hargaEdit = QtWidgets.QLineEdit(self.bgwidget)
        self.hargaEdit.setGeometry(QtCore.QRect(580, 460, 141, 31))
        self.hargaEdit.setStyleSheet("background-color: #769D8A;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
";")
        self.hargaEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.hargaEdit.setValidator(self.onlyInt)
        self.hargaEdit.setObjectName("hargaEdit")

        # Line Edit Domisili
        self.domisiliEdit = QtWidgets.QLineEdit(self.bgwidget)
        self.domisiliEdit.setGeometry(QtCore.QRect(580, 500, 141, 31))
        self.domisiliEdit.setStyleSheet("background-color: #769D8A;\n"
"    border: 0px solid #555;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    font: 12pt \"Sansita\";\n"
";")
        self.domisiliEdit.setAlignment(QtCore.Qt.AlignCenter)
        completer = QtWidgets.QCompleter(data)
        self.domisiliEdit.setCompleter(completer)
        self.domisiliEdit.setObjectName("domisiliEdit")


        self.domisiliEdit.raise_()
        self.hargaEdit.raise_()
        self.navbar.raise_()
        self.gambarTanaman.raise_()
        self.stokLabel.raise_()
        self.hargaLabel.raise_()
        self.domisiliLabel.raise_()
        self.edit1Label.raise_()
        self.edit2Label.raise_()
        self.edit3Label.raise_()
        self.edit4Label.raise_()
        self.edit5Label.raise_()
        self.edit6Label.raise_()
        self.simpanPerubahanButton.raise_()
        self.uploadFileButton.raise_()
        self.namaEdit.raise_()
        self.deskripsiEdit.raise_()
        self.stokEdit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.berandaButton.setText(_translate("Dialog", "Beranda"))
        self.tanamanButton.setText(_translate("Dialog", "Tanaman"))
        self.aboutButton.setText(_translate("Dialog", "Tentang Kami"))
        self.stokLabel.setText(_translate("Dialog", "Stok Tanaman"))
        self.hargaLabel.setText(_translate("Dialog", "Harga Tanaman "))
        self.domisiliLabel.setText(_translate("Dialog", "Domisili Tanaman"))
        self.simpanPerubahanButton.setText(_translate("Dialog", "Simpan Perubahan"))
        self.uploadFileButton.clicked.connect(self.pushButton_handler)
        self.namaEdit.setText(_translate("Dialog", "Nama Tanaman"))
        self.deskripsiEdit.setText(_translate("Dialog", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))
        self.stokEdit.setText(_translate("Dialog", "Stok"))
        self.hargaEdit.setText(_translate("Dialog", "Harga"))
        self.domisiliEdit.setText(_translate("Dialog", "Domisili"))

    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.gambarTanaman.setPixmap(QtGui.QPixmap(self.path))
        # Ganti pathnya 
    
    def handleSubmit(self, conn):
        print(self.tanamanId)
        nama = self.namaEdit.text()
        deskripsi = self.deskripsiEdit.text()
        stok = self.stokEdit.text()
        harga = self.hargaEdit.text()
        domisili = self.domisiliEdit.text()
        print(nama)
        if(self.path is not None):
            image = db_api.convertToBinaryData(self.path)
        else:
            image = self.data[5]
        if nama == "" or deskripsi == "" or stok == "" or harga == "" or domisili == "":
            Widgets.messageBoxEditTanamanGagal()
            print("Gagal mengedit tanaman")
        else:
            db_api.editTanaman(conn, self.data[0], nama, harga, stok, deskripsi, image, domisili)
            Widgets.messageBoxEditTanamanBerhasil(nama)
            print("Edit tanaman berhasil")

    def __init__(self, data, conn):
        super(QtWidgets.QWidget, self).__init__()
        self.tanamanId = data[0]
        self.data = data
        self.path = None
        self.setupUi(self)
        self.namaEdit.setText(data[1])
        self.deskripsiEdit.setText(data[4])
        self.hargaEdit.setText(str(data[2]))
        self.stokEdit.setText(str(data[3]))
        self.domisiliEdit.setText(data[6])
        if(data[5] is not None):
            pm = QtGui.QPixmap()
            pm.loadFromData(data[5])
            self.gambarTanaman.setPixmap(pm)
        self.simpanPerubahanButton.clicked.connect(lambda: self.handleSubmit(conn))

if __name__ == "__main__":
    import sys
    dummy = (1, 'Dummy', 100000, 10, "Dummy data", None, "Jakarta")
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UI_editTanaman(dummy)
    ui.setupUi(Dialog)
    ui.__init__(dummy)
    Dialog.show()
    sys.exit(app.exec_())
