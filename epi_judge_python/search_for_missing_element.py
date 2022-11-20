import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    # place k at A[k], we will find one A[i] in end st. A[i] != i: missing is i, duplicate is A[i]
    """
    mark visited by setting A[i] = -i when we have A[i] = i

    if A[i] == -i: continue
    else:
        swap i, A[i]th elems until encountering negative indicating already visited or find A[i] == i
        -> if we encounter already visited, proceed
        -> otherwise, mark A[i] = -i to indicate this has been set
        then continue
    """
    for i in range(len(A)):
        while i != A[i] and A[i] >= 0 and A[A[i]] >= 0:
            A[A[i]], A[i] = -A[i]-1, A[A[i]]
        if i == A[i]:
            A[i] = -i-1
    for i in range(len(A)):
        if A[i] != -i-1:
            return DuplicateAndMissing(duplicate=A[i], missing=i)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
