import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import Qt 

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        #setting a dark theme example 
        self.setWindowTitle("Testing Dark Theme")
        self.resize(400,300)

        #Createing a Label
        label = QLabel("This is a Dark Theme")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Applying a dark theme 
        self.setStyleSheet("""
        QMainWindow {
            background-color:rgb(33, 32, 32);
            color: #ffffff;
            border: 2px solidrgb(119, 28, 28);
            border_radius: 30px;
        }
        QLabel {
                font-family: 'Arial';
                font-size: 20px;          /* Larger text */
                font-weight: bold;        /* Bold text */
                color:rgb(210, 229, 244);           /* Gold text color */
                }
        QLabel::slection{
                background-color: #ffeb3b;
                color: black;
                
        }

""")
        
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
sys.exit()