from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    """
    F(node)
        => F(node.left)
            => F(node.left)
                => *
                
    """
    stack = []

    def fillLeft(node: BinaryTreeNode):
        nonlocal stack
        while node is not None:
            stack.append(node)
            node = node.left

    fillLeft(tree)

    result = []
    while stack:
        # left is exhausted
        node = stack.pop()
        result.append(node.data)
        # middle is done
        # add all on right
        fillLeft(node.right)

        
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
