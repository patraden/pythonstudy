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

_stack = []


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


def top():
    return _stack[-1]


def pop():
    return _stack.pop()


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


if __name__ == "__main__":
    # help('doctest')
    import doctest

    doctest.testmod(verbose=False)
