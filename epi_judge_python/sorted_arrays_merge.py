from typing import List
import heapq
from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    result = []
    iters = list(map(iter, sorted_arrays))
    min_heap = []
    for i, array in enumerate(sorted_arrays):
        if array:
            min_heap.append((next(iters[i]), i))
    heapq.heapify(min_heap)

    while min_heap:
        min_value, arr_idx = heapq.heappop(min_heap)
        result.append(min_value)
        try:
            heapq.heappush(min_heap, (next(iters[arr_idx]), arr_idx))
        except StopIteration:
            continue

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
