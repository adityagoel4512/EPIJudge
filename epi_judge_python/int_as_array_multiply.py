from typing import List
from collections import deque
from test_framework import generic_test

# 1,3,7
#   2,3
# result = [0,0,0,5,5,1]
# offset, n1 = 1,2
# idx, n2 = 1,3
# res_idx = -1-1-1 = -3
# O(mn) time

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if num1[0] < 0 and num2[0] > 0 or num1[0] > 0 and num2[0] < 0 else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    result = deque([0 for _ in range(len(num1) + len(num2))])
    for i, d1 in enumerate(reversed(num1)):
        for j, d2 in enumerate(reversed(num2)):
            result_idx = -1-i-j
            result[result_idx] += d1 * d2
            result[result_idx-1] += result[result_idx] // 10
            result[result_idx] = result[result_idx] % 10

    while result and result[0] == 0:
        result.popleft()
    if not result:
        result.append(0)
    result[0] *= sign
    return list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
