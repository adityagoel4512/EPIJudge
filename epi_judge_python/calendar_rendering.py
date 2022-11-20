import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    return find_max_simultaneous_events_together(A)

def find_max_simultaneous_events_separate(A: List[Event]) -> int:
    # sort by start time
    # current span start time is max of start times, end times min
    # [(timestamp, start?)]
    timestamps = []
    for start, finish in A:
        timestamps.append((start, False))
        timestamps.append((finish, True))

    timestamps.sort()
    max_simultaneous = 0
    cur_simultaneous = 0
    for _, finish in timestamps:
        if finish:
            cur_simultaneous -= 1
        else:
            cur_simultaneous += 1
            max_simultaneous = max(max_simultaneous, cur_simultaneous)
    return max_simultaneous



def find_max_simultaneous_events_together(A: List[Event]) -> int:
    start_idx = 0
    max_simultaneous = 0
    A.sort(key=lambda e: e.start)
    print(A)
    # sort on start time, so A[k].finish <= A[k+1].finish
    # at each event A[i], compute max number of events together up to ending at the ith

    """
    [
        Event(start=1, finish=5), 
        Event(start=2, finish=7), 
        Event(start=4, finish=5), 
        Event(start=6, finish=10), 
        Event(start=8, finish=9), 
        Event(start=9, finish=17), 
        Event(start=11, finish=13), 
        Event(start=12, finish=15), 
        Event(start=14, finish=15),
    ]
    start_idx = 3
    max_simultaneous = 3
    i = 5
    """
    for i in range(len(A)):
        while A[start_idx].finish < A[i].start:
            start_idx += 1

        # ensures A[start_idx].finish >= A[i].start
        # add one more to sequence
        max_simultaneous = max(max_simultaneous, i-start_idx+1)
    return max_simultaneous

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
