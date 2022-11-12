from test_framework import generic_test

def get_lsb(x):
    return x & -x

def closest_int_same_bit_count(x: int) -> int:
    # rightmost consecutive bits that are different swap
    rightmost_set = get_lsb(x)
    if rightmost_set and rightmost_set & ~1:
        # swap forward
        x |= rightmost_set >> 1
        x &= ~rightmost_set
    else:
        # swap back
        # find rightmost 0
        rightmost_unset = get_lsb(~x)
        x |= rightmost_unset
        x &= ~(rightmost_unset >> 1)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
