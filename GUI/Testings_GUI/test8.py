from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QFrame, QSpacerItem, QSizePolicy, QColorDialog
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("SARAS product by ENGIN.E")
window.resize(400,350)
window.setStyleSheet("background-color: #1c1c1c;")
spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)


layout=QVBoxLayout()
layout.setContentsMargins(10,10,10,10)
layout.setSpacing(20)

Dict = QLabel("Dictionary   ───────────────────────────")
Dict.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Dict.setFont(QFont("Georgia",16))
layout.addWidget(Dict)


Word = QLabel("Word")
Word.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Word.setFont(QFont("AppleGothic",18))
layout.addWidget(Word)


Meaning = QLabel("Meaning of the word is")
Meaning.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Meaning.setFont(QFont("Georgia",16))
layout.addWidget(Meaning)
layout.addItem(spacer)         #added the placer to keep the line below

Line = QFrame()
Line.setFrameShape(QFrame.Shape.HLine)
Line.setFrameShadow(QFrame.Shadow.Sunken)
Line.setFixedHeight(1)
Line.setStyleSheet("""
    border: none; background-color: rgba(255, 255, 255, 0.3);
""")
layout.addWidget(Line)

window.setWindowOpacity(0.9)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
