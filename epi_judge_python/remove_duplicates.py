import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __lt__(self, other) -> bool:
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)


def eliminate_duplicate(A: List[Name]) -> None:
    A.sort()
    write_idx = 1
    # write_idx is the position of the next duplicate to write over with distinct elem
    for read_idx in range(1, len(A)):
        if A[read_idx].first_name != A[read_idx-1].first_name:
            A[write_idx] = A[read_idx]
            write_idx += 1
        # write index doesn't progress if same first name

    # pop extras
    for _ in range(len(A)-write_idx):
        A.pop()
    return


@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([
        e == r.first_name for (e, r) in zip(sorted(expected), sorted(result))
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('remove_duplicates.py',
                                       'remove_duplicates.tsv',
                                       eliminate_duplicate_wrapper, comp))
