## Lecture #5 [Link](https://www.youtube.com/watch?v=3I6OjxoeSS8)
### arrays (list)

```python
a = [1, 2, 3, 4, 5]
for x in a:
 print(x, type(x))
 x += 1 # x=z+1 ситаем результат 1 - временный объект, порождают объект 2 и x связывается с этим объектом. По итогу x ссылается на 2.
 print(x)
print(a) # [1, 2, 3, 4, 5]
```

в питоне есть изменяемые объекты и неизменяемые
есть имена и есть объекты

```python
# возведем каждый элемент в квадрат и покажем, как менять объекты массива
A=[1,2,3,4,5]
for k in range(5):
 A[k]=A[k]**2
```

```python
A=[0]*1000 # создаем массив из 1000 нулей
top = 0
x = int (input())
while x!=0:
 A[top]=x
 top+=1
 x = int (input())
for k in range(4,-1,-1):
 print(A[k])
```

```python
# array copy
n = int(input()) # array size
a = [0]*n
b = [0]*n
for k in range(n):
    a[k] = int(input())
for k in range(n):
    b[k] = a[k]
c = a
a[0] = 777
print(c[0]) # 777
c = list(a) # copying A
```

```python
def array_search(a: list, n: int, x: int) -> int:
    """ Осуществляет поиск числа х в массиве А
    от 0 до N-1 индекса ключительно.
    Возвращает индекс элемента ъ в массике А
    Или -1, если такого нет.
    Если в массиве несколько одинаковых элементов,
    равных х, то венуть индекс первого по счету.
    """
    for k in range(n):
        if a[k] == x:
            return k
    return -1


def test_array_search():
    a1 = [1, 2, 3, 4, 5]
    m = array_search(a1, 5, 8)
    if m == -1:
        print("test#1 - ok")
    else:
        print("test#1 - fail")

    a2 = [-1, -2, -3, -4, -5]
    m = array_search(a2, 5, -3)
    if m == 2:
        print("test#2 - ok")
    else:
        print("test#2 - fail")

    a3 = [10, 20, 30, 10, 10]
    m = array_search(a3, 5, 10)
    if m == 0:
        print("test#3 - ok")
    else:
        print("test#3 - fail")


if __name__ == "__main__":
    test_array_search()
```

```python
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
```
#### cyclic shift

```python
# shift left
a = ...
n = len(a)
tmp = a[0]
for k in range(n-1):
    a[k] = a[k+1]
a[n-1] = tmp

# shift right
tmp = a[n-1]
for k in range(n-2,-1,-1):
    a[k+1] = a[k]
a[0] = tmp
```

#### решето эратосфена

```python
def sieve(n):
    """ Eratosthenes sieve for n."""
    pass
    a = [True] * n
    a[0] = a[1] = False
    for k in range(2, n):
        if a[k]:
            for m in range(2 * k, n, k):
                a[m] = False
    for k in range(n):
        print(k, "-", "simple" if a[k] else "complex")


if __name__ == "__main__":
    sieve(100)
```
синтаксис тернарного оператора
``` <expression on true> if <predicate> else <expression on false>```
