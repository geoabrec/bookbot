from stats import chars_dict_to_sorted_list, get_char_count, get_word_count


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = chars_dict_to_sorted_list(char_count)

    print(f"Found {num_words} total words")
    print(sorted_char_count)


main()
