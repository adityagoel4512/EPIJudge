from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_count = {}
    for c in letter_text:
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1

    for c in magazine_text:
        if c in letter_count:
            letter_count[c] -= 1
            if letter_count[c] == 0:
                del letter_count[c]

    return not letter_count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
