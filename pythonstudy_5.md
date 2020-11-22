# pythonstudy :memo:
## Lecture #5 [Link](https://www.youtube.com/watch?v=3I6OjxoeSS8)
### массивы (list)

```python
A=[1,2,3,4,5]
for x in A:
 print(x, type(x))
 x+=1 # x=z+1 ситаем результат 1 - временный объект, порождают объект 2 и x связывается с этим объектом. По итогу x ссылается на 2.
 print(x)
print(A) #[1,2,3,4,5]
```

в питоне есть изменяемые объекты и неизменяемые
есть имена и есть объекты

```python
# возведем каждый элемент в квадрат и покажем, как менять объекты массива
A=[1,2,3,4,5]
for k in in range(5):
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
# копирование массива
N=int(input()) # array size
A=[0]*N
B=[0]*N
for k in rang(N):
 A[k]=int(input())
for k in range(N):
 B[k]=A{k}
C=A
A[0]=777
print(C[0]) # 777
C=list(A) # copying A
```

```python
def array_search(A:list,N:int,x:int):
    """ Осуществляет поиск числа х в массиве А
    от 0 до N-1 индекса ключительно.
    Возвращает индекс элемента ъ в массике А
    Или -1, если такого нет.
    Если в массиве несколько одинаковых элементов,
    равных х, то венуть индекс первого по счету.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def test_array_search():
    A1 = [1,2,3,4,5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("test#1 - ok")
    else:
        print("test#1 - fail")

    A2 = [-1,-2,-3,-4,-5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("test#2 - ok")
    else:
        print("test#2 - fail")

    A3 = [10,20,30,10,10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("test#3 - ok")
    else:
        print("test#3 - fail")
test_array_search()
```

```python
def invert_array(A,N):
    """ Обращение массива (поворот задом-наперед)
        в рамках индексов от 0 до N-1
    """
    for k in range (N//2):
        A[k],A[N-1-k]=A[N-1-k],A[k]
    return A

def test_invert_array():
    A1 = [1,2,3,4,5]
    print(A1)
    invert_array(A1,5)
    print(A1)
    if A1 == [5,4,3,2,1]:
        print("test#1 - ok")
    else:
        print("test#1 - fail")

    A2 = [0,0,0,0,0,0,0,10]
    print(A2)
    invert_array(A2,8)
    print(A2)
    if A2 == [10,0,0,0,0,0,0,0]:
        print("test#1 - ok")
    else:
        print("test#1 - fail")

test_invert_array()
```
#### Циклический сдвиг

```python
# сдвиг влево
for k in range(N-1):
 A[k]=A[k+1]
A[N-1]=tmp
tmp=A[0]

# свдиг вправо
tmp=A[N-1]
for k in range(N-2,-1,-1):
 A[k+1]=A[k]
A[0]=tmp
```

#### решето эратосфена

```python
def sieve(N):
    """ Решето Эратосфена для числа N
    """
    pass
    A=[True]*N # все числа до N простые
    A[0]=A[1]=False
    for k in range (2,N):
        if A[k]:
            for m in range(2*k,N,k):
                A[m]=False
    for k in range(N):
        print(k,"-","простое" if A[k] else "составное") # тернарный оператор в принте с if
sieve(10)
```
синтаксис тернарного оператора
``` <expression on true> if <predicate> else <expression on false>```

