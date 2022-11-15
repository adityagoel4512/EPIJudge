from test_framework import generic_test
import math

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    is_negative = num_as_string[0] == '-'

    base_10 = 0
    digits = {str(d): d for d in range(10)}
    for i, c in enumerate(('A', 'B', 'C', 'D', 'E', 'F')):
        digits[c] = 10 + i

    str_from_digit = {v:k for k, v in digits.items()}

    """
    num_as_string = 615
    b1 = 7
    b2 = 13
    base_10 = 7
    result = [1, A, 7]
    max_digits = 2
    
    """
    

    for d in num_as_string[is_negative:]:
        base_10 = b1 * base_10 + digits[d]

    if base_10 == 0:
        return '0'
        
    result = [] if not is_negative else ['-']
    max_digits = math.floor(math.log(base_10, b2))
    for pow in range(max_digits, -1, -1):
        digit, base_10 = divmod(base_10, b2**pow)
        result.append(str_from_digit[digit])

    return ''.join(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
