def merge(a: list, b: list):
    """ Merges two sorted arrays into one."""
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:  # assume arrays sort is ascendant and stable (equal number ordering respected)
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):  # append remaining elements from one of two arrays
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


def merge_sort(a: list):
    """ Recursive ascendant merge sort. """
    if len(a) <= 1:
        return
    middle = len(a) // 2
    left = [a[_] for _ in range(middle)]
    right = [a[_] for _ in range(middle, len(a))]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for i in range(len(a)):
        a[i] = c[i]


if __name__ == "__main__":
    test1 = [3, 4, 5, 1, 2, 3, 4, 10, 14, 1, 16]
    merge_sort(test1)
    print(test1)
    test2 = [3]
    merge_sort(test2)
    print(test2)
