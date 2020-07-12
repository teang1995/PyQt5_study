import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import time


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Status bar')
        self.setGeometry(300, 300, 300, 200)
        self. show()


def main():
    app = QApplication(sys.argv)
    ex = MyApp()


if __name__ == '__main__':
    main()

