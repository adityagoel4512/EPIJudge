from typing import List

from test_framework import generic_test


def minimum_path_weight(triangle: List[List[int]]) -> int:
    # triangle[k] has k+1 entries

    """
    O(N) time, O(H) space
    row = [2]
    cur_row_weights = [15]
    """
    if not triangle:
        return 0
    cur_row_weights = triangle[-1][:]
    for r in range(len(triangle)-2, -1, -1):
        # row is above cur_row_weights
        row = triangle[r]
        # len(row) = len(cur_row_weights)-1
        for i in range(len(row)):
            cur_row_weights[i] = row[i] + min(cur_row_weights[i], cur_row_weights[i+1])
        cur_row_weights.pop()

    return cur_row_weights[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
