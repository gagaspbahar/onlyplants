from email import message
import database.db_api as db_api
import welcomescreen
import login
import register
import landingPage
import listTanaman
import adminPage
import addTanaman
import editTanaman
import greetingAdmin
import greetingUser
import aboutUs
import modalLoginRegistrasi
import checkout
import sys
import Widgets

from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets

global LoggedInID
global isAdmin
LoggedInID = 0
isAdmin = False

facts = ["Seorang peneliti asal Jerman, Peter Wohlleben, menemukan fakta unik bahwa ternyata pohon mempunyai perasaan, bisa berteman, dan saling menyayangi seperti halnya manusia lho Squad. Peter mengatakan bahwa pohon dapat merasakan sakit dan emosi seperti rasa takut. Pohon juga memiliki ikatan yang kuat layaknya pasangan manusia dan lebih senang jika tumbuh berdekatan serta saling bersentuhan. Hasil penelitian unik ini bisa kamu tonton di sebuah film dokumenter bernama ‘Intelligent Trees’. Tertarik?",
"Selain memberikan manfaat bagi kehidupan manusia, pohon juga ternyata bisa mematikan. Menurut Guinness World Records, pohon manchineel adalah pohon paling berbahaya di dunia. Bahkan, semua bagian dari manchineel sangat beracun dan berpotensi menyebabkan kematian. Getah dari pohon ini dapat membuat kulit melepuh seperti terbakar. Jika memakan buahnya yang berbentuk seperti apel, akan membuat tenggorokan terasa panas terbakar dan mengalami sesak nafas.",
"Pohon terbesar di dunia berada di kawasan kecil di lereng barat pegunungan Sierra Nevada, California, AS. Pohon ini bernama sequoia raksasa, atau Sequoiadendron giganteum. Sequoia terbesar dan tertinggi, dapat tumbuh hingga seukuran gedung 36 lantai, lho. Pada umumnya, pohon ini berdiameter 6 meter dengan cabang-cabang raksasa berukuran hingga diameter 2,5 meter. Kulit pohon sequoia bisa memiliki ketebalan 90 cm. Selain bentuknya yang besar, pohon ini juga mempunyai umur yang panjang hingga 5.000 tahun.",
"Tanaman herbal memiliki segudang manfaat kesehatan. Seperti daun basil yang punya zat antioksidan kuat dan bisa melindungi tubuh dari radikal bebas. Atau daun thyme yang bisa meningkatkan sistem kekebalan tubuh, menurunkan tekanan darah dan menghentikan batuk, ungkap laman Health Line.", 
"Pohon yang diduga paling lama hidup adalah pohon pinus bristlecone dari California timur, yang pada tahun 2012 usianya diperkirakan 5.062 tahun. Namun untuk mencapai usia lanjut, beberapa pohon memiliki taktik yang cukup cerdik: melakukan kloning. Pohon mengkloning diri sendiri dan hidup di sebuah koloni klona, yang merupakan kumpulan pohon identik yang terhubung oleh sistem akar yang sama.",
"Peneliti Rusia berhasil menghidupkan tanaman yang telah lama punah dengan menggunakan biji yang ditanam oleh tupai 32.000 tahun yang lalu. Jejak tanaman silene stenophylla (tanaman bunga yang suka pada iklim dingin) yang berasal dari Jaman Es ditemukan di sempadan sungai di Siberia. Ilmuwan mengambil jaringan dari biji tanaman itu dan menggunakannya untuk menumbuhkan kecambah, yang lalu tumbuh menjadi tanaman tersebut."]


class UI_MainWindow(QtWidgets.QMainWindow):

  def handleLogin(self, conn):
    global LoggedInID
    global isAdmin
    isAdmin = False
    username = self.LoginWindow.usernamebox.text()
    password = self.LoginWindow.usernamebox_2.text()
    LoggedInID = db_api.login(conn, username, password)
    if (LoggedInID == "" or username =="" or password ==""):
      Widgets.messageBoxLoginBerhasil()
    else :
      Widgets.messageBoxLoginBerhasil()
      print("Login successful as ID: ", LoggedInID)
    self.LoginWindow.usernamebox.setText("")
    self.LoginWindow.usernamebox_2.setText("")
    
    # Admin handler
    if(LoggedInID == 1):
      isAdmin = True
      self.widget.setCurrentWidget(self.AdminPageWindow)
    else:
      self.widget.setCurrentWidget(self.LandingPageWindow)
    return True

  def handleRegister(self, conn):
    global LoggedInID
    username = self.RegisterWindow.usernameBox.text()
    password = self.RegisterWindow.passwordBox.text()
    customerName = self.RegisterWindow.namaBox.text()
    email = self.RegisterWindow.emailBox.text()
    phone = self.RegisterWindow.telpBox.text()
    address = self.RegisterWindow.addressBox.text()
    postalCode = self.RegisterWindow.posBox.text()
    if (username == "" or password == "" or customerName == "" or email == "" or phone == "" or address == "" or postalCode == ""):
      Widgets.messageBoxRegisterGagal()
    else :
      Widgets.messageBoxRegisterBerhasil(username)
      db_api.register(conn, username, db_api.hash(password), customerName, email, phone, address, postalCode)
      print("Register successful as ID: ", db_api.login(conn, username, password))
      self.RegisterWindow.usernameBox.setText("")
      self.RegisterWindow.passwordBox.setText("")
      self.RegisterWindow.namaBox.setText("")
      self.RegisterWindow.emailBox.setText("")
      self.RegisterWindow.telpBox.setText("")
      self.RegisterWindow.addressBox.setText("")
      self.RegisterWindow.posBox.setText("")
      self.widget.setCurrentWidget(self.LoginWindow)
    
    return True

  def handleAddTanaman(self, conn):
    nama = self.AddTanamanWindow.namaTanamanEdit.text()
    filepath = self.AddTanamanWindow.uploadFotoEdit.text()
    deskripsi = self.AddTanamanWindow.textEdit.text()
    stok = int(self.AddTanamanWindow.stokEdit.text())
    harga = int(self.AddTanamanWindow.hargaEdit.text())
    domisili = self.AddTanamanWindow.domisiliEdit.text()
    image = db_api.convertToBinaryData(filepath)
    
    if (nama == "" or filepath == "Path to File" or deskripsi == "" or stok == "" or harga == "" or domisili == ""):
      Widgets.messageBoxAddTanamanGagal()
    else :
      Widgets.messageBoxAddTanamanBerhasil(nama)
      db_api.addTanaman(conn, nama, harga, stok, deskripsi, image, domisili)
      self.AddTanamanWindow.namaTanamanEdit.setText("")
      self.AddTanamanWindow.uploadFotoEdit.setText("Path to File")
      self.AddTanamanWindow.textEdit.setText("")
      self.AddTanamanWindow.stokEdit.setText("")
      self.AddTanamanWindow.hargaEdit.setText("")
      self.AddTanamanWindow.domisiliEdit.setText("")
      print("Add tanaman " + nama + " successful")


  def handleClickUser(self):
    if(LoggedInID == 1) : 
      nama = db_api.getNamaUser(conn, LoggedInID)
      self.greetingAdminWindow.label.setText("Hai, " + nama)
      self.greetingAdminWindow.setWindowModality(QtCore.Qt.ApplicationModal)
      self.greetingAdminWindow.show()
    elif(not LoggedInID):
      self.modalLoginRegistrasiWindow.setWindowModality(QtCore.Qt.ApplicationModal)
      self.modalLoginRegistrasiWindow.show()
    else :
      nama = db_api.getNamaUser(conn, LoggedInID)
      self.greetingUserWindow.label.setText("Hai, " + nama)
      self.greetingUserWindow.setWindowModality(QtCore.Qt.ApplicationModal)
      self.greetingUserWindow.show()
  
  def handleClickCart(self) :
    self.widget.setCurrentWidget(self.CheckOutWindow)

  def handleClickModalLogin(self):
    self.widget.setCurrentWidget(self.LoginWindow)
    self.modalLoginRegistrasiWindow.close()
  
  def handleClickModalRegister(self):
    self.widget.setCurrentWidget(self.RegisterWindow)
    self.modalLoginRegistrasiWindow.close()
  
  def handleClickAdminButton(self) :
    self.widget.setCurrentWidget(self.AdminPageWindow)
    self.greetingAdminWindow.close()
  
  def handleLogout(self) :
    global LoggedInID 
    LoggedInID = 0
    self.greetingAdminWindow.close()
    self.greetingUserWindow.close()
    self.widget.setCurrentWidget(self.LandingPageWindow)


  def goToListTanaman(self, conn):
    self.ListTanamanWindow.updateTanaman(conn, isAdmin)
    windows = [self.ListTanamanWindow.Tanaman1Window, self.ListTanamanWindow.Tanaman2Window, self.ListTanamanWindow.Tanaman3Window, self.ListTanamanWindow.Tanaman4Window, self.ListTanamanWindow.Tanaman5Window, self.ListTanamanWindow.Tanaman6Window]
    for window in windows:
      self.widget.addWidget(window)
      window.setWindowTitle("OnlyPlants")
      window.setWindowIcon(QtGui.QIcon("./img/logo.png"))
      window.berandaButton.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.LandingPageWindow))
      window.tanamanButton.clicked.connect(lambda: self.goToListTanaman(conn))
      if isAdmin:
        window.RedirectButton.clicked.connect(lambda: self.widget.setCurrentWidget(self.AdminPageWindow))
      else:
        window.RedirectButton.clicked.connect(lambda: self.goToListTanaman(conn))
  
    self.widget.setCurrentWidget(self.ListTanamanWindow)
  
  def handleKanan(self, conn):
    self.ListTanamanWindow.increaseTanamanCounter(conn, isAdmin)
    self.goToListTanaman(conn)
  
  def handleKiri(self, conn):
    self.ListTanamanWindow.decreaseTanamanCounter(conn, isAdmin)
    self.goToListTanaman(conn)

  def goToLandingPage(self):
    self.desc = facts
    self.descRand = randint(0, len(self.desc) - 1)
    self.LandingPageWindow.landingText.setText(self.desc[self.descRand])
    self.widget.setCurrentWidget(self.LandingPageWindow)
  
  def handleCheckout(self):
    Widgets.messageBoxCheckoutBerhasil()

  # def initiateCart(self):


  def __init__(self) -> None:
    super(QtWidgets.QWidget, self).__init__()
    self.widget = QtWidgets.QStackedWidget()
    self.widget.setWindowTitle("OnlyPlants")
    self.widget.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    self.widget.setMaximumSize(QtCore.QSize(1200,800))

    self.WelcomeWindow = welcomescreen.Ui_Dialog()
    self.WelcomeWindow.setWindowTitle("OnlyPlants")
    self.WelcomeWindow.setWindowIcon(QtGui.QIcon("./img/logo.png"))
    self.WelcomeWindow.loginButton.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.LoginWindow))

    self.LoginWindow = login.Ui_Login()
    

    self.AboutUsWindow = aboutUs.Ui_AboutUs()
    self.widget.addWidget(self.AboutUsWindow)

    self.LoginWindow.submitButton.clicked.connect(lambda: self.handleLogin(conn))
    self.LoginWindow.daftarButton.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.RegisterWindow))
    self.WelcomeWindow.registerButton.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.RegisterWindow))

    self.RegisterWindow = register.Ui_Register()

    self.RegisterWindow.registerButton.clicked.connect(lambda: self.handleRegister(conn))

    self.widget.addWidget(self.WelcomeWindow)
    self.widget.addWidget(self.LoginWindow)
    self.widget.addWidget(self.RegisterWindow)

    self.LandingPageWindow = landingPage.UI_landingPage()

    self.widget.addWidget(self.LandingPageWindow)

    self.ListTanamanWindow = listTanaman.Ui_Dialog(conn)
    
    self.widget.addWidget(self.ListTanamanWindow)

    self.AdminPageWindow = adminPage.UI_adminPage()

    self.widget.addWidget(self.AdminPageWindow)

    self.AddTanamanWindow = addTanaman.UI_addTanaman()
    self.widget.addWidget(self.AddTanamanWindow)

    dummy = (1, 'Dummy', 100000, 10, "Dummy data", None, "Jakarta")
    self.EditTanamanWindow = editTanaman.UI_editTanaman(dummy, conn)
    self.widget.addWidget(self.EditTanamanWindow)

    self.CheckOutWindow = checkout.Ui_Checkout()
    self.CheckOutWindow.konfirmasiPengajuan.clicked.connect(lambda: self.handleCheckout())
    self.widget.addWidget(self.CheckOutWindow)

    self.greetingUserWindow = greetingUser.Ui_Form()
    self.greetingAdminWindow = greetingAdmin.Ui_Form()
    self.modalLoginRegistrasiWindow = modalLoginRegistrasi.Ui_Form()

    self.AdminPageWindow.editTanaman.clicked.connect(lambda: self.goToListTanaman(conn))

    self.AdminPageWindow.addTanaman.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.AddTanamanWindow))

    self.AddTanamanWindow.tambahkanTanamanButton.clicked.connect(lambda: self.handleAddTanaman(conn))
    self.modalLoginRegistrasiWindow.loginButton.clicked.connect(lambda x = self.widget: self.handleClickModalLogin())
    self.modalLoginRegistrasiWindow.registrasiButton.clicked.connect(lambda x = self.widget: self.handleClickModalRegister())
    self.greetingAdminWindow.masukAdminButton.clicked.connect(lambda x = self.widget: self.handleClickAdminButton())
    self.greetingAdminWindow.keluarButton.clicked.connect(lambda x = self.widget: self.handleLogout())
    self.greetingUserWindow.keluarButton.clicked.connect(lambda x = self.widget: self.handleLogout())

    withNavbar = [self.LoginWindow, self.RegisterWindow, self.LandingPageWindow, self.ListTanamanWindow, self.AboutUsWindow, self.AdminPageWindow, self.AddTanamanWindow, self.EditTanamanWindow, self.CheckOutWindow]
    for window in withNavbar:
        window.setWindowTitle("OnlyPlants")
        window.setWindowIcon(QtGui.QIcon("./img/logo.png"))
        window.berandaButton.clicked.connect(lambda: self.goToLandingPage())
        window.tanamanButton.clicked.connect(lambda: self.goToListTanaman(conn))
        window.aboutButton.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.AboutUsWindow))
        window.userButton.clicked.connect(lambda: self.handleClickUser())
        window.cartButton.clicked.connect(lambda: self.handleClickCart())

    self.ListTanamanWindow.tanaman1.clicked.connect(lambda: self.widget.setCurrentWidget(self.ListTanamanWindow.Tanaman1Window))

    self.ListTanamanWindow.tanaman2.clicked.connect(lambda: self.widget.setCurrentWidget(self.ListTanamanWindow.Tanaman2Window))

    self.ListTanamanWindow.tanaman3.clicked.connect(lambda: self.widget.setCurrentWidget(self.ListTanamanWindow.Tanaman3Window))

    self.ListTanamanWindow.tanaman4.clicked.connect(lambda: self.widget.setCurrentWidget(self.ListTanamanWindow.Tanaman4Window))

    self.ListTanamanWindow.tanaman5.clicked.connect(lambda: self.widget.setCurrentWidget(self.ListTanamanWindow.Tanaman5Window))

    self.ListTanamanWindow.tanaman6.clicked.connect(lambda: self.widget.setCurrentWidget(self.ListTanamanWindow.Tanaman6Window))

    self.ListTanamanWindow.kanan.clicked.connect(lambda: self.handleKanan(conn))
    self.ListTanamanWindow.kiri.clicked.connect(lambda: self.handleKiri(conn))

    self.LandingPageWindow.mulaiSewaButton.clicked.connect(lambda: self.goToListTanaman(conn))

    self.widget.setCurrentWidget(self.WelcomeWindow)
    self.widget.show()


if __name__ == '__main__':
    
    database = r".\src\database\onlyplants.db"
    conn = db_api.create_connection(database)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UI_MainWindow()
    sys.exit(app.exec_())