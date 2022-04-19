import welcomescreen
import login
import register
import landingPage
import listTanaman
import database.db_api as db_api

from PyQt5 import QtCore, QtGui, QtWidgets


global LoggedInID

def handleLogin(LoginWindow: login.Ui_Login, conn):
  global LoggedInID
  username = LoginWindow.usernamebox.text()
  password = LoginWindow.usernamebox_2.text()
  LoggedInID = db_api.login(conn, username, password)
  print("Login successful as ID: ", LoggedInID)
  return True

def handleRegister(RegisterWindow: register.Ui_Register, conn):
  global LoggedInID
  username = RegisterWindow.usernameBox.text()
  password = RegisterWindow.passwordBox.text()
  email = RegisterWindow.emailBox.text()
  phone = RegisterWindow.telpBox.text()
  address = RegisterWindow.addressBox.text()
  postalCode = RegisterWindow.posBox.text()
  db_api.register(conn, username, db_api.hash(password), username, email, phone, address, postalCode)
  print("Register successful as ID: ", db_api.login(conn, username, password))
  return True

if __name__ == '__main__':
    import sys
    
    database = r".\src\database\onlyplants.db"
    conn = db_api.create_connection(database)

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    WelcomeWindow = welcomescreen.Ui_Dialog()
    WelcomeWindow.loginButton.clicked.connect(lambda x = widget: widget.setCurrentWidget(LoginWindow))

    LoginWindow = login.Ui_Login()

    LoginWindow.submitButton.clicked.connect(lambda: handleLogin(LoginWindow, conn))
    LoginWindow.daftarButton.clicked.connect(lambda x = widget: widget.setCurrentWidget(RegisterWindow))
    WelcomeWindow.registerButton.clicked.connect(lambda x = widget: widget.setCurrentWidget(RegisterWindow))

    RegisterWindow = register.Ui_Register()

    RegisterWindow.registerButton.clicked.connect(lambda: handleRegister(RegisterWindow, conn))

    widget.addWidget(WelcomeWindow)
    widget.addWidget(LoginWindow)
    widget.addWidget(RegisterWindow)

    LandingPageWindow = landingPage.UI_landingPage()

    widget.addWidget(LandingPageWindow)

    ListTanamanWindow = listTanaman.Ui_Dialog()
    
    widget.addWidget(ListTanamanWindow)

    withNavbar = [LoginWindow, RegisterWindow, LandingPageWindow, ListTanamanWindow]
    for window in withNavbar:
        window.berandaButton.clicked.connect(lambda x = widget: widget.setCurrentWidget(LandingPageWindow))
        window.tanamanButton.clicked.connect(lambda x = widget: widget.setCurrentWidget(ListTanamanWindow))

    widget.setCurrentWidget(WelcomeWindow)
    widget.show()
    # Window = MainWindow()
    # Window.stack.show()
    sys.exit(app.exec_())