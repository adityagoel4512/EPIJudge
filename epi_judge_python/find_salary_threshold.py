from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    """
    [20,30,40,90,100], sum = 280
    need 70
    cumulative_salaries = 100
    num_salaries = 1

    """
    savings_needed = sum(current_salaries)-target_payroll
    if savings_needed < 0:
        return -1

    sorted_payroll = sorted(current_salaries, reverse=True)
    cumulative_salaries = 0
    for i, pay in enumerate(sorted_payroll):
        cumulative_salaries += pay
        num_salaries = i+1
        candidate_cap = (cumulative_salaries-savings_needed)/num_salaries

        if i == len(sorted_payroll)-1 or candidate_cap >= sorted_payroll[i+1]:
            return candidate_cap

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
