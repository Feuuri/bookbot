from stats import get_num_words, get_book_text, get_num_characters
from stats import sort_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
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