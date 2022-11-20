from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    L = 0
    R = len(A)-1

    """
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    L = 6
    R = 6
    M = 5
    """
    while L <= R:
        M = L + (R-L)//2
        if A[M] == k:
            if M == 0 or A[M-1] != A[M]:
                return M
            else:
                R = M-1
        elif A[M] < k:
            L = M+1
        else:
            # A[M] > k
            R = M-1
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
