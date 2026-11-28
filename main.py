from stats import get_word_count


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")


main()
