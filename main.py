from stats import get_num_words
from stats import get_sorted_chars
import sys

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = get_num_words(args[1])
    sorted_chars = get_sorted_chars(args[1])
    print(f"Found {word_count} total words")
    for item in sorted_chars:
        print(f"{item["char"]}: {item["num"]}")

main()