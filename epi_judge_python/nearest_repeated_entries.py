from typing import List

from test_framework import generic_test

def find_nearest_repetition(paragraph: List[str]) -> int:
    last_idx = {}
    nearest_gap = len(paragraph)
    for i, c in enumerate(paragraph):
        if c in last_idx:
            nearest_gap = min(nearest_gap, i-last_idx[c])
        last_idx[c] = i

    return nearest_gap if nearest_gap < len(paragraph) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
