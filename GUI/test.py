import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pop up")
        label = QLabel("This is the popup")
        self.setCentralWidget(label)

app = QApplication([])
window = Mainwindow()
window.show()

app.exec()
sys.exit()