from stats import chars_dict_to_sorted_list, get_char_count, get_word_count


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def print_report(
    file_path: str,
    num_words: int,
    sorted_char_count: list[tuple[str, int]],
) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted_char_count:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = chars_dict_to_sorted_list(char_count)

    print_report(file_path, num_words, sorted_char_count)


main()
