from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    result = []
    """
    path = "/usr/lib/../bin/gcc"
    tokens = ["", "usr", "lib", "..", "bin", "gcc"]
    absolute = 1
    result = ["", "usr", "bin", "gcc"]
    ret = "/usr/bin/gcc"
    """
    tokens = path.split('/')
    absolute = 1 if path[0] == '/' else 0
    if absolute:
        result.append('')
    for tok_idx in range(absolute, len(tokens)):
        token = tokens[tok_idx]
        # do nothing with current directory
        if token == '.' or token == '':
            continue
        elif token == '..':
            # if already at home directory, do nothing, otherwise go to parent dir
            if absolute:
                if len(result) > 1 or result[0] != '':
                    # reached home dir, do nothing
                    result.pop()
            else:
                if not result or result[-1] == '..':
                    result.append('..')
                else:
                    result.pop()

        else:
            # token is dir name
            result.append(token)
    if len(result) == 1 and result[0] == "":
        return '/'
    return '/'.join(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
