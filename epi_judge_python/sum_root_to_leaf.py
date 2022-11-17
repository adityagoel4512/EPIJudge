from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # provide prefix sum in argument parameter
    # F(null) = return prefix sum
    # F(data, left, right) = return left + right

    # time: O(N), reach every node once with a preorder type traversal
    # space: O(H), as maximum function call depth at any point is the height of the tree

    def helper(node: BinaryTreeNode, prefixSum: int) -> int:
        prefixSum = (prefixSum << 1) + node.data
        if node.left is None and node.right is None:
            return prefixSum
        result = 0
        if node.left:
            result += helper(node.left, prefixSum)
        if node.right:
            result += helper(node.right, prefixSum)
        return result

    return helper(tree, 0) if tree is not None else 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
