from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    result = []
    A_idx, B_idx = 0, 0

    """
    A = [2,3,3,5,5,6,7,7,8,12*], len(A) = 10
    B = [5,5,6,8,8,9,10,10*], len(B) = 8
    result = [5,6,8,]
    A_idx = 9
    B_idx = 8
    """
    while A_idx < len(A) and B_idx < len(B):
        if A[A_idx] < B[B_idx]:
            A_idx += 1
        elif B[B_idx] < A[A_idx]:
            B_idx += 1
        else:
            # A[A_idx] == B[B_idx]
            if not result or result[-1] != A[A_idx]:
                result.append(A[A_idx])
            A_idx += 1
            B_idx += 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
