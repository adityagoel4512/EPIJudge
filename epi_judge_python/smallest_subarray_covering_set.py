import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    left = 0
    smallest_subarray = Subarray(-1, len(paragraph)+1)
    remaining_to_cover = len(keywords)
    covered_keywords = collections.Counter()
    for right, word in enumerate(paragraph):
        # not covering all currently
        if word in keywords:
            # add to covered
            covered_keywords[word] += 1
            if covered_keywords[word] == 1:
                remaining_to_cover -= 1
            while left <= right and remaining_to_cover == 0:
                # covering everything here
                smallest_subarray = min(smallest_subarray, Subarray(left, right), key=lambda s:s.end-s.start)
                if paragraph[left] in covered_keywords:
                    covered_keywords[paragraph[left]] -= 1
                    if covered_keywords[paragraph[left]] == 0:
                        remaining_to_cover += 1
                left += 1



    return smallest_subarray if smallest_subarray.start != -1 else Subarray(-1, -1)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
