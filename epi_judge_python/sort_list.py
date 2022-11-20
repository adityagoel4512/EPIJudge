from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    # merge sort
    if L is None:
        return None
    elif L.next is None:
        return L
    else:
        # find middle and split
        pre_slow = None
        slow = L
        fast = L
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            pre_slow = slow
            slow = slow.next
        # pre_slow is midpoint
        left = L
        right = slow
        # split link between left and right
        pre_slow.next = None
        left = stable_sort_list(left)
        right = stable_sort_list(right)
        # merge sorted left and right

        result = ListNode(None, None)
        tail = result
        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        elif right:
            tail.next = right
        return result.next

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
