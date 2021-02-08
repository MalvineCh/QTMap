import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from get_map import get_image

lon = "37.530887"
lat = "55.703118"
delta = "0.002"
get_image(lon, lat, delta)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def change_im(self, d):
        global delta

        delta = str(int(delta) + d)
        get_image(lon, lat, delta)

        self.pixmap = QPixmap('map.png')
        self.image.setPixmap(self.pixmap)

    def initUI(self):
        self.setGeometry(700, 200, 600, 500)
        self.setWindowTitle('QTMAP')

        self.pixmap = QPixmap('map.png')
        self.image = QLabel(self)
        self.image.resize(400, 400)

        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageDown:
            d = 0.001
            self.change_im(d)
        elif event.key() == Qt.Key_PageUp:
            d = -0.001
            self.change_im(d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())