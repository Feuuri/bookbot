import sys
from pathlib import Path
from stats import get_num_words, get_book_text, get_num_characters
from stats import sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]  # Just use the path as provided

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"File not found: {book_path}")
        sys.exit(1)

    # Now use the text you already retrieved
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_characters(num_characters)

    for char, count in sorted_characters:
        if char.isalpha():  # Only display alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============") # Add the closing line

main()