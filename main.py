from stats import get_num_words, get_book_text, get_num_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print(f"{num_words} words found in the document")
    print(num_characters)  # Print the dictionary directly

main()