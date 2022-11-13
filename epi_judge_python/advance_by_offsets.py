from typing import List

from test_framework import generic_test

# A = [3,3,1,0,2,0,1], i = 5
# furthest_index = 7
def can_reach_end(A: List[int]) -> bool:
    furthest_index = 0
    for i in range(len(A)):
        if furthest_index < i:
            return False
        furthest_index = max(A[i] + i, furthest_index)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
