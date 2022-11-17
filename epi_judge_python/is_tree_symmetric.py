from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # F(l, r) = l == r and F(l.left, r.right) and F(l.right, r.left
    def helper(l, r) -> bool:
        if l is None is r:
            return True
        elif l is None and r is not None:
            return False
        elif l is not None and r is None:
            return False
        else:
            return l.data == r.data and helper(l.left, r.right) and helper(l.right, r.left)
    return tree is None or helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
