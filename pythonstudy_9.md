# pythonstudy :memo:
## Lecture #9 [Link](https://www.youtube.com/watch?v=qf82-r9hl2Y)
### продолжение сортировок слиянием и быстрой
#### сортировка слиянием
##### слияние отсортированных массивов в один

сортировка называется ***устойчивой***, если она не меняет порядок равных элементов
(сортируемая характеристика может быть не единственной у объекта)
один и тот же алгоритм сортировки может быть реализован как устойчиво, так и неустойчиво

```python
def merge(A:list,B:list):
 C=[0]*(len(A)+len(B))
 i=k=n=0
 while i < len(A) and k < len(B):
  if A[i] <= B[k]: # делаем "устойчивую" реализацию алгоритма
   C[n]=A[i]
   i+=1
   n+=1
  else:
   C[n]=B[k]
   k+=1
   n+=1
 while i<len(A): # возможно ничего не "залил", поскольку i > len(A) уже
  C[n]=A[i]
  i+=1
  n+=1
 while k<len(B):
  C[n]=B[k]
  k+=1
  n+=1
 return C
# рекурсивная функция сортировки

def merge_sort(A):
 if len(A)<=1:
  return
 middle=len(A)//2
 L=[A[i] for i in range(middle)]
 R=[A[i] for i in range(middle,len(A))]
 merge_sort(L)
 merge_sort(R)
 C=merge(L,R)
 for i in range(len(A)):
  A[i]=C[i]
```

#### сортировка ТониХоара (QuickSort)
в самом питоне сортировка - прагматичная, которая является гибридом разных сортировок
случайный элемент выбираем первый (т.е. барьерный = 1 элементу массива)

```python
def hoar_sort(A):
 if len(A)<=1:
  return # None
 L=[]
 M=[]
 R=[]
 barrier=A[0]
 for x in A:
  if x<barrier:
   L.append(x)
  elif x==barrier:
   M.append(x)
  else:
   R.append(x)
 hoar_sort(L)
 hoar_sort(R)
 k=0
 for x in L+M+R:
  A[k]=x
  k+=1
```

#### проверка сортировки массива за O(n)

```python
def check_sorted(A,ascending=True):
 """ проверка отсортированности массива за O(n) """
 flag=True
 s=2*int(ascending)-1
 for i in range(len(A)-1):
  if s*A[i]>s*A[i+1]:
   flag=False
   break
 return flag
```

#### бинарный поиск  массиве
сортировка нужна на самом деле для быстрого поиска!
[1,2,2,2,3,4,5,5,5,5,5,7,7,7,7,7]
left_bound
right_bound

```python
#[1,2,2,2,3,4,5,5,5,5,5,7,7,7,7,7]
middle = (left + right)//2
```
