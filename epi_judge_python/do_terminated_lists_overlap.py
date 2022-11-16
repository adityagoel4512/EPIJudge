import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def length(head: ListNode) -> int:
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count

    def advance(head: ListNode, amount: int) -> ListNode:
        node_iter = head
        for _ in range(amount):
            node_iter = node_iter.next
        return node_iter

    len1, len2 = length(l0), length(l1)
    n1, n2 = advance(l0, max(0, len1-len2)), advance(l1, max(0, len2-len1))
    while n1 is not n2:
        n1 = n1.next
        n2 = n2.next
    return n1


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
