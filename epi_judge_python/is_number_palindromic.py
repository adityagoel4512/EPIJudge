from test_framework import generic_test
import math

def get_digits(x: int) -> int:
    return int(math.log(x, 10))+1


# x = 3
# num_digits = 1
# low = 2, top = 2, topval = 100

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False

    if x == 0:
        return True

    num_digits = get_digits(x)
    while num_digits > 1:
        low_digit = x % 10
        top_val = 10 ** (num_digits-1)
        top_digit = x // top_val
        if not(low_digit == top_digit):
            return False
        x -= top_val * top_digit
        x //= 10
        num_digits -= 2

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
