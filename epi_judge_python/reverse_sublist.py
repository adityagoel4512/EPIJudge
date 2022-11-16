from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if L is None:
        return None
    dummy_head = ListNode(data=None, next=L)
    preceding_start_node = dummy_head
    for _ in range(start-1):
        preceding_start_node = preceding_start_node.next

    # find end node and reverse links en route
    slow = preceding_start_node.next
    fast = preceding_start_node.next.next
    for _ in range(finish-start):
        next_fast = fast.next
        fast.next = slow
        slow = fast
        fast = next_fast

    start_node = preceding_start_node.next
    preceding_start_node.next = slow
    start_node.next = fast


    # start = 2, finish = 4
    # dummy head -> 11 -> 3 <- 5 <- 7    2
    # preceding_start_node = 11 ->
    # slow = 7 ->
    # fast = 2 ->
    # next_fast = 2 ->


    # node_number = start,
    # start_node is 

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
