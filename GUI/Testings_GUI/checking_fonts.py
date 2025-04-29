from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

fonts= QFontDatabase.families()

with open('/Users/surisettivamsikrishna/Downloads/Vamsi Pc/CODES/Mark2/SARAS/Saras_-Smart-Define/GUI/fonts','w') as file:
    for font in fonts:
        file.write(font + '\n')

print("DOne")