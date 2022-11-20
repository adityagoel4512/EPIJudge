from typing import List
import collections
from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    # TODO - you fill in here.
    """
    k = len(words[0])
    word_freq_map = Counter(words)
    for start_idx in range(k):
        substring_freq_map = {word:0 for word in words}
        remaining_words = len(words)
        chunked_words = [s[i:i+k] for i in range(start_idx, len(words), k)]
        for num_word, substring_word in enumerate(chunked_words):
            if substring_word in substring_freq_map:
                substring_freq_map[substring_word] += 1
                if substring_freq_map[substring_word] == word_freq_map[substring_word]:
                    remaining_words -= 1
                    if remaining_words == 0:
                        # we have a chunk
                        result.append(start_idx + k*(num_word-len(words)))
                elif substring_freq_map[substring_word] > word_freq_map[substring_word]:
                    # we have extra, need to evict to this point since we cannot have a valid concatenation
                    for word in substring_freq_map:
                        if word == substring_word:
                            substring_freq_map[word] = 1
                        else:
                            substring_freq_map[word] = 0
    N = len(s)
    m =  len(words)
    n = len(words[0])
    time complexity: O(N*m): n * m * N/n; N*m, n*N/n*m 
    """

    result = []
    word_len = len(words[0]) # length of word
    word_freq_map = collections.Counter(words)
    for start_idx in range(word_len):
        substring_freq_map = {word:0 for word in words}
        chunked_words = [s[i:i+word_len] for i in range(start_idx, len(s), word_len)]
        for i in range(len(words)-1):
            if chunked_words[i] in substring_freq_map:
                substring_freq_map[chunked_words[i]] += 1
        # substring_freq_map consists of first len(words)-1 frequencies of words in the words set (no extraneous)

        for i in range(len(words)-1, len(chunked_words)):
            new_word = chunked_words[i]
            if new_word in substring_freq_map:
                substring_freq_map[new_word] += 1
            # substring_freq_map contains len(words) entries if len(words)
            # we have valid contiguous section if 
            if substring_freq_map == word_freq_map:
                # we have valid substring
                result.append(start_idx + (word_len*(i-len(words)+1)))
            if chunked_words[i-len(words)+1] in substring_freq_map:
                substring_freq_map[chunked_words[i-len(words)+1]] -= 1

    return sorted(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
