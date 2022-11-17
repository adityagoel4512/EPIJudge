import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def length(node: BinaryTreeNode) -> int:
    count = 0
    while node is not None:
        node = node.parent
        count += 1
    return count

def advance(node: BinaryTreeNode, amount: int) -> BinaryTreeNode:
    for _ in range(amount):
        node = node.parent
    return node
    
def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # two linked lists
    len0, len1 = length(node0), length(node1)
    node0, node1 = advance(node0, max(0, len0-len1)), advance(node1, max(0, len1-len0))
    while node0 is not node1:
        node1 = node1.parent
        node0 = node0.parent
    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
