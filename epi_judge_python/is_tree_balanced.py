from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple

BalancedHeight = namedtuple('BalancedHeight', ('balanced', 'height'))
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # 1. traverse very node
    # 2. get left height and right height
    # 3. check if diff by more than 1
    # height(node) = 1 + max(height(node.left, node.right))
    # balanced(node) = abs(height(node.left) - height(node.right)) <= 1 and balanced(node.left) and balanced(node.right)
    def balanced(node: BinaryTreeNode) -> BalancedHeight:
        if node is None:
            return BalancedHeight(balanced=True, height=-1)
        left, right = balanced(node.left), balanced(node.right)
        height = max(left.height, right.height)+1
        balanced_status = abs(left.height - right.height) <= 1 and left.balanced and right.balanced
        return BalancedHeight(balanced_status, height)
    return balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
