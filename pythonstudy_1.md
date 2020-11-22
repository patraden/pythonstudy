# pythonstudy :memo:
## Lecture #1 [Link](https://www.youtube.com/watch?v=KdZ4HF1SrFs&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0)
### about programming
* ~~PL Sytax~~
* ~~Libraries~~
* Algorythms & Data structures
* Programming  art/craft (Programmer - writer)
* Programming practice (skills)
* Solution design (architecture)
* Work in groups (ability to collaborate and work with people)
### python 3 синтаксис
```python
print("Hello World!"
x = "Hello World!"
print (x)
print(type(x))
x=1+2+3+4
```
name | value
-- | --
X | "Hello World"

python constantly frees the memory if we want to store something in memory we have to place a link to value in memory
> **=** in Python is a **LINK** . x = 1+2+3+4: python will create temporary objects, then calculates value which will be stored in memory as object. Once onject got calculated x is linked to new object and previous object (x) will be removed

variables values exchange through additional variable
```python
a=2
b=5
tmp=a
a=b
b=tmp
```
variables values exchange through two variable
```python
a=2
b=5
tmp1=b
tmp2=a
a=tmp1
b=tmp2
```
множественное присваивание через кортежи (кортеж переменных и кортеж значений)
```python
a=2
b=5
tmp1,tmp2=b,a #схематично это работает через временный кортеж
a,b=tmp1,tmp2
a,b = b,a #фактический синтаксис обмена через временный кортеж
```
### Арифметические операции
1. x^y==x**y # унарные операции имеют приоритет над бинарными, например 3**0,5, a^b^c==a**b**c в питоне операции выполняются справа на лево
1. -x==-x #унарный минус (тоже самое для унарного плюса)
1. x*y==x*y, x:y==x/y #бинарное деление и умножение 2/3 - float type. x div y=x//y-целочисленное деление x mod y == x%y. Интепретация a/b*c будет последовательно слева направо. **Важно!!** -12//10 =? (-1) -12%10=-2 - это неверно с точки зрения математики, но многие процессоры intel это вычисляют именно так! В питоне это не так! -12//5=-3 -12%3=3 - остаток всегда принадлежит [0,n)
1. x-y==x-y, x+y==x+y имеет наименьший приоритет

### Управляюище операции
в питоне есть только цикл while (for - это "синтаксический сахар")
итерация - однократное выполнение тела цикла

```python
before
while <condition>:
 <operator 1>
 <operator 2>
if <condition>:
  break
 <operator 3>
 continue #go to start of the iteration
else:
 <instructions after all iterations> #чем это отличается от выхода? зачем это нужно? это условие для инструкции break в теле цикла, которое будет игнорировать
after
```
while can be nested
y-=1 - синтаксический сахар y=y+1 *= /= //= %=

```python
if <condition>:
 <operator>
else:
 <operator>
```
```python
for x in 1,5,2,4,3: #rang(start, stop, step) else and break working in for body, else at the end of for also exist. rang(1,10,1)=1,2,3,..,9
 print(x**2)
```
