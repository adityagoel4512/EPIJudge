from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    """
    LS[i] is the longest non decreasing subsequence ending at index i, depemds on LS of previous elems that are smaller or equal
    LS[i] = 1 + max(LS[k] for k in range(i) if A[k] <= A[i])

    O(N)

    O(NlogN) solution:
    - maintain non-decreasing subsequence
    - if A[i] < seq[0]: seq[0] = A[i]
    - elif A[i] > seq[-1]: seq.append(A[i])
    - else: g_idx = bsearch(seq, A[i]); seq[g_idx] = A[i]
    """
    def bsearch(val):
        L = 0
        R = len(lis)-1
        while L <= R:
            M = L + (R-L)//2
            if lis[M] <= val:
                L = M+1
            else:
                # A[M] > val
                if M == 0 or lis[M-1] <= val:
                    return M
                R = M-1
        return -1

    lis = [A[0]]
    for i in range(1, len(A)):
        if A[i] < lis[0]:
            lis[0] = A[i]
        elif A[i] >= lis[-1]:
            lis.append(A[i])
        else:
            lis[bsearch(A[i])] = A[i]

    return len(lis)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
