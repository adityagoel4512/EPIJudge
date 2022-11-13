from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in range(len(A)-1, -1, -1):
        if A[i] == 10:
            A[i] = 0
            if i == 0:
                return [1] + A
            else:
                A[i-1] += 1
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
