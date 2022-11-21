from test_framework import generic_test


def fibonacci(n: int) -> int:
    fib0 = 0
    if n == 0:
        return fib0
    fib1 = 1
    for _ in range(n-1):
        fib0, fib1 = fib1, fib0+fib1
    return fib1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
