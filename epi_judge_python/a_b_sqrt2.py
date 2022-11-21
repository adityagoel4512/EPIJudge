from typing import List
from collections import deque
from test_framework import generic_test
import heapq
import math
def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    sqrt2 = math.sqrt(2)
    def compute(a, b):
        return a + b*sqrt2

    results = []
    candidates = [(compute(0, 0), 0, 0)]
    values = set()
    for _ in range(k):
        val, a, b = heapq.heappop(candidates)
        results.append(val)
        cand0 = compute(a+1, b)
        if cand0 not in values:
            heapq.heappush(candidates, (cand0, a+1, b))
            values.add(cand0)
        cand1 = compute(a, b+1)
        if cand1 not in values:
            heapq.heappush(candidates, (cand1, a, b+1))
            values.add(cand1)

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
