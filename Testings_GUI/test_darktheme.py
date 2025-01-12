import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import Qt 

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        #setting a dark theme example 
        self.setWindowTitle("Testing Dark Theme")

        #Createing a Label
        label = QLabel("This is a Dark Theme")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Applying a dark theme 
        self.setStyleSheet("""
        QMainWindow {
            background-color: #121212;
            color: #ffffff;
            border: 2px solid #1e1e1e;
        }
         QLabel {
                font-size: 20px;          /* Larger text */
                font-weight: bold;        /* Bold text */
                color: #ffcc00;           /* Gold text color */
                }

""")
        
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
sys.exit()