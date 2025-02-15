from trigger import DoubleTapListner  # Correct class for detecting double tap
from db_handler import get_word_meaning  # Correct function for fetching word details
from popup import show_popup  # Correct function for displaying the popup
from db_handler import get_word_meaning
import time

def handle_word_trigger(word):
    """Handles the word trigger flow: fetch meaning and show pop-up."""
    meaning = get_word_meaning(word)
    if meaning:
        show_popup(word, meaning)
    else:
        show_popup(word, "No definition found.")

def main():
    while True:
        # Wait for double-tap and get the selected text
        selected_text = DoubleTapListner()
        
        if selected_text:
            # Fetch word details from the database
            meaning, example, synonyms = get_word_meaning(selected_text) or ("Not found", "", "")

            # Display the popup with the word details
            show_popup(selected_text, meaning, example, synonyms)

            time.sleep(0.5)

if __name__ == "__main__":
    main()
