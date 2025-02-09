from db_handler import get_word_meaning
from popup import show_popup

def handle_word_trigger(word):
    """Handles the word trigger flow"""
    meaning = get_word_meaning(word)
    if meaning:
        show_popup(meaning)
    else:
        show_popup("Oops! Not in the Database")

if __name__ == "__main__":
    print("Listening for double-taps...")
    from trigger import DoubleTapListner
    listner = DoubleTapListner()
    listner.start()
