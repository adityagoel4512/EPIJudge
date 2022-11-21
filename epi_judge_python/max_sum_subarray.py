from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:

    """
    max subarray sum ending at index i inclusive:

    max_subarray_sum[i] = max(max_subarray_sum[i-1]+A[i], A[i])
    result = max(result, max_subarray_sum[i])

    => since we only need max subarray sum i-1 then we can store in single variable, leading to O(1) space
    """
    result = 0
    max_subarray_sum = 0
    for a in A:
        max_subarray_sum = max(max_subarray_sum+a, a)
        result = max(result, max_subarray_sum)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
