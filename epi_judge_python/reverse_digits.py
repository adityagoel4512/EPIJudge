from test_framework import generic_test


def reverse(x: int) -> int:
    if x < 0:
        return -reverse(-x)
    result = 0
    while x:
        d = x % 10
        result *= 10
        result += d
        x //= 10
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
