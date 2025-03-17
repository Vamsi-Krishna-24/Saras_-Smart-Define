import time
from pynput.mouse import Listener

last_click_time = 0
last_position = None

def on_click(x, y, button, pressed):
    """Detects double-click events."""
    global last_click_time, last_position

    if pressed:  # Mouse button pressed
        current_time = time.time()
        
        if (current_time - last_click_time) < 0.3 and last_position == (x, y):
            print(f"Double-click detected at ({x}, {y})")
        
        last_click_time = current_time
        last_position = (x, y)

def start_mouse_listener():
    """Starts the mouse event listener."""
    with Listener(on_click=on_click) as listener:
        listener.join()  # Keeps the listener running

# Run this only if the script is executed directly (not when imported)
if __name__ == "__main__":
    start_mouse_listener()
