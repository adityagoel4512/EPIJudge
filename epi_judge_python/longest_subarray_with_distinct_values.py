from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    """
    at index k, longest subarray with distinct entries:
        - if A[k] in longest subarray with distinct ending at A[k-1], then the answer is from the index after A[k] in the subarray endin at A[k-1] to k
        - otherwise: the same as before with A[k] added
    if A[i:j] is distinct entries:
        if A[j] not in A[i:j] then we can say A[i:j+1] is also distinct
        else:
            #A[j] in A[i:j] then we need to move i forward until the element after A[j] to maintain distinct entries property

    A = [f,s,f,e,t,w,e,n,w,e]
    subarray_entries = {t,w,e}
    left = 4
    right = 6
    result = 5
    """
    left = 0
    subarray_entries = set()
    result = 0
    for right in range(len(A)):
        while A[right] in subarray_entries:
            # shift left until property remaintained
            subarray_entries.remove(A[left])
            left += 1
        subarray_entries.add(A[right])
        # A[left:right+1] are unique
        result = max(result, right-left+1)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
