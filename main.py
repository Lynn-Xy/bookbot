from stats import get_word_count, get_char_count, get_report
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return book_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <book_path>")
        sys.exit(1)
    book_path = f"{sys.argv[1]}"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    report = get_report(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in report:
        for key, value in item.items():  # Each item is a single-key dictionary
            print(f"{key}: {value}")
    
    print("============= END ===============")

main()