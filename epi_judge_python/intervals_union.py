import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []
    intervals.sort(key=lambda interval: (interval.left.val, not interval.left.is_closed, interval.right.val, not interval.right.is_closed))
    result = [intervals[0]]

    for interval in intervals:
        current_interval_right = result[-1].right
        # current_interval_left.val <= interval.left.val and if current_interval.left.val == interval.left.val and current_interval.left.is_closed (closed precedes)
        if interval.left.val < current_interval_right.val or (interval.left.val == current_interval_right.val and (current_interval_right.is_closed or interval.left.is_closed)):
            # overlap, intersection, accumulate into current interval
            new_current_interval_right = max(current_interval_right, interval.right, key=lambda i: (i.val, i.is_closed))
            result[-1] = Interval(result[-1].left, new_current_interval_right)
        else:
            # no overlap, start new current_interval
            result.append(interval)
    return result 


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
