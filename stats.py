def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_counts(text):
    counts: dict[str, int] = {}

    for char in text:
        lowered = char.lower()
        if lowered in counts:
            counts[lowered] += 1
        else:
            counts[lowered] = 1
    return counts


def sort_on(item: tuple[str, int]) -> int:
    return item[1]


def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    result: list[tuple[str, int]] = []

    for char, count in chars_dict.items():
        result.append((char, count))

    return sorted(result, key=sort_on, reverse=True)