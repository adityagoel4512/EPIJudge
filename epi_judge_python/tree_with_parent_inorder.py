from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []
    """
    1. when checking node, we need to know if/what subtrees have been visited
    2. if we have visited neither: go left
    3. if we have visited left only: add to result and go right
    4. if we have visited left and right both: go to parent
    
    we could check what child visited by maintaining two pointers, one with prev accessed node and one with current
    """
    cur = tree
    prev = None

    while cur is not None:
        if prev is cur.parent:
            # came from parent, haven't visited either, go left
            if cur.left is not None:
                prev = cur
                cur = cur.left
            else:
                result.append(cur.data)
                if cur.right is not None:
                    prev = cur
                    cur = cur.right
                else:
                    prev = cur
                    cur = cur.parent
        elif prev is cur.left:
            # completed left subtree, add current then move right
            result.append(cur.data)
            if cur.right:
                prev = cur
                cur = cur.right
            else:
                prev = cur
                cur = cur.parent
        else:
            # prev is cur.right
            # completed right subtree as well, move to parent
            prev = cur
            cur = cur.parent
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
