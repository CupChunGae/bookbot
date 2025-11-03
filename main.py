def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return(file_contents)

def main():
        text = get_book_text("./books/frankenstein.txt")
        print(text)
        

from stats import num_of_words
num_of_words(get_book_text("./books/frankenstein.txt"))