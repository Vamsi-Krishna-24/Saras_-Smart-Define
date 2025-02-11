from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QFrame, QTabWidget
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("SARAS product by ENGIN.E")
window.resize(400,350)
window.setStyleSheet("background-color: #rgb(0,0,0);")

tabs = QTabWidget()

tab1 = QWidget()
layout1=QVBoxLayout()
layout1.setContentsMargins(10,10,10,10)
layout1.setSpacing(2)


Dict = QLabel("Dictionary────────────────────────────")
Dict.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Dict.setFont(QFont("Georgia",16))
layout1.addWidget(Dict)


Word = QLabel("Word")
Word.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Word.setFont(QFont("AppleGothic",18))
layout1.addWidget(Word)


Meaning = QLabel("Meaning of the word is")
Meaning.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Meaning.setFont(QFont("Georgia",16))
layout1.addWidget(Meaning)

Line = QFrame()
Line.setFrameShape(QFrame.Shape.HLine)
Line.setFrameShadow(QFrame.Shadow.Sunken)
layout1.addWidget(Line)


tab2 = QWidget()
layout2= QVBoxLayout()
layout2.setContentsMargins(10,10,10,10)
layout2.setSpacing(2)

Content = QLabel("Version2 (V2) coming soon")
Content.setAlignment(Qt.AlignmentFlag.AlignCenter)

tabs.addTab(tab1, "Dictionary")
tabs.addTab(tab2, "IMAGES")

main_layout = QVBoxLayout()
main_layout.addWidget(tabs)
window.setLayout(main_layout)

window.show()
sys.exit(app.exec())
