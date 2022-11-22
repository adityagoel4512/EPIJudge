from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    """
    N[t] = sum(N[t-k] for k in range(1, maximum_step+1) if t-k >= 0)
    N[0] = 1
    """

    num_ways = [0]*(top+1)
    num_ways[0] = 1

    for step in range(1, top+1):
        num_ways[step] = sum(num_ways[step-k] for k in range(1, maximum_step+1) if step-k >= 0)

    return num_ways[top]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
