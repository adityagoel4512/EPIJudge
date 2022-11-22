from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    """
    we need max revenue for us (i.e. min revenue for other player)
    two options: left and right
    max we can make is remaining coins - min opponent can make
    M(L, R) = 0 if L > R
    M(L, R) = max {
        1. coins[L] + min { M(L+2, R), M(L+1, R-1)}
        2. coins[R] + min { M(L+1, R-1), M(L, R-2)}
    }

    if we cache intermediates, since we always progress to i > j, we have O(N) time and O(N) space complexity with dynamic data structure

    """

    def helper(L, R, cache):
        if L > R:
            return 0
        elif (L, R) in cache:
            return cache[(L, R)]
        else:
            cache[(L, R)] = max(coins[L] - max(-helper(L+2,R,cache), -helper(L+1,R-1,cache)), coins[R] - max(-helper(L+1, R-1,cache), -helper(L, R-2,cache)))
            return cache[(L, R)]
    return helper(0, len(coins)-1, {})


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
