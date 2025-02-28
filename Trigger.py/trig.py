import time
import pyperclip
import pyautogui
from pynput import mouse, keyboard

class MouseListener:
    def __init__(self):
        self.last_click_time = 0
        self.last_position = None
        self.keyboard = keyboard.Controller()  # To send keyboard shortcuts
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self, x, y, button, pressed):
        if pressed:
            current_time = time.time()
            print(f"Clicked at: {x}, {y}")
            
            # Check if it's a double-click
            if (current_time - self.last_click_time) < 0.5 and self.last_position == (x, y):
                print("Double-click detected! Selecting and copying the word...")
                
                # Simulate a double-click to ensure word selection
                pyautogui.doubleClick(x, y)

                # Small delay to ensure selection completes
                time.sleep(0.2)  

                # Press Ctrl + C (or Command + C on Mac)
                with self.keyboard.pressed(keyboard.Key.ctrl):  # Use keyboard.Key.cmd for Mac
                    self.keyboard.tap('c')

                # Wait for clipboard to update
                time.sleep(0.2)  
                copied_text = pyperclip.paste()

                print(f"Copied Word: {copied_text}")

            self.last_click_time = current_time
            self.last_position = (x, y)

    def start(self):
        self.listener.start()
        self.listener.join()

# Run the script
if __name__ == "__main__":
    mouse_listener = MouseListener()
    mouse_listener.start()
