from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    result = []

    def isdigit(c: str) -> bool:
        return ord('0') <= ord(c) <= ord('9')

    idx = 0
    while idx < len(s):
        # idx start at an int array now
        count = 0
        while isdigit(s[idx]):
            count = 10*count + int(s[idx])
            idx += 1
        
        # idx is at a character
        result.append(s[idx]*count)
        idx += 1

    return ''.join(result)


def encoding(s: str) -> str:
    """
    s = eeegffffee
    result = [2,e,1,g,]
    cur_cnt = 1
    idx = 4
    """
    idx = 0
    result = []
    while idx < len(s):
        cur_cnt = 1
        while idx < len(s)-1 and s[idx] == s[idx+1]:
            cur_cnt += 1
            idx += 1
        # idx is now at final char
        result.append(str(cur_cnt))
        result.append(s[idx])
        idx += 1

    return ''.join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
