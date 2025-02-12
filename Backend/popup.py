from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QSpacerItem, QSizePolicy, QApplication
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class Popup(QWidget):
    def __init__(self, word, meaning, example, synonyms):
        super().__init__()
        self.setWindowTitle("SARAS - Product by ENGIN.E")
        self.resize(400, 350)
        self.setStyleSheet("background-color: #1c1c1c;")
        self.setWindowOpacity(0.9)

        # Layout setup
        LayoutV = QVBoxLayout()
        LayoutV.setContentsMargins(10, 10, 10, 10)
        LayoutV.setSpacing(20)

        # Dictionary Label
        Dict = QLabel("Dictionary ───────────────────────────")
        Dict.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        Dict.setFont(QFont("Georgia", 16))
        LayoutV.addWidget(Dict)

        # Word with line
        LayoutH1 = QHBoxLayout()
        WordLabel = QLabel(word)
        WordLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        WordLabel.setFont(QFont("AppleGothic", 18))
        LayoutH1.addWidget(WordLabel)

        sideLine = QFrame()
        sideLine.setFrameShape(QFrame.Shape.HLine)
        sideLine.setFixedHeight(1)
        sideLine.setStyleSheet("background-color: rgba(255, 255, 255, 0.3);")
        LayoutH1.addWidget(sideLine)
        LayoutV.addLayout(LayoutH1)

        # Meaning
        MeaningLabel = QLabel(meaning)
        MeaningLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        MeaningLabel.setFont(QFont("Georgia", 16))
        LayoutV.addWidget(MeaningLabel)

        # Example
        ExampleLabel = QLabel(example)
        ExampleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        ExampleLabel.setFont(QFont("Georgia", 16, -1, italic=True))
        LayoutV.addWidget(ExampleLabel)

        # Spacer
        LayoutV.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Synonyms with line
        LayoutH2 = QHBoxLayout()
        SynonymLabel = QLabel("Synonyms")
        SynonymLabel.setFont(QFont("AppleGothic", 16))
        LayoutH2.addWidget(SynonymLabel)

        sideLine1 = QFrame()
        sideLine1.setFrameShape(QFrame.Shape.HLine)
        sideLine1.setFixedHeight(1)
        sideLine1.setStyleSheet("background-color: rgba(255, 255, 255, 0.3);")
        LayoutH2.addWidget(sideLine1)
        LayoutV.addLayout(LayoutH2)

        SynonymsLabel = QLabel(synonyms)
        SynonymsLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        SynonymsLabel.setFont(QFont("Georgia", 16))
        LayoutV.addWidget(SynonymsLabel)

        # Bottom Line
        Line = QFrame()
        Line.setFrameShape(QFrame.Shape.HLine)
        Line.setStyleSheet("background-color: rgba(255, 255, 255, 0.3);")
        LayoutV.addWidget(Line)

        self.setLayout(LayoutV)

# Function to display popup (called from main.py)
def show_popup(word, meaning, example, synonyms):
    app = QApplication(sys.argv)
    popup = Popup(word, meaning, example, synonyms)
    popup.show()
    sys.exit(app.exec())
