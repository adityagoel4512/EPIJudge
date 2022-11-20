from typing import List
import heapq
from test_framework import generic_test
import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # TODO - you fill in here.
    return find_kth_largest_quickselect(k, A)


def find_kth_largest_quickselect(k: int, A: List[int]) -> int:

    def swap(i, j):
        A[i], A[j] = A[j], A[i]

    def partition(i, j, partition_idx):
        partition_value = A[partition_idx]
        swap(j, partition_idx)
        # partition, A[i], A[i+1], ..., A[j-1], A[j]
        write_idx = i
        for read_idx in range(i, j):
            if A[read_idx] > partition_value:
                # write_idx is at first be <= to partition_value
                swap(write_idx, read_idx)
                write_idx += 1
        swap(j, write_idx)
        return write_idx

    L = 0
    R = len(A)-1
    while L <= R:
        partition_idx = random.randint(L, R)
        pivot_idx = partition(L, R, partition_idx)
        if pivot_idx == k-1:
            return A[pivot_idx]
        elif pivot_idx < k-1:
            # shift right
            L = pivot_idx + 1
        else:
            # pivot_idx > k-1, shift left
            R = pivot_idx-1




def find_kth_largest_heap(k: int, A: List[int]) -> int:
    min_heap = A[:k]
    heapq.heapify(min_heap)
    for i in range(k, len(A)):
        # min_heap has k elems
        if min_heap[0] < A[i]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, A[i])
    return min_heap[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
