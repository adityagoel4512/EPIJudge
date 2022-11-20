from typing import Iterator
from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools

def find_missing_element(stream: Iterator[int]) -> int:
    stream, stream2 = itertools.tee(stream)
    counts = [0] * (1 << 16)
    mask = (1 << 16) - 1
    for num in stream:
        # get top 16 bits
        counts[num>>16] += 1
    missing_top_half = None
    for num, count in enumerate(counts):
        if count < 1 << 16:
            # check stream2
            missing_top_half = num
            break
    counts = [0] * (1 << 16)
    for num in stream2:
        if ((num>>16) & mask) == missing_top_half:
            counts[num & mask] += 1
    
    for num, count in enumerate(counts):
        if count == 0:
            return num + (missing_top_half << 16)


    return -1


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
