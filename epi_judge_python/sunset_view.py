from typing import Iterator, List
from collections import namedtuple
from test_framework import generic_test

IdxHeight = namedtuple('IdxHeight', ('idx', 'height'))

def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    stack = []

    for idx, height in enumerate(sequence):
        while stack and stack[-1].height <= height:
            stack.pop()
        stack.append(IdxHeight(idx=idx, height=height))
    return [idx_height.idx for idx_height in reversed(stack)]

def examine_buildings_with_sunset_west_to_east(west_east_iterator: Iterator[int]) -> List[int]:
    max_height = -1
    result = []
    for idx, height in enumerate(west_east_iterator):
        if height > max_height:
            result.append(idx)
            max_height = height
    return result

def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
