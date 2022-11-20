import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people: List[Person]) -> None:
    age_count = collections.defaultdict(int)
    for person in people:
        age_count[person.age] += 1
    indices = {}

    cumulative_indices = 0
    for age, count in age_count.items():
        indices[age] = {'cur': cumulative_indices, 'end': cumulative_indices+count}
        cumulative_indices += count

    for age, age_indices in indices.items():
        print(age, age_indices)
        
        # swap until loop or we have managed to get person with appropriate index
        while age_indices['cur'] < age_indices['end']:
            cur = age_indices['cur']
            person = people[cur]
            if person.age != age:
                # swap into next available index
                print('swap', list(indices), person.age)
                print('val', indices[person.age])
                dest_index = indices[person.age]['cur']
                person[dest_index], person[cur] = person[cur], person[dest_index]
            else:
                print('here', age_indices['cur'])
                age_indices['cur'] += 1

        # people[indices['cur']] == indices['end'] (done with this section) or 
    return


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('group_equal_entries.py',
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
