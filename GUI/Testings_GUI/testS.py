from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QFrame, QSpacerItem, QSizePolicy, QColorDialog
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)
widget = QWidget()
main_layout = QVBoxLayout()
main_layout.setContentsMargins(10,10,10,10)
main_layout.setSpacing(100)



title = QLabel("Dictonary  ────────────────")
title.setAlignment(Qt.AlignmentFlag.AlignTop and Qt.AlignmentFlag.AlignLeft)
title.setFont(QFont("Georgia",14))
main_layout.addWidget(title)


Dict= QLabel("Word")
Dict.setAlignment(Qt.AlignmentFlag.AlignTop and Qt.AlignmentFlag.AlignLeft)
Dict.setFont(QFont("Georgia",14,QFont.Weight.Bold))
main_layout.addWidget(Dict)


Line = QFrame()
Line.setFrameShape(QFrame.Shape.HLine)
Line.setFrameShadow(QFrame.Shadow.Sunken)
Line.setStyleSheet("color: white; background-color: white; width: 1px")
main_layout.addWidget(Line)

spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
main_layout.addItem(spacer)

widget.setWindowOpacity(0.9)
widget.setStyleSheet("background-color: #1b1b1b;")  
widget.setLayout(main_layout)
widget.setWindowTitle("SARAS - Product of Engin.E")
widget.resize(400,300)
widget.show()
sys.exit(app.exec())