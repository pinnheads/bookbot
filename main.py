import sys
from stats import get_num_words, count_char, sort_char_count


def get_book_text(filepath):
    """Reads a file in certain location and returns the content as string"""
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) == 2:
        file_location = sys.argv[1]
        file_content = get_book_text(file_location)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_location}...")
        print("----------- Word Count ----------")
        word_count = get_num_words(file_content)
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        all_char_count = count_char(file_content)
        for x in sort_char_count(all_char_count):
            print(f"{x['char']}: {x['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
