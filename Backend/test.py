from db_handler import get_word_meaning  

word = "dog"  # Change this to a word in your DB
result = get_word_meaning(word)

if result:
    print("✅ Found:", result)
else:
    print("❌ Word not found in database!")
