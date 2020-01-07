import sys

import numpy as np
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from cpp import functions, reader, gaussian


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.x = np.arange(-5., 5., 0.01)
        self.f = None
        self.setupUI()

    def setupUI(self):
        self.le = QLineEdit('s(x)')
        plt = QPushButton('Plot')
        plt.clicked.connect(self.plotmain)

        adb = QPushButton('Analytical Derivative')
        adb.clicked.connect(self.plot_analytical_derivative)
        ndb = QPushButton('Newton Derivative')
        ndb.clicked.connect(self.plot_newton_derivative)

        self.i1 = QLineEdit()
        self.i2 = QLineEdit()
        sub_hbox = QHBoxLayout()
        sub_hbox.addWidget(self.i1)
        sub_hbox.addWidget(self.i2)

        rib = QPushButton('Riemann Integral')
        rib.clicked.connect(self.plot_riemann_integral)

        mcla = QPushButton('McLaurin series analytical')
        mcla.clicked.connect(self.plot_mclaurin_series_analytical)

        mcln = QPushButton('McLaurin series newton')
        mcln.clicked.connect(self.plot_mclaurin_series_newton)

        self.gauss_coords = QLineEdit('-3,-1;-2,0;-1,-1;0,2')
        gauss = QPushButton('Gaussian')
        gauss.clicked.connect(self.plot_gauss)

        left_vbox = QVBoxLayout()
        left_vbox.addWidget(self.le)
        left_vbox.addWidget(plt)
        left_vbox.addWidget(adb)
        left_vbox.addWidget(ndb)
        left_vbox.addLayout(sub_hbox)
        left_vbox.addWidget(rib)
        left_vbox.addWidget(mcla)
        left_vbox.addWidget(mcln)
        left_vbox.addWidget(self.gauss_coords)
        left_vbox.addWidget(gauss)

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
        ax.grid(True, which='both')
        ax.axvline(x=0, color='k')
        ax.axhline(y=0, color='k')
        self.canvas.draw()

    def plotline(self, x, y, color, clear=False):
        ax = self.figure.add_subplot(111)
        if clear:
            ax.clear()

        for i in range(len(x)):
            ax.plot((x[i], x[i]), (0., y[i]), color)

        ax.grid(True, which='both')
        ax.axvline(x=0, color='k')
        ax.axhline(y=0, color='k')
        self.canvas.draw()

    def plotmain(self):
        self.f = reader.read(self.le.text())
        print(self.f)
        self.f.create_graph()
        y = self.f.evaluate(self.x)
        self.plot(y, 'r', clear=True)

    def plot_analytical_derivative(self):
        d = self.f.analytical_derivative()
        print(d)
        print(d.simplify())
        y = d.evaluate(self.x)
        self.plot(y, 'b')

    def plot_newton_derivative(self):
        y = self.f.newton_derivative(self.x, 0.1)
        self.plot(y, 'g')

    def plot_riemann_integral(self):
        x1 = float(self.i1.text())
        x2 = float(self.i2.text())

        ix, iy, ans = self.f.riemann_integral(x1, x2, 0.01)
        self.plotline(ix, iy, 'm')
        print(ans)

    def plot_mclaurin_series_analytical(self):
        color = 1.
        for i in range(8):
            taylor = functions.taylor_analytical(self.f, i + 1)
            print(taylor)
            y = taylor.evaluate(self.x)
            color -= 0.1
            self.plot(y, str(color))

    def plot_mclaurin_series_newton(self):
        color = 1.
        for i in range(8):
            taylor_y = functions.taylor_newton(self.f, self.x, i + 1)
            color -= 0.1
            self.plot(taylor_y, str(color))

    def plot_gauss(self):
        func = gaussian.from_string(self.gauss_coords.text())
        y = func.evaluate(self.x)
        self.plot(y, 'y')


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    sys.exit(app.exec_())
