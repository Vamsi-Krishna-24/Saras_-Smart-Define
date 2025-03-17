from db_handler import get_word_meaning  # Correct function for fetching word details
from popup import show_popup  # Correct function for displaying the popup
from db_handler import get_word_meaning
import time
from trig mport MouseListener


def handle_word_trigger(word):
    """Handles the word trigger flow: fetch meaning and show pop-up."""
<<<<<<< HEAD
    meaning, example, synonyms = get_word_meaning(word) or ("Not found", "", "")

    show_popup(word, meaning, example, synonyms)

def main():
    listener = DoubleTapListner()  # Create an instance
    
    while True:
        selected_text = listener.listen()  # Wait for double-tap and get text
        
        if selected_text:
            handle_word_trigger(selected_text)

        time.sleep(0.5)  # Prevent excessive looping
=======
    word_details = get_word_meaning(word)
    
    if word_details:
        show_popup(
            word_details["word"],
            word_details["definition"],
            ", ".join(word_details["examples"]),
            ", ".join(word_details["synonyms"])
        )
    else:
        show_popup(word, "No definition found.", "", "")

def main():
    """Start mouse listener for double-tap detection."""
    mouse_listener = MouseListener()
    mouse_listener.start()
>>>>>>> 4ea8e29 (selection of a word have been made)

if __name__ == "__main__":
    main()

