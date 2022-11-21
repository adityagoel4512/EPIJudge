from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    """
    pal(i) = 
        result = []
        for k in range(i+1, len(text)+1):
            if text[i:k] is palindrome:
                results.extend([text[i:k]] + all pal(k))
            else:
                # i:k not palindrome
                
    """
    def is_palindromic(i, j):
        while i < j:
            if text[i] != text[j]:
                return False
            i += 1
            j -= 1
        return True

    def pal(i, prefix):
        if i == len(text):
            result.append([chunk[:] for chunk in prefix])
        else:
            for k in range(i+1, len(text)+1):
                if is_palindromic(i, k-1):
                    prefix.append(text[i:k])
                    pal(k, prefix)
                    prefix.pop()
    result = []
    pal(0, [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
