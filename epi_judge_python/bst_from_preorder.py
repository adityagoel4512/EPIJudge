from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    # preorder = [root, -- left --, -- right --]
    # all elems in left are < root, all in right > root
    def helper(idx, bound_low, bound_high):
        if idx == len(preorder_sequence) or preorder_sequence[idx] < bound_low or preorder_sequence[idx] > bound_high:
            return idx, None
        # otherwise bound_low <= preorder_sequence[idx] <= bound_high
        root = BstNode(data=preorder_sequence[idx])
        right_idx, left_node = helper(idx+1, bound_low, root.data)
        subtree_idx, right_node = helper(right_idx, root.data, bound_high)
        root.left = left_node
        root.right = right_node
        return subtree_idx, root

    _, root = helper(0, float('-inf'), float('inf'))
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
