from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox, QLineEdit
import numpy as np
import matplotlib.pyplot as plt
import cpp.reader as reader
import cpp.functions as functions
# from . import reader
# from . import functions


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
    f = reader.read('/(s(*(p,x)),+(x,5))')
    print(f, f.evaluate(2.))
    f.creategraph()

    # big = VariableFunction()
    # small = NaturalNumberFunction(2)
    # p = SineFunction(ProductFunction(PiFunction(), VariableFunction()))
    x = np.arange(-5., 5., 0.01)
    y = f.evaluate(x)
    plt.plot(x, y, .5)
    plt.show()
    # app = QApplication([])
    # w = Window()
    # sys.exit(app.exec_())
