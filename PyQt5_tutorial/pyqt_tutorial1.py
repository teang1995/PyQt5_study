# EX 3 - 1. 창 띄우기

import sys
from PyQt5.QtWidgets import QApplication, QWidget
import jupyter

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My first Application")
        self.move(300, 300)
        self.resize(400, 400)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
