import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton)
from PyQt5.QtCore import Qt, QTimer, QTime, QRect
from PyQt5.QtGui import QIcon,QFont,QPixmap

#EZ mode
class Windowez(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMITE!!!(EZ)")
        self.setGeometry(500, 100, 900, 900)
        self.setWindowIcon(QIcon("sMite.jpg"))
        label = QLabel(self)

        Blue_pixmap = QPixmap("Blue Sentinel.png")
        label.setPixmap(Blue_pixmap)
        label.setScaledContents(True)
        label.setGeometry(270, 400, 400, 400)

        Red_pixmap = QPixmap("Red Sentinel.png")
        label.setPixmap(Red_pixmap)
        label.setScaledContents(True)
        label.setGeometry(270, 400, 400, 400)

        Elder_pixmap = QPixmap("Elder Dragon.png")
        label.setPixmap(Elder_pixmap)
        label.setScaledContents(True)
        label.setGeometry(270, 400, 400, 400)

        Baron_pixmap = QPixmap("Baron Nashor.png")
        label.setPixmap(Baron_pixmap)
        label.setScaledContents(True)
        label.setGeometry(270, 400, 400, 400)

#HARD mode
class Windowhard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMITE!!!(HARD)")
        self.setGeometry(500, 100, 900, 900)
        self.setWindowIcon(QIcon("sMite.jpg"))



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SMITE!!!")
        self.setGeometry(500,100, 900, 900)
        self.setStyleSheet("background-color: Black;")
        self.setWindowIcon(QIcon("sMite.jpg"))
        self.initUI()

        label = QLabel("Smite Real or Cake",self)
        label.setFont(QFont("Arial",60))
        label.setGeometry(100, 0, 800, 400)
        label.setStyleSheet("color:yellow;fron-weight:bold;font-style: italic")

    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        #ทำปุ่ม EZ
        btn1 = QPushButton("EZ",self)#ใส่ชื่อ
        btn1.setGeometry(QRect(200, 400, 200, 200))
        btn1.setFont(QFont("Arial", 30))#font
        btn1.setStyleSheet("background-color:rgb(27, 250, 87); color:white; font-weight:bold;")
        btn1.clicked.connect(self.go_next1)

        # ทำปุ่ม Hard
        btn2 = QPushButton("HARD", self)  # ใส่ชื่อ
        btn2.setGeometry(QRect(500, 400, 200, 200))
        btn2.setFont(QFont("Arial", 30))  # font
        btn2.setStyleSheet("background-color:rgb(79, 3, 0); color:white; font-weight:bold;")
        btn2.clicked.connect(self.go_next2)

    def go_next1(self):
        self.Window_EZ = Windowez()
        self.Window_EZ.show()

    def go_next2(self):
        self.Window_HARD = Windowhard()
        self.Window_HARD.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()