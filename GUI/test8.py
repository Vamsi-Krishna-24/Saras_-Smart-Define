from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QFrame
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("SARAS product by ENGIN.E")
window.resize(400,350)
window.setStyleSheet("background-color: #rgb(0,0,0);")

layout=QVBoxLayout()
layout.setContentsMargins(10,10,10,10)
layout.setSpacing(2)

Dict = QLabel("Dictionary────────────────────────────")
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

Line = QFrame()
Line.setFrameShape(QFrame.Shape.HLine)
Line.setFrameShadow(QFrame.Shadow.Sunken)
layout.addWidget(Line)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
