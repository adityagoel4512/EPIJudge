import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    """
    we can either:
        - take item now and reduce capacity
        - not take item and wait for something else
    max_value[len(items)][*] = 0
    max_value[item][remaining_capacity] = 
        if remaining_capacity >= item.weight:
            max(item.value+max_value[item+1][remaining_capacity-item.weight], max_value[item+1][remaining_capacity])
        else:
            max_value[item+1][remaining_capacity]
    
    need later item, lower capacity max_value
    m = len(items)
    n = capacity
    O(mn) time and space complexity

    => can reduce to O(n) space complexity through array reuse or dual array since we only ever access max_value[item+1] elems
        - max_value[capacity] = max_value[item+1][capacity]
    """

    max_value = [0] * (capacity+1)
    # dp = num items x capacity+1 

    for item in range(len(items)-1, -1, -1):
        max_value_new = [0] * (capacity+1)
        for remaining_capacity in range(0, capacity+1):
            if remaining_capacity < items[item].weight:
                max_value_new[remaining_capacity] = max_value[remaining_capacity]
            else:
                # we can add this potentially
                max_value_new[remaining_capacity] = max(max_value[remaining_capacity],  items[item].value+max_value[remaining_capacity-items[item].weight])
        max_value = max_value_new
    return max_value[capacity]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
