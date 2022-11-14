from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # 1. iterate from back, 
    # 2. find first descending adjacent numbers: 
    #   - swap smaller elem in descending relationship with the smallest number larger than it in the preceding ascending section
    #   - sort / reverse elems

    # [x, a, b, c, d]
    # a >= b >= c >= d
    # x < a
    # 1. find element in a,b,c,d immediately larger than x
    # 2. swap x with it
    # 3. reverse elems after x
    
    def swap(i: int, j: int) -> None:
        perm[i], perm[j] = perm[j], perm[i]

    def reverse(i: int, j: int) -> None:
        while i < j:
            swap(i, j)
            i += 1
            j -= 1
    
    # perm = [1,3,1,2]
    # i = 1
    # j = 2
    for i in range(len(perm)-2, -1, -1):
        if perm[i] < perm[i+1]:
            # got smaller elems, perm[i+1:] is in ascending order
            # find elem just larger than it
            for j in range(len(perm)-1, i, -1):
                if perm[j] > perm[i]:
                    # perm[j] is number just larger
                    swap(i, j)
                    reverse(i+1, len(perm)-1)
                    return perm
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
