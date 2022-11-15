from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    base = 26
    # time: O(len(t) + len(s))
    def hash(i: int, j: int, string: str) -> int:
        result = 0
        for idx in range(i, j+1):
            result = (base * result) + ord(string[idx]) - ord('A')
        return result
    if len(s) > len(t):
        return -1
    # O(len(s))
    search_hash = hash(0, len(s)-1, s)
    # O(len(s))
    rolling_text_hash = hash(0, len(s)-2, t)

    # O(len(t)), if good hash function collision only happens once in case of substring presence with no false positive.
    for i in range(len(s)-1, len(t)):
        # rolling text hash consists of hash for len(s)-1 elems, needs to be shifted and added
        rolling_text_hash = (base * rolling_text_hash) + ord(t[i]) - ord('A')
        if rolling_text_hash == search_hash and s == t[i+1-len(s):i+1]:
            return i+1-len(s)
        rolling_text_hash -= (base ** (len(s)-1)) * (ord(t[i+1-len(s)])-ord('A'))
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
