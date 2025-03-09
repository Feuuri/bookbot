def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    character_counts = {}
    
    for char in text.lower():  # Convert to lowercase here so every character is standardized
        if char in character_counts:  # Check if the character is already in the dictionary
            character_counts[char] += 1  # Increment the count
        else:
            character_counts[char] = 1  # Add the character with an initial count of 1

    return character_counts

