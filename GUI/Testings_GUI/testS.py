from PyQt6.QtWidgets import QHBoxLayout

# Horizontal layout for "Word" and the line beside it
word_layout = QHBoxLayout()

Word = QLabel("Word")
Word.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
Word.setFont(QFont("AppleGothic", 18))
word_layout.addWidget(Word)

# Sleek line beside the word
Line = QFrame()
Line.setFrameShape(QFrame.Shape.HLine)
Line.setStyleSheet("border: none; background-color: rgba(255, 255, 255, 0.3); height: 1px;")
Line.setFixedHeight(1)        # Line thickness
Line.setFixedWidth(180)       # Line length
word_layout.addWidget(Line)

# Add this horizontal layout to the main vertical layout
layout.addLayout(word_layout)
