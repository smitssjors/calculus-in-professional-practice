from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox, QLineEdit, QApplication, QGridLayout, QVBoxLayout, QHBoxLayout
import numpy as np
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import reader
import functions


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.x = np.arange(-5., 5., 0.01)
        self.f = None
        self.setupUI()

    def setupUI(self):
        self.le = QLineEdit('/(s(*(x,p)),+(x,5))')
        plt = QPushButton('Plot')
        plt.clicked.connect(self.plotmain)
        adb = QPushButton('Analytical Derivative')
        adb.clicked.connect(self.plot_analytical_derivitive)
        ndb = QPushButton('Newton Derivative')
        ndb.clicked.connect(self.plot_newton_derrivitive)

        left_vbox = QVBoxLayout()
        left_vbox.addWidget(self.le)
        left_vbox.addWidget(plt)
        left_vbox.addWidget(adb)
        left_vbox.addWidget(ndb)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        nav = NavigationToolbar(self.canvas, self)

        right_vbox = QVBoxLayout()
        right_vbox.addWidget(self.canvas)
        right_vbox.addWidget(nav)

        hbox = QHBoxLayout()
        hbox.addLayout(left_vbox)
        hbox.addLayout(right_vbox)

        self.setLayout(hbox)
        # self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calculus in Professional Practice')
        self.show()

    def plot(self, y, color, clear=False):
        ax = self.figure.add_subplot(111)
        if clear:
            ax.clear()
        ax.plot(self.x, y, color)
        self.canvas.draw()

    def plotmain(self):
        self.f = reader.read(self.le.text())
        y = self.f.evaluate(self.x)
        self.plot(y, 'r', clear=True)

    def plot_analytical_derivitive(self):
        d = self.f.analytical_derrivite()
        print(d)
        print(d.simplify())
        y = d.evaluate(self.x)
        self.plot(y, 'b')

    def plot_newton_derrivitive(self):
        y = self.f.newton_derrivitive(self.x, 0.1)
        self.plot(y, 'g')

    def showVal(self):
        QMessageBox.information(self, 'About', self.le.text())


if __name__ == '__main__':
    # f = reader.read('/(s(*(x,p)),+(x,5))')
    # print(f, f.evaluate(2.))
    # d = f.analytical_derrivite()
    # print(d)
    # s = d.simplify()
    # print(s)

    # j = d.evaluate(x)
    # p = s.evaluate(x)

    # plt.plot(x, y, 'r', x, j, 'b')
    # plt.show()
    app = QApplication([])
    w = Window()
    sys.exit(app.exec_())
