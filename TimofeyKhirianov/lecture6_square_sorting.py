def insert_sort(a):
    """insert sort"""
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


def choice_sort(a):
    """choice sort"""
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def bubble_sort(a):
    """bubble sort"""
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]


def test_sort(sort_algorithm):
    print("testing:", sort_algorithm.__doc__)
    print("testcase #1:", end="")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print("ok" if a == a_sorted else "fail")
    print("testcase #2:", end="")
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(0, 20))
    sort_algorithm(a)
    print("ok" if a == a_sorted else "fail")
    print("testcase #3:", end="")
    a = [4, 2, 4, 2, 1]
    a_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(a)
    print("ok" if a == a_sorted else "fail")


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
