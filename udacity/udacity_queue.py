"""
Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!

>>> q = Queue(1)
>>> q.enqueue(2)
>>> q.enqueue(3)
>>> print (q.peek())
1
>>> print (q.dequeue())
1
>>> q.enqueue(4)
>>> print (q.dequeue())
2
>>> print (q.dequeue())
3
>>> print (q.dequeue())
4
>>> q.enqueue(5)
>>> print (q.peek())
5
"""


class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
