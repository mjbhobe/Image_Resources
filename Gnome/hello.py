#!/usr/bin/env python3
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def main():
    app = QApplication(sys.argv)

    win = QWidget()
    label = QLabel(f"Welcome to Python Gui programming with PyQt {PYQT_VERSION_STR}")
    btn = QPushButton("Quit!")
    btn.setDefault(True)
    layout = QHBoxLayout()
    layout.addWidget(label)
    layout.addWidget(btn)
    btn.clicked.connect(qApp.quit)
    win.setLayout(layout)
    win.setWindowTitle("PyQt5 Programming")
    win.move(100, 100)
    win.show()

    return app.exec()

if __name__ == "__main__":
    main()


