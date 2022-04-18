import welcomescreen
import login
import register

from PyQt5 import QtCore, QtGui, QtWidgets

# class MainWindow(QtWidgets.QMainWindow):
#   def __init__(self, parent=None):
#     super(MainWindow, self).__init__(parent)
#     self.stack = QtWidgets.QStackedWidget()

#     self.loginWindow = login.Ui_Login()
#     self.registerWindow = register.Ui_Register()
#     self.welcomeWindow = welcomescreen.Ui_Dialog()

#     self.stack.addWidget(self.welcomeWindow)
#     self.stack.addWidget(self.loginWindow)
#     self.stack.setCurrentWidget(self.welcomeWindow)
#     self.stack.show()
  
#   def initLoginPage(self):
#     self.welcomeWindow.loginButton.clicked.connect(lambda x = self.stack: self.stack.setCurrentWidget(self.loginWindow))
  
#   def initRegisterPage(self):
#     self.stack.addWidget(self.registerWindow)
#     self.welcomeWindow.registerButton.clicked.connect(lambda x = self.stack: self.stack.setCurrentWidget(self.registerWindow))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    WelcomeWindow = welcomescreen.Ui_Dialog()
    WelcomeWindow.loginButton.clicked.connect(lambda x = widget: widget.setCurrentWidget(LoginWindow))

    LoginWindow = login.Ui_Login()

    WelcomeWindow.registerButton.clicked.connect(lambda x = widget: widget.setCurrentWidget(RegisterWindow))
    RegisterWindow = register.Ui_Register()

    widget.addWidget(WelcomeWindow)
    widget.addWidget(LoginWindow)
    widget.addWidget(RegisterWindow)
    
    widget.setCurrentWidget(WelcomeWindow)
    widget.show()
    # Window = MainWindow()
    # Window.stack.show()
    sys.exit(app.exec_())