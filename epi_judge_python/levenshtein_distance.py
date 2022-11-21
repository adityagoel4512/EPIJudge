from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    """
    levenshtein distance for A[:i], B[:j]
    if A[i] == B[j]:
        distance[i][j] = distance[i-1][j-1]
    else:
        distance[i][j] = 1+min(distance[i-1][j-1], distance[i-1][j], distance[i][j-1])
        -- make A[:i] == B[:j] then transform A[i] to B[j]
        -- make A[:i] to B[:j-1] then add B[j] to A[i]
        -- make A[:i-1] to B[:j] then delete A[i]

    distance[0][j] = j
    distance[i][0] = i

    time: O(AB), space: O(AB)

    O(min(A,B)) space solution
    if A is larger, B smaller
    -- when traversing distance[i][j] becomes distance[i-1][j] in updates:
    cache exists (for distance[i-1][j-1])
    => if A[i] == B[j]: cache = distance[j]; distance[j] = distance[j-1]
    => else: cache = distance[j]; distance[j] = 1+min(distance[j], cache, distance[j-1])

    """
    if len(A) < len(B):
        return levenshtein_distance(B, A)
    # len(A) >= len(B)
    distance = [0] * (len(B)+1)
    for j in range(len(distance)):
        distance[j] = j
    # distance[j] = distance[0][j]
    for i in range(1,len(A)+1):
        # cache = distance[i-1][j-1] -> distance[i-1][0]
        distance[0] = i-1
        cache = distance[0]
        for j in range(1, len(B)+1):
            next_cache = distance[j]
            if A[i-1] == B[j-1]:
                distance[j] = cache
                # distance[i][j] = distance[i-1][j-1]
            else:
                distance[j] = 1+min(cache, distance[j], distance[j-1])
            cache = next_cache

    return distance[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
