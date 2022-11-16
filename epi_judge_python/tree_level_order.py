from typing import List
from collections import deque
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None:
        return []

    level_queue = deque([tree])
    result = []
    """
    result = [[314], [6,6], [271, 561, 2, 271,..]]
    level_queue = [C, F, J, O]
    next_level_queue = [C, F, J, O]

    time: O(N), space: O(M) where M is width of binary tree at maximum point
    """
    while level_queue:
        result.append([node.data for node in level_queue])
        next_level_queue = deque()
        while level_queue:
            node = level_queue.popleft()
            if node.left:
                next_level_queue.append(node.left)
            if node.right:
                next_level_queue.append(node.right)
        level_queue = next_level_queue
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
