import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import Window

if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    sys.exit(app.exec_())
