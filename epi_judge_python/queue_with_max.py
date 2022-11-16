from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque


class QueueWithMax:
    def __init__(self) -> None:
        self._data = deque()
        self._max_deque = deque()

    def enqueue(self, x: int) -> None:
        self._data.append(x)
        while self._max_deque and self._max_deque[-1] < x:
            self._max_deque.pop()

        # x <= all elems in max deque
        self._max_deque.append(x)
        return

    def dequeue(self) -> int:
        ret = self._data.popleft()
        if ret == self._max_deque[0]:
            self._max_deque.popleft()
        return ret

    def max(self) -> int:
        return self._max_deque[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
