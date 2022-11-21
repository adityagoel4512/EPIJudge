from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    number_char_map = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    """
    Time complexity [n = len(phone_number)]:
    Base case cost: O(n)
    Base case number: 4^n 
    Recursive case cost: O(1)
    Recursive case number = 1 + 4 + 4^2 + ... + 4^n = 1.(1-4^{n})/(1-4) = 1/3 * (4^{n}-1)
    Result: O(n*4^n)
    """
    # tuple = (phone_number_index at, char_children_processed)
    stack = [(0,0)]
    result = []
    prefix = []
    while stack:
        phone_number_index, char_children_processed = stack.pop()
        if phone_number_index == len(phone_number):
            # finished, add to res
            result.append(''.join(prefix))
        else:
            # not finished
            digit = int(phone_number[phone_number_index])
            num_children_to_process = len(number_char_map[digit])
            if num_children_to_process == char_children_processed:
                # processed all children, pop off stack and prefix
                prefix.pop()
            else:
                if char_children_processed == 0:
                    # first time at this node, add to prefix
                    prefix.append(number_char_map[digit][char_children_processed])
                else:
                    prefix.pop()
                    prefix.append(number_char_map[digit][char_children_processed])
                # reinsert parent to be reprocessed
                stack.append((phone_number_index, char_children_processed+1))
                # more children remain to be processed
                stack.append((phone_number_index+1,0))


    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
