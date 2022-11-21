from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def gen(l, r, prefix):
        if l > r or l < 0 or r < 0:
            # used a ) before ( operning, invalid
            return
        elif l == 0 and r == 0:
            result.append(''.join(prefix))
        else:
            # l <= r
            # try l first
            prefix.append('(')
            gen(l-1, r, prefix)
            prefix.pop()

            prefix.append(')')
            gen(l, r-1, prefix)
            prefix.pop()
            return

    result = []
    gen(num_pairs, num_pairs, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
