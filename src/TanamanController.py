import listTanaman

from PyQt5 import QtCore, QtGui, QtWidgets

class UI_ListTanamanWindow(QtWidgets.QWidget):
  def __init__(self):
    super(QtWidgets.QWidget, self).__init__()
    self.ListTanaman = listTanaman.Ui_Dialog()
  