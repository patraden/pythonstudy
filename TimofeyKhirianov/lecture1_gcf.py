def gcd(a, b):
    """ Euklid gcd with Bezu coefficients
    >>> gcd(18,6)[0]
    6
    >>> gcd(9515,121)[0]
    11
    >>> gcd(2,3)[0]
    1
    >>> gcd(-14,21)[0]
    -7
    """
    flag = True
    if a < b:
        a, b = b, a
        flag = False
    up, un = 1, 0
    vp, vn = 0, 1
    q = a // b
    r = a - b * q
    while r != 0:
        a, b = b, r
        un, up = up - un * q, un
        vn, vp = vp - vn * q, vn
        q = a // b
        r = a - b * q
    return b, (un, vn) if flag else (vn, un)


def gcd_array(a, b):
    """НОД и НОК для массива целых чисел
    >>> gcd(18,6)[0]
    6
    >>> gcd(9515,121)[0]
    11
    >>> gcd(2,3)[0]
    1
    >>> gcd(-14,21)[0]
    -7
    """
    flag = True
    if a < b:
        a, b = b, a
        flag = False
    up, un = 1, 0
    vp, vn = 0, 1
    q = a // b
    r = a - b * q
    while r != 0:
        a, b = b, r
        un, up = up - un * q, un
        vn, vp = vp - vn * q, vn
        q = a // b
        r = a - b * q
    return b, (un, vn) if flag else (vn, un)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
