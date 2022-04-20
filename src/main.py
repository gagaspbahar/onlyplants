import UIController as UIC
import database.db_api as db_api
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == '__main__':
    
    database = r".\src\database\onlyplants.db"
    conn = db_api.create_connection(database)
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont("./resources/Sansita-Regular.ttf")
    MainWindow = UIC.UI_MainWindow(conn)
    sys.exit(app.exec_())