from PyQt6.QtWidgets import QLabel, QFrame, QVBoxLayout, QWidget, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase
import sys

app = QApplication(sys.argv)

window = QWidget()
Layout = QVBoxLayout()
Layout.setContentsMargins(10,10,10,10)
Layout.setSpacing(10)
window.resize(400,350)
window.setWindowTitle("Checking the Fonts")


fonts = QFontDatabase.families()
for font in fonts:
    label = QLabel(font[:20])
    label.setFont(QFont(font,14))
    Layout.addWidget(label)

window.setLayout(Layout)
window.show()

sys.exit(app.exec())