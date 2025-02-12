from trigger import detect_double_tap_and_get_text
from db_handler import fetch_word_details
from popup import show_popup

def main():
    while True:
        # Wait for double-tap and get the selected text
        selected_text = detect_double_tap_and_get_text()
        
        if selected_text:
            # Fetch word details from the database
            meaning, example, synonyms = fetch_word_details(selected_text)

            # Display the popup with the word details
            show_popup(selected_text, meaning, example, synonyms)

if __name__ == "__main__":
    main()
