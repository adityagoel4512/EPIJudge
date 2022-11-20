from typing import List
import heapq
from test_framework import generic_test


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # merge on different subarrays

    if len(A) < 2:
        return A

    def build_iterator(start_idx: int, end_idx: int, increasing: bool):
        offset = 1 if increasing else -1
        start = start_idx if increasing else end_idx
        end = end_idx+1 if increasing else start_idx-1
        for i in range(start, end, offset):
            yield A[i]

    iters = []
    prev_idx = 0
    increasing = A[1] >= A[0]
    for i in range(1, len(A)):
        if increasing and A[i-1] > A[i]:
            # increased until A[i-1]
            iters.append(build_iterator(prev_idx, i-1, increasing))
            prev_idx = i # decreasing from A[i] to ?
            increasing = False
        elif not increasing and A[i-1] < A[i]:
            # decreased until A[i-1]
            iters.append(build_iterator(prev_idx, i-1, increasing))
            prev_idx = i # increasing from A[i] to ?
            increasing = True
    
    iters.append(build_iterator(prev_idx, len(A)-1, increasing))
    # print([list(it) for it in iters])
    result = []
    min_heap = []
    for i, it in enumerate(iters):
        try:
            num = next(it)
            min_heap.append((num, i))
        except StopIteration:
            continue

    heapq.heapify(min_heap)
    while min_heap:
        num, it = heapq.heappop(min_heap)
        result.append(num)
        try:
            new_num = next(iters[it])
            heapq.heappush(min_heap, (new_num, it))
        except StopIteration:
            continue

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
