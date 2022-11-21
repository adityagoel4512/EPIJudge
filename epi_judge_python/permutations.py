from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    """
    Time complexity:
    Base case complexity: O(n)
    Base case num calls: n!
    Recursive case complexity: O(1)
    Recursive case num calls: 1 + n + n*(n-1) + n*(n-1)*(n-2) + ... + n! = (e-1)*n!
    => n!n + n! => (n+1)n!
    """
    def helper(i):
        if i == len(A):
            result.append(A[:])
        else:
            for k in range(i, len(A)):
                A[i], A[k] = A[k], A[i]
                helper(i+1)
                A[k], A[i] = A[i], A[k]
    result = []
    helper(0)
    return result
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
