from typing import List

from test_framework import generic_test, test_utils
import heapq

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    result = []

    min_heap_queue = [(-A[0], 0)]
    while min_heap_queue and len(result) < k:
        max_val, max_idx = heapq.heappop(min_heap_queue)
        result.append(-max_val)
        left, right = 2*max_idx+1, 2*max_idx+2
        if left < len(A):
            heapq.heappush(min_heap_queue, (-A[left], left))
            if right < len(A):
                heapq.heappush(min_heap_queue, (-A[right], right))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
