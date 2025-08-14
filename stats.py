def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    book_text = get_book_text("books/frankenstein.txt")
    book_list = book_text.split()
    word_count = len(book_list)
    return word_count

def get_char_count():
    book_text = get_book_text("books/frankenstein.txt")
    char_dict = {}
    char_list = []
    for char in book_text:
        charl = char.lower()
        if charl.isalpha() and charl not in char_dict:
            char_dict[charl] = 1
        elif charl.isalpha():
            char_dict[charl] += 1
    for item in char_dict:
        char_list.append({"char": item, "num": char_dict[item]})
    return char_list

def sort_on(items):
    return items["num"]

def get_sorted_chars():
    char_list = get_char_count()
    char_list.sort(reverse=True, key=sort_on)
    return char_list