"""
Test cases for module.
>>> test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
>>> print (quicksort(test,0,len(test)-1))
[1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
>>> print (get_fib(9))
34
>>> print (get_fib(11))
89
>>> print (get_fib(0))
0
>>> test_list = [1,3,9,11,15,19,29,30]
>>> test_val1 = 15
>>> test_val2 = 29
>>> test_val3 = 30
>>> print (binary_search(test_list, test_val1))
4
>>> print (binary_search(test_list, test_val2))
6
>>> print (binary_search(test_list, test_val3))
7
"""


def binary_search(input_array: list, value: int):
    """
    Binary search in a sorted array.
    """
    high = len(input_array)
    low = 0
    while low < high:
        mid = (high + low) // 2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def get_fib(n: int):
    """
    Returns Nth Fibonacci number.
    Simple reccursive example.
    """
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return get_fib(n - 1) + get_fib(n - 2)


def quicksort(a: list, s: int, e: int):
    """
    Quicksort where pivot value is the last element in a list.
    Takes array with start and end indexes as arguments to minimize memory consumption.
    """
    if s == e:
        return [a[s]]
    elif s > e:
        return []
    p = e
    m = s
    while m < p:
        while a[m] > a[p]:
            a[m], a[p - 1] = a[p - 1], a[m]  # swap m with pivot
            a[p], a[p - 1] = a[p - 1], a[p]  # swap pivot and its predecessor
            p -= 1
        m += 1
    return quicksort(a, s, p - 1) + [a[p]] + quicksort(a, p + 1, e)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)
