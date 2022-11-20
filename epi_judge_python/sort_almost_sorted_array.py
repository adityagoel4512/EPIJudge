from typing import Iterator, List
import heapq
from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    min_heap = [next(sequence) for _ in range(k)]
    heapq.heapify(min_heap)
    result = []

    for num in sequence:
        heapq.heappush(min_heap, num)
        result.append(heapq.heappop(min_heap))

    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
