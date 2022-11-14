from typing import List

from test_framework import generic_test

""" O(n) space, O(n) time
max_profit_after = [0] * len(prices) # max_profit_after[i] is max profit makable with buy at ith day or later
    max_price_after = 0

    #                    [12, 11, 13, 9, 11, 12, 8]
    # max_price_after = 13

    for i in range(len(prices)-1, -1, -1):
        if i != len(prices)-1:
            # max profit after this point (including this point buy is max later or if we buy now then max price after this point)
            max_profit_after[i] = max(max_profit_after[i+1], max_price_after-prices[i])
        max_price_after = max(max_price_after, prices[i])

    min_price_before = float('inf')
    max_profit_so_far = 0
    max_total_profit = 0
    # A =                [12, 11, 13, 9, 11, 12, 8]
    # max_profit_after = [3,  3,  3,  3, 1,  0,  0]
    # max_total_profit  = 5
    # max_profit_so_far = 2
    # min_price_before  = 9
    for i in range(len(prices)):
        # max_profit_so_far doesn't include day i but max_profit_after[i] includes buying at day i
        max_total_profit = max(max_profit_after[i]+max_profit_so_far, max_total_profit)
        # max_profit_so_far includes prices[i] after this (if we sold today)
        max_profit_so_far = max(max_profit_so_far, prices[i]-min_price_before)
        min_price_before = min(min_price_before, prices[i])
        


"""

def buy_and_sell_stock_twice(prices: List[float]) -> float:
    min_price_so_far = float('inf')
    max_profit_after_first_sell = 0
    max_profit_after_second_buy = float('-inf')
    max_profit_after_second_sell = 0.0

    for price in prices:
        max_profit_after_first_sell = max(max_profit_after_first_sell, price-min_price_so_far)
        max_profit_after_second_buy = max(max_profit_after_second_buy, max_profit_after_first_sell-price)
        max_profit_after_second_sell = max(max_profit_after_second_sell, max_profit_after_second_buy+price)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit_after_second_sell


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
