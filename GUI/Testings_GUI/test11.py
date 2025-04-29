from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout, QFrame, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

# Window setup
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("SARAS product by ENGIN.E")
window.resize(400, 350)
window.setStyleSheet("background-color: #1c1c1c;")
spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
small_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

# Main Vertical Layout
LayoutV = QVBoxLayout()
LayoutV.setContentsMargins(10, 10, 10, 10)
LayoutV.setSpacing(20)

# Dictionary Label
Dict = QLabel("Dictionary ───────────────────────────")
Dict.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Dict.setFont(QFont("Georgia", 16))
LayoutV.addWidget(Dict)

# Horizontal Layout for Word + Side Line
LayoutH1 = QHBoxLayout()
LayoutH2 = QHBoxLayout()


#--------------------------------------
Word = QLabel("Word")
Word.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Word.setFont(QFont("AppleGothic", 18))
LayoutH1.addWidget(Word)

sideLine = QFrame()
sideLine.setFrameShape(QFrame.Shape.HLine)
sideLine.setFrameShadow(QFrame.Shadow.Sunken)
sideLine.setFixedHeight(1)
sideLine.setFixedWidth(320)
sideLine.setStyleSheet("border: none; background-color: rgba(255, 255, 255, 0.3);")
LayoutH1.addWidget(sideLine)

LayoutV.addLayout(LayoutH1)  # Nesting H layout inside V layout
#--------------------------------------

# Meaning Label
Meaning = QLabel("Meaning of the word is")
Meaning.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Meaning.setFont(QFont("Georgia", 16))
LayoutV.addWidget(Meaning)

Example = QLabel("Here is an example, Here is another example")
Example.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Example.setFont(QFont("Georgia", 16, -1, italic=True))
LayoutV.addWidget(Example)
LayoutV.addItem(small_spacer)
#--------------------------------------
Synonm = QLabel("Synonm")
Synonm.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Synonm.setFont(QFont("AppleGothic", 16))
LayoutH2.addWidget(Synonm)

sideLine1 = QFrame()
sideLine1.setFrameShape(QFrame.Shape.HLine)
sideLine1.setFrameShadow(QFrame.Shadow.Sunken)
sideLine1.setFixedHeight(1)
sideLine1.setFixedWidth(320)
sideLine1.setStyleSheet("border: none; background-color: rgba(255, 255, 255, 0.3); ")
LayoutH2.addWidget(sideLine1)

LayoutV.addLayout(LayoutH2)  # Nesting2 H layout inside V layout
#-------------------------------------------------

Synonms = QLabel("Also called as: Synonm1,synonm2")
Synonms.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Synonms.setFont(QFont("Georgia", 16))
LayoutV.addWidget(Synonms)

LayoutV.addItem(spacer)

# Bottom Line
Line = QFrame()
Line.setFrameShape(QFrame.Shape.HLine)
Line.setFrameShadow(QFrame.Shadow.Sunken)
Line.setFixedHeight(1)
Line.setStyleSheet("border: none; background-color: rgba(255, 255, 255, 0.3);")
LayoutV.addWidget(Line)

# Final Window Setup
window.setLayout(LayoutV)
window.setWindowOpacity(0.9)
window.show()
sys.exit(app.exec())
