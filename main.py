from stats import wordcounter
from stats import charactercounter
from stats import sorter
import sys


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        contents = get_book_text(path)
        wordcount = wordcounter(contents)
        unsorted_dict = charactercounter(contents)
        sorted_dict = sorter(unsorted_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        for c in sorted_dict:
            print(f"{c["char"]}: {c["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

 
def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
    return book_contents



main()