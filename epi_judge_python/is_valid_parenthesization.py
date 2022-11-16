from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    close_open_map = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in close_open_map:
            if not stack or stack.pop() != close_open_map[c]:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
