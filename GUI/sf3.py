from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QScrollArea
from PyQt6.QtGui import QFont, QFontDatabase
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 400)
window.setFixedSize(800, 650)
window.setWindowTitle("Checking the Fonts")

# Adding scroll element
scroll = QScrollArea()
scroll.setWidgetResizable(True)

# Content widget to hold labels
content_widget = QWidget()
Layout = QVBoxLayout(content_widget)

fonts = QFontDatabase.families()
for font in fonts:
    label = QLabel(font[:20])
    label.setFont(QFont(font, 14))
    Layout.addWidget(label)

content_widget.setLayout(Layout)
scroll.setWidget(content_widget)  # Attach the content to the scroll
scroll.show()  # Show the scroll area instead of the window

sys.exit(app.exec())
