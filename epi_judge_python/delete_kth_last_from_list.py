from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_node = ListNode(data=None, next=L)
    slow =  dummy_node
    fast = dummy_node
    for _ in range(k+1):
        fast = fast.next
    # L = D -> 1; k = 1
    while fast is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy_node.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
