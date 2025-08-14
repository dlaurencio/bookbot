def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    book_text = get_book_text("books/frankenstein.txt")
    book_list = book_text.split()
    word_count = len(book_list)
    print(f"{word_count} words found in the document")
    
