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
    for i in range(n):
        a = l[i]
        while (a <= n) and (a != l[a - 1]) and (a > 0):
            l[a - 1], a = a, l[a - 1]  # swap a and l[a-1]

    # Second loop, finding the smallest positive integer missing.
    for i in range(n):
        if (i + 1) != l[i]:
            return i + 1

    # If l = [1, 2, 3, 4, ..., n]
    return n + 1
