import sys
from stats import get_num_words
from stats import get_char_count


if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    #filepath = "books/frankenstein.txt"
    def get_book_text(filepath):
        with open(filepath) as f: 
            book_contents = f.read()
            return book_contents


    book_contents = get_book_text(sys.argv[1])
    #print(book_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at "+sys.argv[1])
    print("----------- Word Count ----------")
    get_num_words(book_contents)
    print("--------- Character Count -------")
    get_char_count(book_contents)
    print("============= END ===============")
