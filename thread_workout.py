import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import threading


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.btn1 = QPushButton('&Button1', self)
        self.btn2 = QPushButton(self)
        self.label = QLabel('First Label', self)
        self.initUI()

    def thread_run(self):
        self.label.setText('First label')

    def btn_clicked(self):
        self.label.setText('Thread test')
        threading.Timer(2.5, self.thread_run).start()

    def initUI(self):

        self.btn1.setCheckable(True)
        self.btn1.toggle()

        self.btn2.setText('Button&2')
        self.btn2.clicked.connect(self.btn_clicked)


        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Second label')

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())