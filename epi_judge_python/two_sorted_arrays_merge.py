from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    A_idx = m-1
    B_idx = n-1

    """
    A = [3,13,17,_,_,_,_,_]
    B = [3,7,11,18]
    write_idx = 6
    A_idx = 2
    B_idx = 3
    """
    for write_idx in range(m+n-1, -1, -1):
        if A_idx < 0:
            A[write_idx] = B[B_idx]
            B_idx -= 1
        elif B_idx < 0:
            A[write_idx] = A[A_idx]
            A_idx -= 1
        elif A[A_idx] > B[B_idx]:
            A[write_idx] = A[A_idx]
            A_idx -= 1
        else:
            A[write_idx] = B[B_idx]
            B_idx -= 1
    
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
