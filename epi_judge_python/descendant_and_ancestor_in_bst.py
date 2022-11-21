import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:

    if middle is possible_anc_or_desc_0 or middle is possible_anc_or_desc_1:
        return False
    """
    paths between nodes unique, so if possible_anc_or_desc_0 is ancestor and possible_anc_or_desc_1 is desecendent then path between these will include middle, otherwise return false
    if possible_anc_or_desc_0.data > possible_anc_or_desc_1.data and possible_anc_or_desc_0 is ancestor of possible_anc_or_desc_1:
        possible_anc_or_desc_1 will lie on left subtree of possible_anc_or_desc_0

    1. find path from possible_anc_or_desc_0 to possible_anc_or_desc_1 O(logN), middle should appear en route if true
    2. if fails, try with reverse
    time complexity - O(H)
    """

    # middle distinct 
    def search(anc, desc):
        found_middle = False
        cur = anc
        while cur is not None:
            if cur is desc:
                return found_middle
            if cur is middle:
                found_middle = True
            if desc.data < cur.data:
                cur = cur.left
            else:
                # desc.data >= cur.data
                cur = cur.right
        return False

    return search(possible_anc_or_desc_0, possible_anc_or_desc_1) or search(possible_anc_or_desc_1, possible_anc_or_desc_0)


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
