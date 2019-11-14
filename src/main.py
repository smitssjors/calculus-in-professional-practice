import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit, QMessageBox, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn = QPushButton('push', self)
        btn.clicked.connect(self.printVal)
        self.lbl = QLabel(self)
        self.lbl.move(100, 40)
        self.le = QLineEdit('Wolla', self)
        self.le.move(100, 100)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Dit is skuu')
        self.show()

    def printVal(self):
        QMessageBox.information(self, "About", self.le.text())


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    sys.exit(app.exec_())
