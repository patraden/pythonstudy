def invert_array(a, n):
    """ Inverts an array. """
    for k in range(n // 2):
        a[k], a[n - 1 - k] = a[n - 1 - k], a[k]
    return a


def test_invert_array():
    a1 = [1, 2, 3, 4, 5]
    print(a1)
    invert_array(a1, 5)
    print(a1)
    if a1 == [5, 4, 3, 2, 1]:
        print("test#1 - ok")
    else:
        print("test#1 - fail")

    a2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(a2)
    invert_array(a2, 8)
    print(a2)
    if a2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("test#1 - ok")
    else:
        print("test#1 - fail")


if __name__ == "__main__":
    test_invert_array()
