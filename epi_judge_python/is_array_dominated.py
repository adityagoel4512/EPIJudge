import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height: List[int]) -> None:
        self._players = [Team.Player(h) for h in height]

    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0: 'Team', team1: 'Team') -> bool:
        team0 = sorted(team0._players, reverse=True)
        team1 = sorted(team1._players, reverse=True)

        """
        team0 = [5,4,1]
        team1 = [3,2,0]
        """
        for player0, player1 in zip(team0, team1):
            if player0.height >= player1.height:
                return False

        return True


@enable_executor_hook
def valid_placement_exists_wrapper(executor, team0, team1, expected_01,
                                   expected_10):
    t0, t1 = Team(team0), Team(team1)

    result_01 = executor.run(
        functools.partial(Team.valid_placement_exists, t0, t1))
    result_10 = executor.run(
        functools.partial(Team.valid_placement_exists, t1, t0))
    if result_01 != expected_01 or result_10 != expected_10:
        raise TestFailure('')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_array_dominated.py',
                                       'is_array_dominated.tsv',
                                       valid_placement_exists_wrapper))
