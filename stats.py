def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    character_counts = {}
    for char in text.lower():  # Convert to lowercase for standardization
        if char in character_counts:  # If the character exists in the dictionary
            character_counts[char] += 1  # Increment the count
        else:  # If the character does not exist in the dictionary
            character_counts[char] = 1  # Initialize the count
    return character_counts

def sort_characters(char_count_dict: dict) -> list:
    # Return a list of tuples sorted by count in descending order
    return sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)