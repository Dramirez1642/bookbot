# Created by Dalton Ramirez for the boot.dev project regarding a bookbot.

import sys

from stats import get_book_text
from stats import word_count
from stats import character_count
from stats import report_results



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    num_words = word_count(book_contents)
    num_characters = character_count(book_contents)
    report = report_results(num_characters)
    print(report)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in report:
        current_char = dict["character"]
        current_count = dict["count"]
        print(f"{current_char}: {current_count}")
    print("============= END ===============")




if __name__ == "__main__":
    main()