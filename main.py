from stats import get_book_text, get_num_words, get_sorted_chars
import sys

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(args[1])
    word_count = get_num_words(book_text)
    sorted_chars = get_sorted_chars(book_text)
    print(f"Found {word_count} total words")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

main()