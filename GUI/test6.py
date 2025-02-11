from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)
widget = QWidget()
main_layout = QVBoxLayout()
main_layout.setContentsMargins(10,10,10,10)
main_layout.setSpacing(5)

def create_section(title,content):
    section_layout=QVBoxLayout()

    title_label= QLabel(title)
    title_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    section_layout.addWidget(title_label)


    line = QFrame()
    line.setFrameShape(QFrame.Shape.HLine)
    line.setFrameShadow(QFrame.Shadow.Sunken)
    section_layout.addWidget(line)

    content = QLabel(content)
    content.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    section_layout.addWidget(content)

    return section_layout


main_layout.addLayout(create_section("WORD","The meaning of the word"))
main_layout.addLayout(create_section("Examples could be:", "Yeah this is a good example"))
main_layout.addLayout(create_section("Synonms","You coul duse these synonms"))


widget.setLayout(main_layout)
widget.setWindowTitle("Hey There !")
widget.show()
widget.resize(400,300)

sys.exit(app.exec())