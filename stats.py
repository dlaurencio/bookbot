def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(book_text):
    book_list = book_text.split()
    return len(book_list)

def get_char_count(book_text):
    char_dict = {}
    char_list = []
    for char in book_text:
        char_lower = char.lower()
        if char_lower.isalpha():
            char_dict[char_lower] = char_dict.get(char_lower, 0) + 1
    for item in char_dict:
        char_list.append({"char": item, "num": char_dict[item]})
    return char_list

def sort_on(items):
    return items["num"]

def get_sorted_chars(book_text):
    char_list = get_char_count(book_text)
    char_list.sort(reverse=True, key=sort_on)
    return char_list