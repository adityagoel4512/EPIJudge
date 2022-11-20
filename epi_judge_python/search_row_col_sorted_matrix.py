from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    row = 0
    col = len(A[0])-1

    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif x < A[row][col]:
            col -= 1
        else:
            # x > A[row][col]
            row += 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
