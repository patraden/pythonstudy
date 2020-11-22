# pythonstudy :memo:
## Lecture #12 [Link](https://www.youtube.com/watch?v=rEPggzaPoUw)
### вычисление соотношения Левенштейна
#### редакционное расстояние между строками (расстояние Левенштейна) O(n*m)

допустим есть два слова:
А="колокол"
В="молоко"
вопрос: сколько типографических опечаток нужно сделать в первом, чтобы получилось второе (кратчайшее редакционное расстояние)
топиграфические ошибки:
1. перепутали символ
1. вставили лишний символ
1.  потеряли нужный символ

физический смысл: данное расстояние позволяет измерять схожесть слов в пространстве всех слов алфавита
данная задача решается методом динамического программирования

len(A)=n
Len(B)=m
Fij={минимальное редакционное расстояние между срезами строк А[:i] и B[:j]}
ответ = Fnm

рекурентное соотношение
пусть:
A[:i]="a1a2...ai-1x"
B[:j]="b1b2...bj-1x"
тогда:
F=Fi-1j-1

пусть:
A[:i]="a1a2...ai-1x"
B[:j]="b1b2...bj-1y"
тогда нужно рассмотреть три варианта преобразования:
1. если посчитано расстояние между A[:i] без "x" и B[:j] то кратчайшее расстояние общее можно посчитать добавлением "x" (предполагаем ошибку 2))
1. если посчитано расстояние между A[:i] и B[:j] без "y" то кратчайшее расстояние общее можно посчитать добавлением "y" (предполагаем ошибку 2))
1. если посчитано расстояние между A[:i] без "x" и B[:j] без "y" то кратчайшее расстояние общее можно посчитать заменой "х" на "y" (предполагаем ошибку 1))
в итоге:
F=1+min(Fi-1j ; Fij-1 ; Fi-1j-1)

крайний случай:
если A[:i]=[], то F = len(B[:j])
F0j=j
Fi0=i
F00=0

```python
def levenstein(A,B):
 F=[[(i+j) if i*j==0 else 0 for j in range(len(B)+1)] for i in range(len(A)+1)]
 #обходить будем слева-направо, сверху-вниз
 for i in range(1,len(A)+1):
  for j in range(1,len(B)+1):
   if A[i-1]==B[j-1]:
    F[i][j]=F[i-1][j-1]
   else:
    F[i][j]=1+min(F[i-1][j],F[i][j-1],F[i-1][j-1])
 return F[len(A)][len(B)]
```

### проверка равенства строк
теоретически можно проверять равенство строк через расстояние левенштейна (==0)

но, однако, наивный поиск будет работать гораздо лучше
A="строки"
B="равны"
если строки равны по длине, то мы можем сделать это за O(N)

```python
def equal(a,b):
 if len(a)!=len(b):
  retrun False
 for i in range (len(a)):
  if a[i]!=b[i]:
   return False
 return True
```

### поиск подстроки в строке (очень интересная задачка, всем этим занимаются google, yandex и прочие)
s="abacabadabacabafabacabadabacabadabacabafaba"
в этой строке ищем подстроки "aba"
sub="dabac"
наивный поиск будет выглядеть как. Его сложность O(n,m)

```python
def equal(a,b):
 if len(a)!=len(b):
  retrun False
 for i in range (len(a)):
  if a[i]!=b[i]:
   return False
 return True

def search_substring(s,sub):
 for i in range(len(s)-len(sub)):
  if equal(s[i:i+len(sub)],sub):
   print(i)
```

будем изучать структуру самой строки
#### преефикс-функция PI строки
* собственный суффикс - окончание строки, либо суффикс не равный строке
* PI(s) - длин максимального собственного суффикса, который является префиксом
* PI(s)i - префикс-функция среза строки s[:i]

s="     |x     |      |x"
если sp+1=x (p длина максимального собственного суффикса), то PI(s)i=p+1, где p=PI(S)i-1

s="     |y     |      |x"
в этом случае возможно меньший префикс равен меньшему суффиксу

напишем на псевдокоде, **реализовать самостоятельно!**
PI=[0 for any i]
для всех i строки s:
 p=PI(S)i-1
 пока p > 0 и si!=sp+1
  p=PI(sp)
 если si=sp+1, то
  p+=1
 PI(s)i=p

```python
def pi_function(s:list="&&&&vv&&advvv&&"):
    pi=[0 for i in range(len(s))]
    for i in range(1,len(s)):
        p=pi[i-1]
        while p>0 and s[i]!=s[p]:
            p=pi[p-1]
        if s[i]==s[p]:
            p+=1
        pi[i]=p
    return pi
print(pi_function())
```

какой это имеет отношение к поиску подстроки в строке?
вычисление пи функции происзодит за O(n) - длина строки

#### алгоритм Кнута-Морриса-Пратта
s*=sub+"#" (спецсимвол) + s
когда PIi=len(sub) то это вхождение
в этом случае скорость поиска такая же как скорость вычисления пи-функции = O(n+m)


```python
def pi_function(s:list="&&&&vv&&advvv&&&"):
    """pi-functions returns the max string own suffix which is in turn its prefix
    (maximum string suffix cannot be equal to string)
    complexity is O(len(s))"""
    pi=[0 for i in range(len(s))]
    for i in range(1,len(s)):
        p=pi[i-1]
        while p>0 and s[i]!=s[p]:
            p=pi[p-1]
        if s[i]==s[p]:
            p+=1
        pi[i]=p
    return pi

def kmp(s="aueqdasdsaueqdahdksdakhueqdkjasgdkqwe",sub="ueq"):
    """ Algorythm of Knutt-Morris-Pratt to find substring in string based on pi-function.
    Complexity is O(len(s)+len(sub)).Key contrain = string and substring should not contain "#" special symbol
    """
    sub_l=len(sub)
    pi=pi_function(sub+'#'+s)
    indexes=[]
    for i in range(len(pi)):
        if pi[i]==sub_l:
            indexes.append(i-2*sub_l)
    return indexes

print(kmp())
#print(pi_function())
```
