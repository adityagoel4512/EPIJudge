from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    A.sort()
    max_constructable_value = 0
    for a in A:
        if max_constructable_value+1 < a:
            return max_constructable_value+1
        max_constructable_value += a
    return max_constructable_value+1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
