from typing import Iterator, List
import heapq
from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    top_half = [] # k nums, top half
    bottom_half = [] # k or k+1 nums, bottom half
    # total 2k or 2k+1 nums processed
    result = []

    """
    sequence = [1,0,3,5,2,0,1]
    top_half = [3, 5]
    bottom_half = [0, -1, -2]
    result = [1, 0.5, 1,2]
    num = 2
    """
    for num in sequence:
        if not bottom_half or num <= -bottom_half[0]:
            heapq.heappush(bottom_half, -num)
        else:
            heapq.heappush(top_half, num)

        if len(bottom_half) > len(top_half)+1:
            heapq.heappush(top_half, -heapq.heappop(bottom_half))
        elif len(top_half) >= len(bottom_half)+1:
            heapq.heappush(bottom_half, -heapq.heappop(top_half))
        
        if len(bottom_half) == len(top_half):
            result.append((-bottom_half[0] + top_half[0])/2)
        else:
            result.append(-bottom_half[0])
        
    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
