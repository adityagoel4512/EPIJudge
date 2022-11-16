import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook
import math

def zero_one_random():
    return random.randrange(2) 


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    num_trials = math.ceil(math.log2(upper_bound-lower_bound+1))
    bin_num = 0
    for _ in range(num_trials):
        bin_num = (bin_num << 1) + zero_one_random()
    result = bin_num+lower_bound
    
    # [3,5] => 2
    # XY 11
    
    return result if result <= upper_bound else uniform_random(lower_bound, upper_bound)


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
