from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import Qt
import sys

class DictionaryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dictionary")
        self.setStyleSheet("""
            QWidget {
                background-color:rgb(27, 25, 25);
                color: #ffffff;
                font-family: Helvetica, Arial, sans-serif;
                font-size: 16px;
            }
            QFrame {
                border: 1px solid #ffffff;
            }
            QLabel#heading {
                font-size: 25px;
                font-weight: bold;
            }
            QLabel#sectionTitle {
                font-weight: bold;
            }
        """)

        layout = QVBoxLayout()

        # Heading
        heading = QLabel("Dictionary")
        heading.setObjectName("heading")
        layout.addWidget(heading)

        layout.addWidget(self.create_line())

        # Word and Meaning
        word_meaning = QLabel("Word : Meaning")
        layout.addWidget(word_meaning)

        layout.addWidget(self.create_line())

        # Examples
        examples = ["Example 1", "Example 2"]
        for example in examples:
            layout.addWidget(QLabel(example))

        layout.addWidget(self.create_line())

        # Synonyms
        synonyms_label = QLabel("SYNONYMS: synonym1, synonym2")
        synonyms_label.setObjectName("sectionTitle")
        layout.addWidget(synonyms_label)

        self.setLayout(layout)
        self.resize(400, 300)

    def create_line(self):
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        return line

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DictionaryWindow()
    window.show()
    sys.exit(app.exec())