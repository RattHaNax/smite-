import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton)
from PyQt5.QtCore import Qt, QTimer,QTime
from PyQt5.QtGui import QIcon,QFont,QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMITE!!!")
        self.setGeometry(400,350, 600, 600)
        self.setWindowIcon(QIcon("sMite.jpg"))

    def




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()