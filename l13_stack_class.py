"""
stack class using list type
>>> a=stack()
>>> a.clear()
>>> a.isEmpty()
True
>>> a.push(1)
>>> a.push(2)
>>> a.push(3)
>>> a.isEmpty()
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
>>> a.isEmpty()
True
"""

class stack:
     def __init__(self):
         self.items = []
     def clear(self):
         self.items.clear()
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def top(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
