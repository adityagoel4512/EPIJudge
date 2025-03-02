import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    result = []
    def helper(node: BstNode):
        if node is None:
            return
        else:
            # node has data
            if interval.left <= node.data <= interval.right:
                helper(node.left)
                result.append(node.data)
                helper(node.right)
            elif node.data < interval.left:
                helper(node.right)
            else:
                # node.data > interval.right
                helper(node.left)
    helper(tree)
    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
