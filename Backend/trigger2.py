import pyautogui
import keyboard
import time

def get_mouse_position():
    print("Double-click anywhere to get the coordinates...")
    
    # Wait for the user to double-click
    keyboard.wait("double click")
    
    # Get current mouse position
    x, y = pyautogui.position()
    
    print(f"Detected coordinates: ({x}, {y})")
    return x, y

def copy_text_at_position(x, y):
    # Move to the detected position
    pyautogui.moveTo(x, y)

    # Simulate a click to focus (optional)
    pyautogui.click()

    # Simulate Ctrl+C to copy text
    pyautogui.hotkey("ctrl", "c")
    
    print("Text copied!")

if __name__ == "__main__":
    x, y = get_mouse_position()
    time.sleep(0.5)  # Small delay
    copy_text_at_position(x, y)
