# pythonstudy :memo:
## Lecture #6 [Link](https://www.youtube.com/watch?v=NLq7nB9bV0M)
### массивы динамические
```python
A=[]
x=int(input())
A.append(x)
n=len(A)
x=A.pop()
n=len(A)
```
### list comprehension
A=[x**2 for i in range(10)] # заводим массив квадратов натуральных чисел от 0 до 10

A=[1,2,3,4,5]
for x in A:
создаем массив из А где все элементы будут квадратами и взять только четные элементы

B=[]
for x in A:
 if x%2==0:
  B.append(x*x)

B=[x*x for x in A if x%2==0] # тоже самое что выше
B=[0 if x<0 else x*x for x in A if x%2==0] # тоже самое что выше с тернанрным if

#### сортировки
##### квадратичные сортировки (кол-во операций O(n*n))
###### insert sort
```python
def insert_sort(A):
    """сортировка списка А вставками"""
    N=len(A)
    for top in range(1,N):
        k=top
        while k>0 and A[k-1]>A[k]: #оператор and ленивый и поэтому, если k=0, то вторую часть питон вычислять не будет и не произойдет выхода за границы массива
            A[k],A[k-1]=A[k-1],A[k]
            k-=1
```
###### choice sort
```python
def choice_sort(A):
    """сортировка списка А выбором"""
    N=len(A)
    for pos in range(0,N-1):
        for k in range(pos+1,N):
            if A[k]<A[pos]:
                A[k],A[pos]=A[pos],A[k]
```
###### bubble sort
```python
def bubble_sort(A):
    """сортировка списка А методом пузырька"""
    N=len(A)
    for bypass in range(1,N):
        for k in range(0,N-bypass):
            if A[k]>A[k+1]:
                A[k],A[k+1]=A[k+1],A[k]
```
###### сортировка подсчетом O(n) по операи=циям и O(m) по памяти, где m - количество различных элементов
применяет алгоритм частотного анализа вхождения в массив конечного числа элементов, например 0-9.
```python
A=1,2,3,4,5,6,7,4,3,2,3,4,5,6,7,8,9,7,6,4,3,3,8,9,5,4]
N=..;
F=[0]*10
for i in range(N):
 x=int(input(i))
 F[x]+=1
```
