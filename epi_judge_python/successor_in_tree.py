import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def leftmost(node: BinaryTreeNode) -> BinaryTreeNode:
    while node.left is not None:
        node = node.left
    return node # node.left is None here, 

def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    if node.right:
        return leftmost(node.right)
    # find first parent for which node is left child not right
    while node.parent and node.parent.right is node:
        node = node.parent
    # node.parent.left is node or node.parent is None (initial node was rightmost)
    return node.parent


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
