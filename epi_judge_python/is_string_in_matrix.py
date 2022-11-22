from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    """
    if pattern_idx == len(pattern):
        return True
    elif i, j not in grid:
        return False
    else:
        contained[pattern_idx, i, j] = grid[i][j] == pattern[pattern_idx] and (contained[pattern_idx+1, i+1, j] or contained[pattern_idx+1, i-1, j] or contained[pattern_idx+1, i, j+1] or contained[pattern_idx+1, i, j-1])
        return contained[pattern_idx, i, j]

    O(mnp) time and space complexity
    """

    offsets = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def contains(pattern_idx, row, col, cache):
        if pattern_idx == len(pattern):
            return True
        elif (pattern_idx, row, col) in cache:
            return cache[(pattern_idx, row, col)]
        elif row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return False
        elif grid[row][col] != pattern[pattern_idx]:
            return False
        else:
            # 0 <= row < len(grid) and 0 <= col < len(grid[0])
            cache[(pattern_idx, row, col)] = any(contains(pattern_idx+1, row+r, col+c, cache) for r, c in offsets)
            return cache[(pattern_idx, row, col)]

    return any(contains(0, row, col, {}) for row in range(len(grid)) for col in range(len(grid[0])))
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
