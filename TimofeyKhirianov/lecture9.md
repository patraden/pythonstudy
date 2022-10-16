## Lecture #9 [Link](https://www.youtube.com/watch?v=qf82-r9hl2Y)
#### recursive sorting
#### quick sort by Tony Hoare
 
* W(n*log(n))
* не всегда работает хорошо, существуют такие массивы, на которых она работает плохо как O(n*n)
* сортирующее действие выполняется на прямом ходу рекурсии не требует дополнительной памяти
* "разделяй и властвуй"

* Логически сортировка разбивает все на 3 группы:
1. группа "солдатов" меньше по росту произвольного "барьерного" элемента
2. группа равных по росту (этих дальше сортировать не надо)
3. группу тех, кто "выше"

#### merge sort
* O(nlog(n))
* сортирующее действие выполняется на обратном ходу рекурсии 
* нужно O(n) дополнительной памяти
 
* разделяем на два списка:
1. часть списка от 0 до n//2 не включительно
2. от n//2 включительно до n не включительно
* далее каждый список сортируется (как-то)
* потом сравниваем поэлементно и формируем конечный список (двигаемся по двум индексам).
* При равенстве элементов уславливаемся из какого списка взять первым и вторым
* в конце оин список будет пустым, а во втором последовательно
* отсортированною будут находиться "большие" элементы, которые достаточно "слиять"
* с результирующим списком

Сортировка называется ***устойчивой***, если она не меняет порядок равных элементов
(сортируемая характеристика может быть не единственной у объекта)
один и тот же алгоритм сортировки может быть реализован как устойчиво, так и неустойчиво

```python
def merge(a: list, b: list):
    """ Merges two sorted arrays into one."""
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:  # assume arrays sort is ascendant and stable (equal number ordering respected)
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):  #
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


def merge_sort(a: list):
    """ Recursive ascendant merge sort. """
    if len(a) <= 1:
        return
    middle = len(a) // 2
    left = [a[_] for _ in range(middle)]
    right = [a[_] for _ in range(middle, len(a))]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for i in range(len(a)):
        a[i] = c[i]
```
#### Cортировка Тони Хоара (QuickSort)
в самом питоне сортировка - прагматичная, которая является гибридом разных сортировок
случайный элемент выбираем первый (т.е. барьерный = 1 элементу массива)
```python
def quick_sort(a: list):
    """ Tony Hoare quick sort. """
    if len(a) <= 1:
        return  # None
    left = []
    middle = []
    right = []
    barrier = a[0]  # we can always change it to a random or some better logic
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    quick_sort(left)
    quick_sort(right)
    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1


if __name__ == "__main__":
    test1 = [3, 4, 5, 1, 2, 3, 4]
    quick_sort(test1)
    print(test1)
```
#### Проверка сортировки массива
```python
def check_sorted(a, ascending=True):
    """ Checks if array is sorted in O(n). """
    s = 2 * int(ascending) - 1
    for i in range(len(a)-1):
        if s * a[i] > s * a[i+1]:
            return False
    return True
```