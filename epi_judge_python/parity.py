from test_framework import generic_test


def parity(x: int) -> int:
    res = 0
    while x:
        res ^= 1
        x &= x-1
    return res

# 32 bit
def parity32bit(x: int) -> int:
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
