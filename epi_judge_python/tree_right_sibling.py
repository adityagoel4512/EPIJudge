import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.

def sibling_iterator(node: BinaryTreeNode):
    while node is not None:
        yield node
        node = node.next

def construct_right_sibling(tree: BinaryTreeNode) -> None:
    # need to tie left most at each level in right subtree with right most at each level in left subtree
    # return leftmost
    # F(node):
    #  leftmostright = F(node.right)

    cur_level_head = tree 

    """
    BST with pointers/linked list inside the tree itself
    """

    while cur_level_head is not None:

        next_level_head = None
        next_level_tail = None

        def append_to_next_level(node: BinaryTreeNode):
            nonlocal next_level_head
            nonlocal next_level_tail
            if next_level_head is None:
                next_level_head = node 
                next_level_tail = node
            else:
                next_level_tail.next = node
                next_level_tail = next_level_tail.next

        for parent in sibling_iterator(cur_level_head):
            if parent.left is not None:
                append_to_next_level(parent.left)
            if parent.right is not None:
                append_to_next_level(parent.right)
        cur_level_head = next_level_head

    return


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
