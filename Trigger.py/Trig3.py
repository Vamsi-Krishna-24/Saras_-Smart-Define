import time
import pyperclip
from pynput import mouse, keyboard

class MouseListener:
    def __init__(self):
        self.last_click_time = 0
        self.last_position = None
        self.keyboard = keyboard.Controller()
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self, x, y, button, pressed):
        if pressed:
            current_time = time.time()
            print(f"Clicked at: {x}, {y}")

            # Detect double-click
            if (current_time - self.last_click_time) < 0.5 and self.last_position == (x, y):
                print("Double-click detected!")

                # Step 1: Simulate "Shift + Left Arrow" (forces text selection)
                self.keyboard.press(keyboard.Key.shift)
                self.keyboard.tap(keyboard.Key.left)
                self.keyboard.release(keyboard.Key.shift)
                time.sleep(0.1)  

                # Step 2: Copy selected text
                pyperclip.copy("")  # Clear clipboard
                time.sleep(0.1)
                self.keyboard.press(keyboard.Key.ctrl)
                self.keyboard.tap('c')
                self.keyboard.release(keyboard.Key.ctrl)

                time.sleep(0.3)  # Wait for clipboard update
                copied_text = pyperclip.paste()
                
                if copied_text.strip():
                    print(f"✅ Copied: {copied_text}")
                else:
                    print("❌ No text copied! Did the word actually get selected?")

            self.last_click_time = current_time
            self.last_position = (x, y)

    def start(self):
        print("Listening for double-clicks...")
        with self.listener:  
            self.listener.join()  

if __name__ == "__main__":
    mouse_listener = MouseListener()
    mouse_listener.start()
