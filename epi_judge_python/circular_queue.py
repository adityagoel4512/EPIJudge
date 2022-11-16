from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self._size = 0
        self._data = [None] * capacity
        self._front = 0 # index to dequeue from (first inserted element)
        self._back = 0 # index to enqueue at (first after used idxes)
        return

    def enqueue(self, x: int) -> None:
        if self.size() == len(self._data):
            new_arr = [None] * (len(self._data) * 2)
            idx = 0
            for i in range(self._front, len(self._data)):
                new_arr[idx] = self._data[i]
                idx += 1
            for i in range(0, self._front):
                new_arr[idx] = self._data[i]
                idx += 1
            
            self._front = 0
            self._back = len(self._data)

            # dynamic reallocation
            self._data = new_arr
        
        self._data[self._back] = x
        self._back = (self._back + 1) % len(self._data)
        self._size += 1
        return

    def dequeue(self) -> int:
        data = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return data

    def size(self) -> int:
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
