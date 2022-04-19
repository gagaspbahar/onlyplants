import database.db_api as db_api
import welcomescreen
import login
import register
import landingPage
import listTanaman
import adminPage
import addTanaman
import editTanaman
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


global LoggedInID
global isAdmin


class UI_MainWindow(QtWidgets.QMainWindow):

  def handleLogin(self, conn):
    global LoggedInID
    global isAdmin
    isAdmin = False
    username = self.LoginWindow.usernamebox.text()
    password = self.LoginWindow.usernamebox_2.text()
    LoggedInID = db_api.login(conn, username, password)
    print("Login successful as ID: ", LoggedInID)
    
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
    email = self.RegisterWindow.emailBox.text()
    phone = self.RegisterWindow.telpBox.text()
    address = self.RegisterWindow.addressBox.text()
    postalCode = self.RegisterWindow.posBox.text()
    db_api.register(conn, username, db_api.hash(password), username, email, phone, address, postalCode)
    print("Register successful as ID: ", db_api.login(conn, username, password))
    return True


  def __init__(self) -> None:
    super(QtWidgets.QWidget, self).__init__()
    self.widget = QtWidgets.QStackedWidget()

    self.WelcomeWindow = welcomescreen.Ui_Dialog()
    self.WelcomeWindow.loginButton.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.LoginWindow))

    self.LoginWindow = login.Ui_Login()

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

    self.ListTanamanWindow = listTanaman.Ui_Dialog()
    
    self.widget.addWidget(self.ListTanamanWindow)

    self.AdminPageWindow = adminPage.UI_adminPage()

    self.widget.addWidget(self.AdminPageWindow)

    self.AddTanamanWindow = addTanaman.UI_addTanaman()
    self.widget.addWidget(self.AddTanamanWindow)

    self.EditTanamanWindow = editTanaman.UI_editTanaman()
    self.widget.addWidget(self.EditTanamanWindow)

    self.AdminPageWindow.editTanaman.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.EditTanamanWindow))

    self.AdminPageWindow.addTanaman.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.AddTanamanWindow))

    withNavbar = [self.LoginWindow, self.RegisterWindow, self.LandingPageWindow, self.ListTanamanWindow, self.AdminPageWindow, self.AddTanamanWindow, self.EditTanamanWindow]
    for window in withNavbar:
        window.berandaButton.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.LandingPageWindow))
        window.tanamanButton.clicked.connect(lambda x = self.widget: self.widget.setCurrentWidget(self.ListTanamanWindow))

    self.widget.setCurrentWidget(self.WelcomeWindow)
    self.widget.show()





if __name__ == '__main__':
    
    database = r".\src\database\onlyplants.db"
    conn = db_api.create_connection(database)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UI_MainWindow()
    sys.exit(app.exec_())