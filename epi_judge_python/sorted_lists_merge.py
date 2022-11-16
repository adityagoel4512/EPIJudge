from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(data=0, next=None)
    end = dummy
    while L1 is not None and L2 is not None:
        if L1.data < L2.data:
            end.next = L1
            L1 = L1.next
        else:
            end.next = L2
            L2 = L2.next
        end = end.next
    if L1 is None:
        end.next = L2
    if L2 is None:
        end.next = L1

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
