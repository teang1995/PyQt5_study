import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#파일명만 바꿔서
form_class = uic.loadUiType("qt_designer_testt.ui")[0]
form_class2 = uic.loadUiType("qt_designer_testt2.ui")[0]
#MainBoard
#giveHint
#etc..


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()