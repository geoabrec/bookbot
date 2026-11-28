def get_word_count(book_text: str) -> int:
    words = book_text.split()
    return len(words)


def get_char_count(book_text: str) -> dict[str, int]:
    lower_case_text = book_text.lower()
    char_count = {}

    for c in lower_case_text:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count


def sort_on(char_pair: tuple[str, int]) -> int:
    return char_pair[1]


def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    char_tuple_list = []
    for char, count in char_dict.items():
        char_tuple_list.append((char, count))
    sorted_char_tuple_list = sorted(char_tuple_list, reverse=True, key=sort_on)

    return sorted_char_tuple_list
