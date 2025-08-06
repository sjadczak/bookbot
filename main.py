import sys

from pathlib import Path

from stats import word_count, char_count, sorted_char_count_list


def get_book_text(filepath: Path) -> str:
    with open(filepath, 'rt') as f:
        contents = f.read()

    return contents

def main():
    # Check path to book passed in
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Validate that argument is a valid file path
    book_path = Path(sys.argv[1])
    if not book_path.is_file():
        print(f"Error: `{book_path}` does not exist.")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {str(book_path)}...")

    # Get file contents & calculate statistics
    text = get_book_text(book_path)
    wc = word_count(text)
    cc = char_count(text)
    sl = sorted_char_count_list(cc)

    print(f"Found {wc} total words")
    print("--------- Character Count -------")

    for char in sl:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

if __name__ == '__main__':
    main()
