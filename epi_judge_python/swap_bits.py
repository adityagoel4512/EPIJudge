from test_framework import generic_test

# 01111
# 2, 4
# 00100, 10000
def swap_bits(x, i, j):
    mask_i = 1 << i
    mask_j = 1 << j
    t1 = x & mask_i
    t2 = x & mask_j
    if t1:
        x |= mask_j
    else:
        x &= ~mask_j
    if t2:
        x |= mask_i
    else:
        x &= ~mask_i
    
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
