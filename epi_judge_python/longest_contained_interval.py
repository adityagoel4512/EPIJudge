from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    """
    # n, n+1, ...
    
    A = [3,-2,]
    """

    elems = set(A)
    result = 0
    while elems:
        num = elems.pop()
        longest = 1
        lower = num-1
        while lower in elems:
            elems.remove(lower)
            lower -= 1
            longest += 1
        upper = num+1
        while upper in elems:
            elems.remove(upper)
            upper += 1
            longest += 1
        result = max(result, longest)

        
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
