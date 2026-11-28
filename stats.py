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
