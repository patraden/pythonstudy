"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""

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

def get_fib(position):
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
            A[m],A[p-1]=A[p-1],A[m] #swap m with pivot value
            A[p],A[p-1]=A[p-1],A[p] #swap pivot predecessor with pivot value
            p-=1
        m+=1
    return quicksort(A,s,p-1)+[A[p]]+quicksort(A,p+1,e)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
ltest=len(test)-1

print (quicksort(test,0,ltest))

# Test cases
#print (get_fib(9))
#print (get_fib(11))
#print (get_fib(0))



test_list = [1,3,9,11,15,19,29,30]
test_val1 = 15
test_val2 = 29
test_val3 = 30
#print (binary_search(test_list, test_val1))
#print (binary_search(test_list, test_val2))
#print (binary_search(test_list, test_val3))
