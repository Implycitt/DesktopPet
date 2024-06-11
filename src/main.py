import window, pets
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *
from functools import partial

class mainWindow(QMainWindow):

    row = 2 
    pets = []

    def __init__(self):
        super().__init__()

        self.addFriend()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.layout = QGridLayout(centralWidget)

        side_layout = QGridLayout()
        solveButton = QPushButton(self)
        solveButton.setText("Add Friend")
        solveButton.clicked.connect(partial(self.createPanel))
        side_layout.addWidget(solveButton, 0, 0)

        self.layout.addLayout(side_layout, 1, 0)

        self.resize(400, 450)
        self.setWindowTitle("Desktop Friends")

    def addFriend(self):
        pet = window.Window()

    def createPanel(self):
        layout = QGridLayout()
        kill = QPushButton(self)
        layout.addWidget(kill, 0, 0)
        self.layout.addLayout(layout, self.row, 0)
        self.row += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())
