from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    
    def dfs(node: BinaryTreeNode, k: int) -> bool:
        if node.left is None and node.right is None:
            return k == node.data

        return (node.left is not None and dfs(node.left, k-node.data)) or (node.right is not None and dfs(node.right, k-node.data))
            
    if tree is None:
        return remaining_weight == 0
    else:
        return dfs(tree, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
