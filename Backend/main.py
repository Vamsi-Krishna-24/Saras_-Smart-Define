from trigger import DoubleTapListner  # Correct class for detecting double tap
from db_handler import get_word_meaning  # Correct function for fetching word details
from popup import show_popup  # Correct function for displaying the popup
from db_handler import get_word_meaning
import time

def handle_word_trigger(word):
    """Handles the word trigger flow: fetch meaning and show pop-up."""
    meaning, example, synonyms = get_word_meaning(word) or ("Not found", "", "")

    show_popup(word, meaning, example, synonyms)

def main():
    listener = DoubleTapListner()  # Create an instance
    
    while True:
        selected_text = listener.listen()  # Wait for double-tap and get text
        
        if selected_text:
            handle_word_trigger(selected_text)

        time.sleep(0.5)  # Prevent excessive looping

if __name__ == "__main__":
    main()
