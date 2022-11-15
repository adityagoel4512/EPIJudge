import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # do removal first, and count how many 'a's present since that denotes the expansion amount
    write_index = 0
    num_insertions = 0
    for read_index in range(size):
        if s[read_index] != 'b':
            s[write_index] = s[read_index]
            write_index += 1
        if s[read_index] == 'a':
            num_insertions += 1
    # write index will finish one after final element
    # iterate backwards from write_index + num_insertions - 1 inclusive to front
    #   - when not 'a', copy letter back to write index
    #   - when 'a', write 'd' and advance write index extra and write 'd' again
    #  write index will always precede read index sufficiently because it is num_insertions behind

    # [a, a, c, a, c] and 4
    # num_insertions  = 2
    # write_index = 3
    # end_of_array = 2
    # final_length = 5
    # read_index = 1
    end_of_array = write_index-1
    write_index = write_index + num_insertions - 1
    final_length = write_index + 1
    for read_index in range(end_of_array, -1, -1):
        if s[read_index] == 'a':
            s[write_index] = 'd'
            write_index -= 1
            s[write_index] = 'd'
            write_index -= 1
        else:
            s[write_index] = s[read_index]
            write_index -= 1

    return final_length


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
