"""
Tests for doctest module.

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

def binary_search(input_array:list, value:int):
    """
    Binary search in sorted array
    """
    high=len(input_array)
    low=0
    while low<high:
        mid=(high+low)//2
        if input_array[mid]==value:
            return mid
        elif input_array[mid]<value:
            low=mid+1
        else:
            high=mid-1
    return -1

def get_fib(position:int):
    """
    Just simple reccursive example.
    """
    if position < 0:
        return -1
    elif position == 0 or position == 1:
        return position
    else:
        return get_fib(position-1)+get_fib(position-2)

def quicksort(A:list, s:int,e:int):
    """
    Quicksort where pivot value is the last element in a list.
    Takes array with start and end indexes as arguments to minimize memory consumption.
    """
    if s==e:
        return [A[s]]
    elif s>e:
        return []
    p=e
    m=s
    while m<p:
        while A[m]>A[p]:
            A[m],A[p-1]=A[p-1],A[m] #swap m with pivot
            A[p],A[p-1]=A[p-1],A[p] #swap pivot and its predecessor
            p-=1
        m+=1
    return quicksort(A,s,p-1)+[A[p]]+quicksort(A,p+1,e)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
