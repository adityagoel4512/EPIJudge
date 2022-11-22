from typing import List

from test_framework import generic_test


def minimum_messiness(words: List[str], line_length: int) -> int:
    """
    let M[j] be minimum messiness ending at word j not inclusive
    M[0] = 0
    M[j] = min_i<=j { M[i-1] + line_messiness(i, j-1) } [words[i:j] must constrain to line_length rule]

    operate in order from early word to later word
    """

    M = [float('inf')] * (len(words)+1)
    M[0] = 0

    for j in range(1,len(words)+1):
        cumulative_chars = 0
        for i in range(j, -1, -1):
            cumulative_chars += len(words[i-1])
            if cumulative_chars <= line_length:
                # still have enough chars for final line validity
                line_messiness = (line_length-cumulative_chars) ** 2
                M[j] = min(M[j], line_messiness + M[i-1])
            cumulative_chars += 1 # extra for space

    return M[len(words)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
