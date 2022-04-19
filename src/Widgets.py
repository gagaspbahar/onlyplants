from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel, QDialogButtonBox

class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        grid_layout = self.layout()

        qt_msgboxex_icon_label = self.findChild(QLabel, "qt_msgboxex_icon_label")
        qt_msgboxex_icon_label.deleteLater()

        qt_msgbox_label = self.findChild(QLabel, "qt_msgbox_label")
        qt_msgbox_label.setAlignment(Qt.AlignCenter)
        grid_layout.removeWidget(qt_msgbox_label)

        qt_msgbox_buttonbox = self.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
        grid_layout.removeWidget(qt_msgbox_buttonbox)

        grid_layout.addWidget(qt_msgbox_label, 0, 0, alignment=Qt.AlignCenter)
        grid_layout.addWidget(qt_msgbox_buttonbox, 1, 0, alignment=Qt.AlignCenter)

class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        self.setIcon(QtGui.QIcon("./img/eyeclose.png"))

    def mouseReleaseEvent(self, event):
        super(PushButton, self).mouseReleaseEvent(event)
        self.setIcon(
            QtGui.QIcon("./img/eyeopen.png" if self.isChecked() else "./img/eyeclose.png"))