def quick_sort(a: list):
    """ Tony Hoare quick sort. """
    if len(a) <= 1:
        return  # None
    left = []
    middle = []
    right = []
    # do not do: left = right = middle = []
    barrier = a[0]  # we can always change it to a random or some better logic
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    quick_sort(left)
    quick_sort(right)
    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1


def check_sorted(a, ascending=True):
    """ Checks if array is sorted in O(n). """
    s = 2 * int(ascending) - 1
    for i in range(len(a)-1):
        if s * a[i] > s * a[i+1]:
            return False
    return True


if __name__ == "__main__":
    test1 = [3, 4, 5, 1, 2, 3, 4]
    quick_sort(test1)
    print(check_sorted(test1))
