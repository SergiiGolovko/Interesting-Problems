def smallest_missing_integer(l):
    '''Find smallest positive integer missing in the array.

    Parameters:
    -----------
    l: iterable over integers.

    Returns:
    --------
    res: integer, smallest positive integer missing in the array l.
    '''

    # First loop, filling smartly array,
    n = len(l)
    for a in l:
        while (a <= n) and (a > 0) and (a != l[a - 1]):
            l[a - 1], a = a, l[a - 1]  # swap a and l[a-1]

    # Second loop, finding the smallest positive integer missing.
    for (i, a) in enumerate(l):
        if i + 1 != a:
            return i + 1

    # If l = [1, 2, 3, 4, ..., n]
    return n + 1
