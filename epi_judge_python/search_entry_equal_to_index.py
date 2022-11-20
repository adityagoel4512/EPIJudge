import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def search_entry_equal_to_its_index(A: List[int]) -> int:
    # A has unique entries
    """
    A = [-2,-1,0,0,2,2,3]
    L = 0
    R = 6
    M = 3
    """
    L = 0
    R = len(A)-1
    while L <= R:
        M = L + (R-L)//2
        if A[M] == M:
            return M
        elif A[M] > M:
            # means that for all i > M, A[i] > i by uniqueness of A
            R = M-1
        else:
            # A[M] < M
            # means that for all i < M, by uniqueness A[i] < i
            L = M+1
    return -1


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index,
                                            A))
    if result != -1:
        if A[result] != result:
            raise TestFailure('Entry does not equal to its index')
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure('There are entries which equal to its index')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_entry_equal_to_index.py',
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
