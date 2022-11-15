from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    prefix = []
    results = []

    def chunk_in_range(chunk: str) -> bool:
        if chunk[0] == '0' and len(chunk) > 1:
            return False
        return 0 <= int(chunk) <= 255

    def valid_in_range(k: int, i: int):
        if k == 0 and i == len(s):
            results.append('.'.join(prefix))
            return

        if k < 0 or i >= len(s):
            return
        

        # check if we can append to prefix with valid num
        if prefix and chunk_in_range(prefix[-1] + s[i]):
            prefix[-1] = prefix[-1] + s[i]
            valid_in_range(k, i+1)
            prefix[-1] = prefix[-1][:len(prefix[-1])-1]
        if not prefix or chunk_in_range(prefix[-1]):
            prefix.append(s[i])
            valid_in_range(k-1, i+1)
            prefix.pop()
    
    # s = '1.9216811'
    # prefix = []
    # results = []
    valid_in_range(4, 0)
    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
