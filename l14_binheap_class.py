"""
binary heap class using list
>>> a=binheap()
>>> a.currentSize
0
>>> a.buildHeap([9,5,6,2,3])
>>> print(a.delMin())
2
>>> print(a.delMin())
3
>>> print(a.delMin())
5
>>> print(a.delMin())
6
>>> print(a.delMin())
9
>>> print(a.delMin())
Traceback (most recent call last):
    ...
AssertionError
"""

class binheap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def _percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self._percUp(self.currentSize)
    def _minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def percDown(self,i):
         while (i * 2) <= self.currentSize:
            mc = self._minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
    def delMin(self):
        assert self.currentSize >= 1
        value = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return value
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
