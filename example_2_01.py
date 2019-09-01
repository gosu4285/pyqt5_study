import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('비즈뿌리오 발송 테스터기')
        self.setWindowIcon(QIcon('logo.jpg'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())