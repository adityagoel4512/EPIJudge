from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    """
    inorder: left - root - right
    preorder: root - left - right

    T(N) = N + 
    T(1) = 1

    1. root is head of preorder list
    2. lookup root index in inorder (use dict)
    3. recurse into left and right subarrays, returning completed index in preorder section (like parser)

    """

    inorder_idx_map = {data:idx for idx, data in enumerate(inorder)}

    def helper(preorder_idx: int, inorder_idx_start: int, inorder_idx_end: int):
        # inorder_idx_start is start index (inclusive) of inorder section, inorder_idx_end is inclusive end
        if inorder_idx_start > inorder_idx_end:
            return preorder_idx, None
        
        root = BinaryTreeNode(data=preorder[preorder_idx])
        root_idx = inorder_idx_map[root.data]

        left_completion_idx, root.left = helper(preorder_idx+1, inorder_idx_start, root_idx-1)
        right_completion_idx, root.right = helper(left_completion_idx, root_idx+1, inorder_idx_end)
        return right_completion_idx, root

    _, result = helper(0, 0, len(inorder)-1)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
