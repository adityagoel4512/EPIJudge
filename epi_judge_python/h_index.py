from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    citations.sort(reverse=True)
    result = 0
    for i, num in enumerate(citations):
        if num >= (i+1):
            result = i+1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
