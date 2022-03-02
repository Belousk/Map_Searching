import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from ui_file import Ui_Form
from api_work import get_address_coords, save_image

# test coords(39.741917,54.629565)(37.622513,55.75322)

MAX_MAP_SCALE = 21
MIN_MAP_SCALE = 0


class Example(QMainWindow, Ui_Form):
    def __init__(self, default_scale=8):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.map_scale = default_scale
        self.coords = [20, 20]

    def set_coords(self):
        self.coords = [float(i) for i in self.lineEdit.text().split(',')]
        self.create_image()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Up:
            if self.coords[1] - 0.001 > 0:
                self.coords[1] -= 0.11
                self.create_image()
        if event.key() == Qt.Key_Down:
            if self.coords[1] + 0.001 < 360:
                self.coords[1] += 0.11
                self.create_image()
        if event.key() == Qt.Key_Left:
            if self.coords[0] + 0.001 < 360:
                self.coords[0] += 0.11
                self.create_image()
        if event.key() == Qt.Key_Right:
            if self.coords[0] - 0.001 < 360:
                self.coords[0] -= 0.11
                self.create_image()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.setFocus()

    def create_image(self):
        save_image(self.coords, self.map_scale, 'map.jpg')
        self.pixmap = QPixmap('map.jpg')
        self.image.setPixmap(self.pixmap)
        # self.lineEdit.hide()
        # self.pushButton.hide()

    def initUI(self):
        self.pushButton.clicked.connect(self.set_coords)
        self.image = QLabel(self)
        self.image.move(10, 10)
        self.image.resize(650, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
