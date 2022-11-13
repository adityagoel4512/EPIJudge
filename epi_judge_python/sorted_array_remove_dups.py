import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    
    if not A:
        return 0

    # A = [1,2,3,3]
    # w = 3
    # r = 3
    write_index = 1
    for read_index in range(1, len(A)):
        if A[read_index] == A[read_index-1]:
            continue
        A[write_index] = A[read_index]
        write_index += 1
        
    return write_index


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
