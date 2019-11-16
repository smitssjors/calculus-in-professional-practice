from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox, QLineEdit
from functions import *
import numpy as np
import matplotlib.pyplot as plt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn = QPushButton('push', self)
        btn.clicked.connect(self.showVal)
        self.lbl = QLabel(self)
        self.lbl.move(100, 40)
        self.le = QLineEdit('Wolla', self)
        self.le.move(100, 100)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Dit is skuu')
        self.show()

    def showVal(self):
        QMessageBox.information(self, 'About', self.le.text())


if __name__ == '__main__':
    big = VariableFunction()
    small = NaturalNumberFunction(2)
    p = FactorialFunction(big)
    x = np.arange(-5., 5., 0.2)
    y = p.evaluate(x)
    plt.plot(x, y, 'r')
    plt.show()
    # app = QApplication([])
    # w = Window()
    # sys.exit(app.exec_())
