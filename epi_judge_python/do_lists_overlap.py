import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def is_cyclic(l: ListNode) -> Optional[ListNode]:
    slow = l
    fast = l
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return fast
    return None

def length(l: ListNode) -> int:
    count = 0
    while l is not None:
        count += 1
        l = l.next
    return count

def advance(l: ListNode, amount: int) -> ListNode:
    for _ in range(amount):
        l = l.next
    return l

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    c0, c1 = is_cyclic(l0), is_cyclic(l1)
    if c0 is None and c1 is None:
        # find using linked list approach non-cyclic
        cnt0, cnt1 = length(l0), length(l1)
        adv0, adv1 = advance(l0, max(0, cnt0-cnt1)), advance(l1, max(0, cnt1-cnt0))
        while adv0 is not adv1:
            adv0 = advance(adv0, 1)
            adv1 = advance(adv1, 1)
        return adv0
    elif c0 is None and c1 is not None:
        return None
    elif c1 is None and c0 is not None:
        return None
    else:
        if c0 is c1:
            return c0
        # check if same cycle
        iter_node = c0.next
        while iter_node is not c0:
            if iter_node is c1:
                return iter_node
            iter_node = advance(iter_node, 1)
        return None

@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
