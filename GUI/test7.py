from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt
import sys

app = QApplication(sys.argv)
widget = QWidget()

# Main layout to hold all sections
main_layout = QVBoxLayout()
main_layout.setContentsMargins(10, 10, 10, 10)
main_layout.setSpacing(10)  # Spacing between sections

def create_section(title, content):
    section_layout = QVBoxLayout()  # Layout for each section
    
    # Title
    title_label = QLabel(title)
    title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    section_layout.addWidget(title_label)
    
    # Content
    content_label = QLabel(content)
    content_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    section_layout.addWidget(content_label)

        # Line under the title
    line = QFrame()
    line.setFrameShape(QFrame.Shape.HLine)
    line.setFrameShadow(QFrame.Shadow.Plain)
    line.setStyleSheet("background-color: black;")
    line.setFixedHeight(2)  # Thin line
    section_layout.addWidget(line)

    return section_layout

# Adding sections
main_layout.addLayout(create_section("Vamsi Dictionary", "This is the main dictionary section."))
main_layout.addLayout(create_section("Introduction", "Here’s an introduction to the content."))
main_layout.addLayout(create_section("Features", "These are some cool features."))

# Apply the layout
widget.setLayout(main_layout)
widget.setWindowTitle("Structured Layout Example")
widget.resize(350, 250)
widget.show()

sys.exit(app.exec())
