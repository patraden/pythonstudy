## Lecture #4 [Link](https://www.youtube.com/watch?v=DvsCUI5FNnI)
### функции
```python
def hello():
    print("hello world")

hello()
f=hello # f links to the same function
f()
```

```python
def hello(name="World"):
    print("hello", name)

def max2(x,y):
    if x>y:
        return x # дальнейшее выполнение прекращается!
    return y

def max3(x,y,z):
    return max2(x,max2(y,z))

hello("John")
hello()
print(max3(5,2,7))
print(max3(1.5,0.2,17))
print(max3('ab', 'abc','abd')) # duck typing rule. Утиный полиморфизм или утиные типизация. "Если что-то плавает как утка, крякает как утка, то это утка"
# 'кит' < 'кот'
# 'кот' < 'котенок' # сравнение строк идет посимвольно и по алфавиту
```

```python
def hello_separated(name="World", separator="-"):
    print("Hello",name,sep=separator)

hello_separated(separator="***",  # Hello***World
                name = "John")
```
call stack, стек вызовов функции
main => FA => FB => FC => FD
если функции будут себя вызывать бесконечно, то будет происходить переполнения стека вызовов функции
стек вызовов функций необходим для error handling и его питон выводит на экран при ошибке

#### Структурное программирование

Проектирование "сверху-вниз"
Предположим мы строим дом

O       O        O        O
/|\ <=> /|\  <=> /|\  <=> /|\
/\      /\       /\       /\

заказчик, менеджер, архитектор, прораб
важно формализовать список параметров для заказа дома, например: локация и точка, размер
важно проектировать от функций верхнего уровня, до функций нижнего
процесс состоит из этапа "мечтания о программе" и "приземления"
вначале все функции "пустышки", но мы описываем взаимодействие между ними и параметры. Делаем наброски.
Потом описываем документ-строки описывая, что каждая из функций делает. Заземляем и получаем следующую версию

```python
def build_house():
    """ Функция, которая рисует дом """
    pass

build_house()
print('Ура! Дом построен!')
```
#### метод грубой силы (brute force)

область определения функции
область значения функции
шпростейший алгоритм перебора. это обычно и называется методом грубой силы

```python
def is_simple_number(x: int) -> bool:
    """ Validates if integer number is simple. """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def factorize_number(x: int):
    """ Factorizes integer number. """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1


if __name__ == "__main__":
    factorize_number(999)
    print(is_simple_number(19))
```
