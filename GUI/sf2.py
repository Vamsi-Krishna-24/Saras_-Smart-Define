from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication
import sys

app = QApplication(sys.argv)

# Main window should be QWidget, not QLabel
window = QWidget()
layout = QVBoxLayout()
layout.setContentsMargins(10, 10, 10, 10)
layout.setSpacing(10)

window.resize(400, 350)
window.setWindowTitle("Checking the Fonts")

# Read from the file and display first 20 lines
with open('/Users/surisettivamsikrishna/Downloads/Vamsi Pc/CODES/Mark2/SARAS/Saras_-Smart-Define/GUI/fonts', 'r') as file:
    lines = file.readlines()[:20]  # Correct way to get first 20 lines
    for line in lines:
        font_label = QLabel(line.strip())  # Remove extra newlines
        layout.addWidget(font_label)       # Correct method with capital 'W'

# Set layout to the window
window.setLayout(layout)
window.show()

sys.exit(app.exec())
