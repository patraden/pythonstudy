## Lecture #2 [Link](https://www.youtube.com/watch?v=ZgSx3yH7sJI&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=2)
### logics algebra
```python
A = 2+2==4 # True
B = 1+1==1 # False 
# Важно однако в каком языке мы делаем высказывание, 
# пример "бог есть" - для верующего это верно, для атеиста - ложь.
# бертран рассел пыталя сделать единственно истинную систему
# существуют атомарные высказывание и составные высказывание.
```

Basic atomic operations:
1. Не А # инверсия
2. А и В # конъюнкция
3. А или В # дизъюнкция
4. А => В # импликация x=2 => x^2=4
5. A <=> B # эквиваленция
6. тавтология - тождественный единица
7. противоречеие - тождественный ноль

пусть истина=1, ложь=0, то что произойдет дальше?
рассмотрим функцию от логической переменной f(x)

####  truth table for a function of two variables

x y | f(x,y)
-- | --
0 0 | 2 варианта
0 1 | 2 варианта
1 0 | 2 варианта
1 1 | 2 варианта

если посчитать все комбинации функции, то это 2'*2'*2'*2=2^4=2^(2^2)=16
n функций трех переменных = 2^(2^3)

x y | x*y | x+y | x xor y | x => y | x=y | x< >y |
-- | -- | -- | -- | -- | -- | -- |
0 0 | 0 | 0 | 0 | 1 | 1 | 0 |
0 1 | 0 | 1 | 1 | 1 | 0 | 1 |
1 0 | 0 | 1 | 1 | 0 | 0 | 1 |
1 1 | 1 | 1 | 0 | 1 | 1 | 0 |

xor - исключающее или, сложение по модулю 2
or - нестрогое или. так же антиэквиваленция
x => y - 2+2=4 => 4+4=8 само следование или рассуждение  (посылка и вывод) истино или ложно, пример:
* из истины следует истина 2+2=4 => 4+4=8 - это истина
* из истины следует ложь 2+2=4 => 4+4 =10 - это ложное, плохое рассуждение
* из лжи следует ложь 2+2=5 => 4+4=10 - если пришли из ложного к ложному, то "я в этом не виноват и это истина
* из джи следует истина 2+2=5 => 5=2+2 => 2+2=2+2 - из лжи может следовать истина

#### disjunctive normal form
the form defining logical function.
example for function with 3 arguments:

 x | y | z  | f  = | f1+ | f2+ | f3 
-- | -- | --| -- | -- | -- | -- 
0  | 0 | 0 | 1 = | 1 + | 0 + | 0 
0  | 0 | 1 | 0 = | 0 + | 0 + | 0 
0  | 1 | 0 | 0 = | 0 + | 0 + | 0 
0  | 1 | 1 | 1 = | 0 + | 1 + | 0 
1  | 0 | 0 | 0 = | 0 + | 0 + | 0 
1  | 0 | 1 | 0 = | 0 + | 0 + | 0 
1  | 1 | 0 | 1 = | 0 + | 0 + | 1 
1  | 1 | 1 | 0 = | 0 + | 0 + | 0 

f = ^x*^y*^z + ^x*y*z + x*y*^z - can we simplify this expression?

* operations with constant rules:
  * 0+x=x, 1+x=1, 0*x=0, 1*x=x
* simple rules:
  * A*A=A, A+A=A, A+^A=1, A*^A=0, A*(A+B)=A, A+A*B=A
* properties of logical operators "and" and "or":
  * (A*B)*C=A*(B*C)=A*B*C # associative
  * А*В=В*А, А+В=В+А # commutative
  *A*(B+C)=A*B+A*C, A+B*C=(A+B)*(A+C)# distributive for addition against multiplication and vise versa
* de-Morgan rules:
  * ^(A+B)=^A*^B, ^(A*B)=^A+^B
* double not
  * ^^A=A
* consequences:
  * A=>B=^A+B
  * (A==B)=A*B+^A*^B

### logical constructs in python
```python
flag = False
n = int(input())
for i in range (n):
  x = int(input())
  flag = (x % 10 == 0) or flag

flag = True
n = int(input())
for i in range (n):
  x = int(input())
  flag = (flag and x % 10 == 0) # is divisor of 10
print(flag)
```
#### nested and consequent if-s
consequent if
```python
x = int(input())
if x % 2 == 0:
  print('y')
if x % 3 == 0:
  print('y')
# above condition is contradiction for 6
# better refactor this way
if x % 2 == 0 or x % 3 == 0:
  print('y')
```
nested if
```python
x = int(input())
if x % 2 == 0:
  if x % 3 == 0:
    print('divisor of 6')
else:
  print('not divisor of 6')
# equivalent syntax
if x % 2 == 0 and x % 3 == 0:
  print('divisor of 6')
else:
  print('not divisor of 6')
```
#### cascaded if conditions
```python
# split of 1-d number axe
x = int(input())
if x < 0:
  print('A')
elif x < 5:
  print('B')
elif x < 10:
  print('C')
elif x > 10: # formally this is excessive, however this is a culture of code and exception handling
  print('D')
else:
  raise Exception # special catchers, which is a "signature" of a high quality developer (contract)

# split of 2-d area by ordinates and abscissa
x = int(input())
y = int(input())
if y > 0:
  if x > 0:
    print('I')
  else:
    print('II')
else:
  if x > 0:
    print('III')
  else:
    print('IV')
```
