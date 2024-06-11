import window, pets
import sys
from PyQt5 import QtCore, QtWidgets

class mainWindow(QtWidgets.QWidget):

    pets = []

    def __init__(self, parent=None):
        super().__init__(parent)


        self.copy_btn = QtWidgets.QPushButton()
        self.copy_btn.setText("Copy")

        lay = QtWidgets.QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addStretch()
        lay.addWidget(self.copy_btn, alignment=QtCore.Qt.AlignRight)

        self.resize(400, 450)
        self.setWindowTitle("Desktop Friends")
        pet = window.Window()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
