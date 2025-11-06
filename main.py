import sys
from stats import num_of_words, character_count, sorting_dict
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return(file_contents)

def main():
        text = get_book_text(file_direct)
        print(text)
        
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    print(sys.argv)
file_direct = sys.argv[1]
big_dict = sorting_dict(character_count(get_book_text(file_direct)))

print(f"""
    ======= BOOKBOT =======
    Analyzing book found at {file_direct} . . .
    ------- Word Count -------
    {num_of_words(get_book_text(file_direct))}
    ------- Character Count -------
""")
for i in range(len(big_dict)):
    print(f"{big_dict[i]['char']}: {big_dict[i]['num']}")
    
print("======= END =======")
