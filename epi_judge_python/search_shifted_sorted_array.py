from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    """
    A[k+1], A[k+2], ..., A[n-1], *A[0], A[1], ..., A[k]
    while L < R:
        if A[R] < A[M]:
            # A[M:R+1] contains midpoint
            L = M
        elif A[M] < A[R]:
            # A[M:R+1] does not contain midpoint
            R = M
            
            
        if A[M] < A[L]:
            smallest cannot be in left
            shift right, L = M
        else:
            # A[M] >= A[L]
            smallest cannot be in right
            shift left, R = M
    """
    L = 0
    R = len(A)-1
    while L < R:
        M = L + (R-L)//2
        if A[R] < A[M]:
            L = M+1
        else:
            R = M
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
