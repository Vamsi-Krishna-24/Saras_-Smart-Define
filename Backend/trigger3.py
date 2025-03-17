import time
import pyperclip
from pynput import mouse
import win32api
import win32con

def copy_word_at(x, y):
    """
    Moves the cursor to the given (x, y) coordinate,
    performs a double-click to select a word,
    simulates a Ctrl+C to copy it,
    then retrieves the text using pyperclip.
    """
    # Move cursor
    win32api.SetCursorPos((x, y))
    time.sleep(0.2)  # Let the cursor settle

    # Simulate a double-click
    for _ in range(2):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)  # Brief pause between clicks

    time.sleep(0.3)  # Allow selection to register

    # Simulate Ctrl+C to copy selection
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)   # Press Ctrl down
    win32api.keybd_event(0x43, 0, 0, 0)                   # Press 'C' down (0x43 is the ASCII code for 'C')
    time.sleep(0.1)
    win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release 'C'
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release Ctrl

    time.sleep(0.5)  # Wait for clipboard to update

    # Use pyperclip to get the copied text from the clipboard
    copied_text = pyperclip.paste()
    print(f"Copied word: {copied_text}")
    return copied_text

def on_click(x, y, button, pressed):
    """Handles mouse click events. On press, calls copy_word_at."""
    if pressed:
        print(f"Clicked at: {x}, {y}")
        copy_word_at(x, y)

# Start the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
