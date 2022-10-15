# pythonstudy :memo:
## Lecture #7 [Link](https://www.youtube.com/watch?v=0Bc8zLURY-c)
### рекурсия

***очень важно*** очередная подзадача должна быть проще в том смысле, что она ближе к крайнему случаю
когда мы придумываем рекурсия, мы должны иметь:
* рекурретный случай
* крайний случаай (конечнй)
рекуррсия не всегда нужна. например, если характер задачи циклический

```python
def matryoshka(n):
    """"""
    if n==1:
        print("Матрешечка")
    else:
        print("Верх матрешки n=", n)
        matryoshka(n-1)
        print("Низ матрешки n=", n)
    pass
```

#### фрактальные структуры

выбираем произвольную глубину рекурсии

A1x=(1-alfa)*Ax+alfa*Bx
B1x=
C1x=
D1x=

```python
import graphics as gr

window = gr.GraphWin("lecture 7", 300, 300)
alpha=0.2

def fractal_rectangle(A,B,C,D, depth=10): #координаты x,y в виде кортежей
    if depth < 1:
        return
    for M,N in (A,B), (B,C), (C,D), (D,A):
        gr.Line(gr.Point(*M),gr.Point(*N).draw(window))
    A1=(A[0]*(1-alpha) + B[0]*alpha,A[1]*(1-alpha) + B[1]*alpha)
    B1=(B[0]*(1-alpha) + C[0]*alpha,B[1]*(1-alpha) + C[1]*alpha)
    C1=(C[0]*(1-alpha) + D[0]*alpha,C[1]*(1-alpha) + D[1]*alpha)
    D1=(D[0]*(1-alpha) + A[0]*alpha,D[1]*(1-alpha) + A[1]*alpha)
    fractal_rectangle(A1,B1,C1,D1, depth-1)

fractal_rectangle((100,100),(100,500),(500,500),(100,500))
```
#### фракториал (лучше сделать в цикле, конечно же)

f(n)=(1 if n<=1) or (f(n-1)*n>1

```python
def f(ni:int):
 assert n>=0, "Факториал отрицательного неопределен" # assert - оператор проверки, который вызывает ошибку
 if n==0:
  return 1
 return n*f(n-1)
```

#### алгоритм Евклида - поиск НОД(GCD)

НОД(А,В) = НОД(А-В,В)
если D - НОД, то D делит a-b 
gcd(a,b)=(a, a=b) or (gcd(a-b,b), a>b) or (gcd(a, b-a), b>=a)

```python
def gcd(a:int,b:int):
 if a==b:
  return a
 elif a>b:
  return gcd(a-b,b)
 else: # a<=b
  return gcd(a,b-a) 
```
НОД(А,В) = НОД(В,В%A) #оптимизация алгоритма на случай, если А намного больше В
gcd(a,b)=(a, b=a) or (gcd(b,a%b), a<>b)

```python
def gcd(a,b):
 if b==a:
  return a
 else:
  return gcd(b,a%b)
```

```python
def gcd(a,b):
 return a if b==a else gcd(b,a%b)
```

#### бастрое возведение в степень

a^n=a*...*a (n times)
a^n=a^n-1*a # рекурретное рассуждения для положительных n
pow(a,n)= (1 if n=0) or (pow(a,n-1)*a if n>0)

```python
def pow(a:float,n:int):
 if n==0:
  return 1
 else:
  return pow(a, n-1)*a
```

assume n=2k => (a^2)^k
```python
def pow(a:float,n:int):
 if n==0:
  return 1
 elif n%2==1:
  return pow(a, n-1)*a
 else: #n%2==0
 return pow(a*a,n//2)
```

#### ханойские башни

3 пирамиды с блинчиками, с правилом, что больший диск, не должен лежать на диске меньшего диаметра

```python
def pyramid_game(pyramid,size:int,source_i:int=1,target_i:int=3):
    """рекурсивный алгоритм игры ханойские башни (классические 3 оси)"""
    pyramid_size=len(pyramid[source_i-1])
    assert type(pyramid) is list and pyramid_size>0 and size>0
    if size==1:
         top_element=pyramid[source_i-1].pop()
         pyramid[target_i-1].append(top_element)
    else:
         tmp_i=6-source_i-target_i
         pyramid_game(pyramid,size-1,source_i,tmp_i)
         base_element=pyramid[source_i-1].pop()
         pyramid[target_i-1].append(base_element)
         pyramid_game(pyramid,size-1,tmp_i,target_i)

def pyramid_game_tests():

    print("test#1", end="")
    p=[[1],[],[]]
    pyramid_game(pyramid=p,size=len(p[0]))
    print("ok" if p==[[],[],[1]] else "fail")

    print("test#2", end="")
    p=[[1],[],[]]
    pyramid_game(pyramid=p,size=len(p[0]),source_i=1,target_i=2)
    print("ok" if p==[[],[1],[]] else "fail")

    print("test#3", end="")
    p=[[2,1],[],[]]
    pyramid_game(pyramid=p,size=len(p[0]))
    print("ok" if p==[[],[],[2,1]] else "fail")

    print("test#4", end="")
    p=[[],[10,9,8,7,6,5,4,3,2,1],[]]
    pyramid_game(pyramid=p,size=10,source_i=2,target_i=1)
    print("ok" if p==[[10,9,8,7,6,5,4,3,2,1],[],[]] else "fail")

if __name__ == "__main__":
    pyramid_game_tests()
```


