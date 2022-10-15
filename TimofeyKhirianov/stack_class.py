"""
stack class using list type
>>> a=Stack()
>>> a.clear()
>>> a.is_empty()
True
>>> a.push(1)
>>> a.push(2)
>>> a.push(3)
>>> a.is_empty()
False
>>> a.size()
3
>>> a.top()
3
>>> a.pop()
3
>>> a.pop()
2
>>> a.pop()
1
>>> a.is_empty()
True
"""


class Stack:
    def __init__(self):
        self.items = []

    def clear(self):
        self.items.clear()

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)
