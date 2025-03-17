import time
import pyperclip
import win32api, win32con
import pynput
from pynput import keyboard,mouse


class WordCopier:
    def __init__(self):
        self.last_click_time = 0
        self.last_position = None
        self.keyboard=keyboard.Controller()
        self.listener = mouse.Listener(on_click=self.on_click)

    def on_click(self,x,y,pressed):
        if pressed:
            current_time=time.time()
            print("clicked at {x},{y}")

            if(current_time-self.last_click_time)<0.3 and self.last_position==(x,y):
                print("double clicked")

                win32api.SetCursorPos((x,y))




                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                time.sleep(0.1)


                win32api.keybd_event(win32con.VK_CONTROL,0,0,0)
                win32api.keybd_event(0x43,0,0,0)
                time.sleep(0.05)
                win32api.keybd_event(0x43,0,win32con.KEYEVENTF_KEYUP,0)
                win32api.keybd_event(win32con.VK_CONTROL,0,win32con.KEYEVENTF_KEYUP,0)

                time.sleep(0.2)
                copied_text=pyperclip.paste()

                if copied_text.strip():
                    print(f"Copied: {copied_text}")
                else:
                    print("No text selected!")
                    
                    self.last_click_time=current_time
                    self.last_position=(x,y)

    def start(self):
        print("Starting mouse listener")
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()


if __name__ == "__main__":
    copier = WordCopier()
    copier.start()


