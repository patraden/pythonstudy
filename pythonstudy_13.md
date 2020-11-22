# pythonstudy :memo:
## Lecture #13 [Link](https://www.youtube.com/watch?v=L4IU1bPKvHM)
### стуктуры данных
#### стек (очередь LIFO)

"first in - first out"
"пришли в порядке 1,2,3 == ушли в порядке 3,2,1"
базовые операции над стеком
* push
* pop
* stack size
* top (study/touch top element without changing/pop)
* is_empty
* clear()
как такое реализовать?
продумает использую структурное программирование

use case:
1. clear()
1. push(1)
1. push(2)
1. push(3)
1. pop() #3
1. pop() #2
1. pop() #1
1. is_empty() #True

##### реализации
* A_stacke: на массиве list
* B_stack: на односвязном списке

```python
"""
Модуль, описывающий структуру данных - стек
>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
"""

_stack=[]

def push(x):
    """
    добавляет элемент x в конец стека
    >>> size = len(_stack)
    >>> push(5)
    >>> len(_stack)-size
    1
    >>> _stack[-1]
    5
    """
    _stack.append(x)
def pop():
    return _stack.pop()
def clear():
    _stack.clear()
def is_empty():
    return len(_stack)==0

if __name__ == "__main__":
    # help('doctest')
    import doctest
    doctest.testmod(verbose=False)
    doctest.testmod()
```
##### проверка корректности скобочной последовательности
правила (схоже с определением регулярного языка)
* A=""-корректное скобочное выражение
* B=(A) - корректное скобочное выражения
* C=AB = корретное скобочное выражение
  * "((()))()(((())))" - корректно
  * "())(()" - некоррктно (хотя количество отк и закр скобок одинковы

* f(n) - функция кол-ва скобок по кол-ву символов
* f(n) - не должно быть < 0 (это будет признак некорректного выражения)
таким образом, если  у нас только 1 вид скобок, то стек даже не нужен

рассмотри () и []

* A=""-корректное скобочное выражение
* B=(A) - корректное скобочное выражения
* C=AB = корретное скобочное выражение
* B=[A] - корректное
  * "[(())]([])" - корректно
  * "[)" - некорректно, "[(])" - тоже некорректно и функция счетчиков не поймает такие выражения, поскольку надо помнить последнюю открытую скобку

алгоритм:
для каждой очередной скобки:
 если она открывающаяся:
  тогда - в стек
 иначе:
  если стек пуст:
   то - все, некорректно
  иначе:
   x=pop()
   если x не соотвествует y-скобке:
    то все, выход

если стек пусть, то все корректно, а иначе нет

```python
import l13_stack as A_stack
def is_brackets_sequence_correct(s:str):
    """
    проверяет корректность скобочной последовательности
    из круглых и квадратных скобок () []
    >>> is_brackets_sequence_correct("(([()]))[]")
    True
    >>> is_brackets_sequence_correct("(])]")
    False
    >>> is_brackets_sequence_correct("(")
    False
    >>> is_brackets_sequence_correct("]")
    False
    """
    for bracket in s:
        if bracket not in "()[]":
            continue
        if bracket in "([": # даннный поиск подстроки в строке разобтает гораздо хуже z-function, но для коротких строк его можно использовать
            A_stack.push(bracket)
        else: # bracket in ")]"
            assert bracket in ")]", "Ожидалась закрывающая скобка!" + str(bracket)
            if A_stack.is_empty():
                return False
            left = A_stack.pop()
            assert left in "([" , "Ожидалась открывающая скобка!" + str(left)
            if left == "(":
                right = ")"
            else:
                right = "]"
            if right != bracket:
                return False
    return A_stack.is_empty()

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```
##### обратная польская нотация
данный алгоритм вычисляет арифметических выражений в постфиксной записи(нотации)
[5,2,'+'] <==> 5+2
(2+7)*5 <==> [2,7,+,5,*]
2+7*5 <==> [2,7,5,*,+]

для каждого <токен>:
если очередной <токен> -чилсо
то мы его кладем в стек
иначе - он операция, мы берем со стека два операнда
y=pop()
x=pop()
вычисляем результат операции z=x операция y
и резульатат кладем в стек
push(z)

в результате останется одно числео в стеке - результат оперции
result=pop()
