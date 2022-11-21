from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    """
    num_paths[m-1][n-1] = 1
    num_paths[i][j] = num_paths[i+1][j] + num_paths[i][j+1]
    """
    num_paths = [[0 for _ in range(n)] for _ in range(m)]
    num_paths[-1][-1] = 1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            num_paths[i][j] += (num_paths[i+1][j] if i+1 < m else 0) + (num_paths[i][j+1] if j+1 < n else 0)
    return num_paths[0][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
