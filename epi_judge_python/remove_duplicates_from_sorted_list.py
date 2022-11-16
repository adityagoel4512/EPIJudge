from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    # equal elems will be adjacent
    # 1. for each sequence of unique nums, find start and end node, end is not same num
    # 2. start.next = end
    # 3. move on

    node_iter = L

    while node_iter is not None:
        # node_iter sits at start of new sequence
        start_node = node_iter
        while node_iter is not None and node_iter.data == start_node.data:
            node_iter = node_iter.next

        # node_iter is None (end of list) or has different data value
        start_node.next = node_iter


    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
