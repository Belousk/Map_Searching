import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from ui_file import Ui_Form
from api_work import get_address_coords, save_image


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def creat_image(self):
        coords = self.lineEdit.text().split()
        z = int(self.lineEdit_2.text())
        save_image(coords, z, 'map.jpg')
        self.pixmap = QPixmap('map.jpg')
        self.image.setPixmap(self.pixmap)

    def initUI(self):
        self.pushButton.clicked.connect(self.creat_image)
        self.image = QLabel(self)
        self.image.move(10, 10)
        self.image.resize(650, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
