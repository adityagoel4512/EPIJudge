from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def helper(L, R, node):
        if node is None:
            return True

        return L <= node.data <= R and helper(L, node.data, node.left) and helper(node.data, R, node.right)

    return helper(float('-inf'), float('inf'), tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
