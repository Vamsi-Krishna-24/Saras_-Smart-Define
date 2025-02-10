from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)
widget = QWidget()
layout = QVBoxLayout()
layout.setContentsMargins(10, 10, 10, 10) 
layout.setSpacing(5)



header = QLabel("Vamsi Window  ────────────────────")
header.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

layout.addWidget(header)

line = QFrame()
line.setFrameShape(QFrame.Shape.HLine)
line.setFrameShadow(QFrame.Shadow.Raised)
line.setLineWidth(1)
layout.addWidget(line)


Word = QLabel("Word")
Word.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
layout.addWidget(Word)


widget.setLayout(layout)
widget.setWindowTitle("SARAS   Product of Engin")
widget.resize(400,300)
widget.show()
sys.exit(app.exec())
