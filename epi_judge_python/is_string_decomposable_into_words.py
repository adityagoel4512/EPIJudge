import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    """
    decompose_ends = {}
    decompose[j]:
        for k in decompose_ends:
            if domain[k:j] in dictionary:
                # valid decomposition until j exists
                decompose_ends[j].append(k)
        

    => at decompose[len(domain)-1] contains the first index of the last dict word in various decompositions -> follow links back to 0 to see all results, caching visited to not repeat any

    aaaaaaa
    """

    decompose_ends = [[] for _ in range(len(domain)+1)]
    decompose_ends[0].append(None)
    for j in range(1,len(domain)+1):
        for prefix_end in range(j):
            cand = domain[prefix_end:j]
            if cand in dictionary and decompose_ends[prefix_end]:
                decompose_ends[j].append(prefix_end)

    result = []
    def traverse(end_idx):
        if end_idx == 0:
            return
        else:
            for start_idx in decompose_ends[end_idx][:1]:
                traverse(start_idx)
                if domain[start_idx:end_idx]:
                    result.append(domain[start_idx:end_idx])
    traverse(len(domain))
    return result


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
