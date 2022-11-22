from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    """
    num_paths[m-1][n-1] = 1
    num_paths[i][j] = num_paths[i+1][j] + num_paths[i][j+1]

    time: O(mn), space: O(mn)

    space: O(min(m,n)) solution - reuse num_paths
    num_paths[j] becomes num_paths[i+1][j] during iteration
    keep num_paths[i][j+1] in cache variable
    """
    m, n = max(m, n), min(m, n)
    
    # m >= n
    # num_paths[j] = num_paths[i][j]
    num_paths = [0 for _ in range(n)]
    num_paths[n-1] = 1
    for _ in range(m):
        # num_paths[i][n-1]
        for j in range(n-2, -1, -1):
            # num_paths[i][j] = num_paths[i+1][j] + num_paths[i][j+1]
            num_paths[j] += num_paths[j+1]

                
    return num_paths[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
