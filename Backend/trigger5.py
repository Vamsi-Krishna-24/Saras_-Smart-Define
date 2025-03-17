import time
import win32api, win32con
import pyperclip  # Required to get copied text
from pynput.mouse import Button, Controller

mouse = Controller()
#cat dirnks teh milk eh ? do nu think
def copy(x, y):
    # Move mouse to given coordinates
    mouse.position = (x, y)
    time.sleep(0.2)  # Wait for stability
    #this is a word actually to see the test set for pyper
    # Click to focus on the text field
    mouse.click(Button.left, 2)
    time.sleep(0.2)

    
    time.sleep(0.2)  # Wait for clipboard to update


# Example usage
copy(653, 200)
