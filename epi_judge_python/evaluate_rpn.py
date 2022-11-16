from test_framework import generic_test


def evaluate(expression: str) -> int:
    operands = []
    operator = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x//y}
    for token in expression.split(','):
        if token in operator:
            second_operand = operands.pop()
            first_operand = operands.pop()
            operands.append(operator[token](first_operand, second_operand))
        else:
            operands.append(int(token))
        
    return operands[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
