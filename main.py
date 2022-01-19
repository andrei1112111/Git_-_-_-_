from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from pyui import Ui_MainWindow


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.setFixedSize(100, 100)
        self.ui.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.ui.centralwidget)
        layout.addWidget(self.ui.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        w = randint(10, 100)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.setPen(pen)
        painter.drawEllipse(randint(10, 500), randint(10, 500), w, w)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    from random import randint
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
