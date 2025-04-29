from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QFrame, QTabWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)

# Main Window
window = QWidget()
window.setWindowTitle("SARAS product by ENGIN.E")
window.resize(400, 350)

# Apply Background Color with Transparency
# RGBA -> A = Alpha (transparency) from 0 (fully transparent) to 255 (opaque)
window.setStyleSheet("background-color: rgba(200, 200, 255, 230);")  # Light blue with slight transparency

# Create Tab Widget
tabs = QTabWidget()  # Container for tabs

# Tab 1 - Dictionary Layout
tab1 = QWidget()
layout1 = QVBoxLayout()
layout1.setContentsMargins(10, 10, 10, 10)
layout1.setSpacing(2)

Dict = QLabel("Dictionary────────────────────────────")
Dict.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Dict.setFont(QFont("Georgia", 16))
layout1.addWidget(Dict)

Word = QLabel("Word")
Word.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Word.setFont(QFont("AppleGothic", 18))
layout1.addWidget(Word)

Meaning = QLabel("Meaning of the word is")
Meaning.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Meaning.setFont(QFont("Georgia", 16))
layout1.addWidget(Meaning)

Line = QFrame()
Line.setFrameShape(QFrame.Shape.HLine)
Line.setFrameShadow(QFrame.Shadow.Sunken)
layout1.addWidget(Line)

tab1.setLayout(layout1)  # Attach layout to Tab 1

# Tab 2 - Placeholder for New Content
tab2 = QWidget()
layout2 = QVBoxLayout()
label2 = QLabel("Welcome to the Second Tab!")
label2.setFont(QFont("Arial", 14))
layout2.addWidget(label2)
tab2.setLayout(layout2)

# Add Tabs to the Tab Widget
tabs.addTab(tab1, "Dictionary")
tabs.addTab(tab2, "Introduction")

# Main Layout
main_layout = QVBoxLayout()
main_layout.addWidget(tabs)
window.setLayout(main_layout)

# Show Window
window.show()
sys.exit(app.exec())
