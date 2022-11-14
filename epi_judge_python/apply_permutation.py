from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    def swap(i: int, j: int, arr: List[int]) -> None:
        arr[i], arr[j] = arr[j], arr[i]
    # a=>c=>b=>a*
    # A       = [a,b,c,d]
    # perm    = [2,0,1,3]
    # => b=>0  [b,c,a,d]
    # src_idx = 0
    # O(N) time, O(1) space
    src_idx = 0
    while src_idx < len(A):
        if perm[src_idx] == src_idx:
            src_idx += 1
        else:
            swap(src_idx, perm[src_idx], A)
            swap(src_idx, perm[src_idx], perm)

    return

def inverse_permutation(perm: List[int]) -> None:
    # this is really a graph problem, where we need to point edges in opposite direction in-place, 
    # need to know when node visited to avoid loops so use negative num

    # perm = [1,0,4,2,3]                        => [1,0,4,2,3]
    # start_idx = 0
    # perm[i] => move i elem to perm[i], in inverse: move perm[i]th elem to i elem
    # 1. construct swaps from perm[i]th index with ith index, for each i in len(perm)
    #   2. mark -1-new_res to indicate done, continue swaps until cycle of elem indices done

    for src, dest in enumerate(perm):
        while dest >= 0:
            # unvisited
            tmp_src, tmp_dest = dest, perm[dest]
            perm[dest] = -1-src
            src, dest = tmp_src, tmp_dest
    for i in range(len(perm)):
        perm[i] = -perm[i]-1
            



def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
