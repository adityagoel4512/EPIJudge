import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:

    """
    paragraph = [a,b,a,d,b,c]
    keywords = [a,b,c]
    - brute force:
        1. at each index i,
        2. iterate back towards 0, when we see char that's the next prev word in keyword shift pointer back in keyword
        3. stop when at 0th keyword

    - one pass, create hashmap st: closest_preceding[i] is the closest index of the char preceding it to index i
        - i.e. for paragraph, closest_preceding = {0:-1, 1:0, 2:-1, 3:-1, 4:2, 5:4}
    - one step further, hashmap closest_preceding contains closest index of the first char in keywords:
        - maintain highest index for each char, -1 if preceding not set
        - closest_preceding = {'a': -1, 'b': -1, 'c': -1}
        - word_to_keyword_index = {c:i for i, c in enumerate(keywords)}
        for i, word in enumerate(paragraph):
            if word in closest_preceding:
                # keyword
                # check if preceding set
                idx = word_to_keyword_index[word]
                if idx == 0:
                    # first word
                    closest_preceding[word] = i
                else:
                    # later word, propagate up initial index
                    if closest_preceding[keywords[idx-1]] != -1:
                        closest_preceding[word] = closest_preceding[keywords[idx-1]]
                        if word == keywords[-1]:
                            result = min(result, Subarray(closest_preceding[word], i))


    
    - optimise brute force:
        1. at index i,
        2. index closest_preceding[i] and update i until we get
    
    paragraph = ['apple', 'banana', 'cat', 'apple']
    keywords = ['banana', 'apple']
    result = (-1, inf)
    word_to_keyword_index = {'banana':0, 'apple': 1}
    closest_preceding = {'banana': 1, 'apple': 1}
    """
    result = Subarray(-1, float('inf'))
    word_to_keyword_index = {w:i for i, w in enumerate(keywords)}
    closest_preceding = {w:-1 for w in keywords}
    for i, word in enumerate(paragraph):
        if word in closest_preceding:
            # keyword found
            keyword_idx = word_to_keyword_index[word]
            if keyword_idx == 0:
                # first word
                closest_preceding[word] = i
                if keyword_idx == len(keywords)-1:
                    # final word
                    result = min(result, Subarray(i, i), key=lambda s: s.end-s.start)
            else:
                if closest_preceding[keywords[keyword_idx-1]] != -1:
                    closest_preceding[word] = closest_preceding[keywords[keyword_idx-1]]
                    if keyword_idx == len(keywords)-1:
                        # final word
                        result = min(result, Subarray(closest_preceding[word], i), key=lambda s: s.end-s.start)

    return result if result[0] != -1 else Subarray(-1, -1)


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
