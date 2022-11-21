from typing import List
from test_framework import generic_test


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]
                                           ) -> int:
    """
    brute force:
    check each possible triple O(mnp)

    improvement 1:
    use sortedness: next candidate is num array with smallest

    if we have a, b, c candidate with a <= b <= c, then: 
        - no point increasing c as this will increase closeness
        - no point varying b
        - increasing a would improve things while it's minimum
    new minimum will do the same
    """

    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
