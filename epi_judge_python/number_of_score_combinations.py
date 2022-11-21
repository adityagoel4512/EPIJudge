from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    """
    scoring 12 => either:
        1. scoring 10 + 2 point play
        2. scoring 9 + 3 point play
        3. socring 5 + 7 point play

    num_combinations[s] = sum(num_combinations[s-k] for k in individual_play_scores if s-k >= 0) -- order dependent
    => to force ordering, process plays in sequential order
    k = individual_play_scores[i]
    num_combinations[s,i]  is number of combinations up to final score s using plays up to and including ith play type
    num_combinations[s,i] = num_combinations[s,i-1] (don't use this play type) + num_combinations[s-k,i] (use this play type)

    process order: play score ascending -> along char
    """

    num_combinations = [0] * (final_score+1)
    num_combinations[0] = 1
    for play in individual_play_scores:
        for score in range(1, final_score+1):
            if score-play >= 0:
                num_combinations[score] += num_combinations[score-play]

    return num_combinations[final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
