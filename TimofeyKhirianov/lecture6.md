## Lecture #6 [Link](https://www.youtube.com/watch?v=NLq7nB9bV0M)
### list is an object which mimics dynamic arrays
```python
a = []
x = int(input())
a.append(x)
n = len(a)
x = a.pop()
```
### list comprehension
```python
a = [_**2 for _ in range(10)] # declare an array of size 10
for x in [1,2,3,4,5]:
    pass

b=[]
for x in a:
 if x % 2 == 0:
  b.append(x*x)

b = [x * x for x in a if x % 2 == 0] # sames as above but works much faster due to list comprehension build-in optimizations
b1 = [0 if x < 0 else x * x for x in a if x % 2 == 0] # with ternary operator
```
### sorting
#### square sorting - O(n*n)
```python
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
```
#### ordering sort O(n) for operations and O(m) for memory, where m - number of unique values in an array, for example 0-9.
```python
a = [1,2,3,4,5,6,7,4,3,2,3,4,5,6,7,8,9,7,6,4,3,3,8,9,5,4]
n = 10
f = [0] * 10
for i in range(n):
 x = int(input(i))
 f[x]+=1
```
