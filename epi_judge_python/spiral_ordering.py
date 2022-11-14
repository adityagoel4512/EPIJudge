from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []
    def spiral_with_offset(offset: int) -> None:
        # top to right
        for col in range(offset, len(square_matrix)-offset):
            result.append(square_matrix[offset][col])

        
        # top right to bottom right
        for row in range(offset+1, len(square_matrix)-offset-1):
            result.append(square_matrix[row][len(square_matrix)-offset-1])


        # bottom right to bottom left
        for col in range(len(square_matrix)-offset-1, offset, -1):
            result.append(square_matrix[len(square_matrix)-offset-1][col])


        # bottom left to top left
        for row in range(len(square_matrix)-offset-1, offset, -1):
            result.append(square_matrix[row][offset])

        
    
    offsets = 1+len(square_matrix)//2 if len(square_matrix) & 1 else len(square_matrix)//2
    for offset in range(offsets):
        spiral_with_offset(offset)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
