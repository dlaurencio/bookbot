from stats import get_num_words
from stats import get_sorted_chars

def main():
    word_count = get_num_words()
    sorted_chars = get_sorted_chars()
    print(f"Found {word_count} total words")
    for item in sorted_chars:
        print(f"{item["char"]}: {item["num"]}")

main()