import time
import pyautogui
import pyperclip
from pynput import mouse

class MouseListener:
    def __init__(self):
        self.last_click_time = 0
        self.last_position = None
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self, x, y, button, pressed):
        if pressed:
            current_time = time.time()
            print(f"clicked at:{x},{y}")
            if (current_time - self.last_click_time) < 0.5 and self.last_position == (x, y):
                pyautogui.moveTo(x, y)
                pyautogui.click()
                pyautogui.hotkey("ctrl", "c")
                time.sleep(0.5)  # Ensure clipboard updates
                copied_text = pyperclip.paste()
                print(f"Copied: {copied_text}")

            self.last_click_time = current_time
            self.last_position = (x, y)

    def start(self):
        self.listener.start()
        self.listener.join()

# Only run if executed directly, not on import
if __name__ == "__main__":
    mouse_listener = MouseListener()
    mouse_listener.start()

