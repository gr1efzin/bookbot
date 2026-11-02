import sys

from stats import get_char_counts, get_word_count, chars_dict_to_sorted_list


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def print_report(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_counts(text)
    sorted_chars = chars_dict_to_sorted_list(char_count)
    print_report(book_path, word_count, sorted_chars)


main()