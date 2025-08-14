def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    book_text = get_book_text("books/frankenstein.txt")
    book_list = book_text.split()
    word_count = len(book_list)
    print(f"{word_count} words found in the document")

def get_char_count():
    book_text = get_book_text("books/frankenstein.txt")
    char_dict = {}
    for char in book_text:
        charl = char.lower()
        if charl not in char_dict:
            char_dict[charl] = 1
        else:
            char_dict[charl] += 1
    print(char_dict)