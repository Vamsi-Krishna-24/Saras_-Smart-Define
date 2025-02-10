import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class PopupWindow(QMainWindow):
    def __init__(self, word, meaning, examples, synonyms):
        super().__init__()
        
        self.setWindowTitle(f"Definition of '{word}'")
        self.resize(400, 300)

        # Main widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Labels for word, meaning, and synonyms
        word_label = QLabel(f"<b>Word:</b> {word}")
        meaning_label = QLabel(f"<b>Meaning:</b> {meaning}")
        examples_label = QLabel(f"<b>Examples:</b> {examples}")
        synonyms_label = QLabel(f"<b>Synonyms:</b> {', '.join(synonyms)}")

        for label in (word_label, meaning_label,examples_label, synonyms_label):
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            layout.addWidget(label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Applying the dark theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: rgb(33, 32, 32);
                color: #ffffff;
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 10px;
                padding: 15px;
            }
            QLabel {
                font-family: 'Helvetica';
                font-size: 16px;
                color: #E0E0E0;
            }
            QLabel::selection {
                background-color: #ffeb3b;
                color: black;
            }
        """
        )

def show_popup(word, meaning, examples, synonyms):
    app = QApplication(sys.argv)
    window = PopupWindow(word, meaning, examples, synonyms)
    window.show()
    app.exec()
    sys.exit()

# Example usage
if __name__ == "__main__":
    show_popup("Example", "A representative form or pattern", ["This is an example sentence."], ["sample", "instance", "case"])

