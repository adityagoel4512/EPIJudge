import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    even_idx = 0
    odd_idx = len(A)-1

    def swap(i, j):
        A[i], A[j] = A[j], A[i]

    while even_idx <= odd_idx:
        # if even_idx elem is even, move ptr forward, otherwise swap with odd ptr and move that back
        # in this way, progress is constantly made (at end of iteration, odd_idx decreased or even_idx increased)
        if A[even_idx] & 1:
            swap(even_idx, odd_idx)
            odd_idx -= 1
        else:
            even_idx += 1

@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
