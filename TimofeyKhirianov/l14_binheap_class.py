"""
binary heap class using list
>>> a=BinHeap()
>>> a.currentSize
0
>>> print(a)
[]
>>> a.BuildHeap([10,9,5,6,2,3,12,13,14,11,4,5,3,45])
>>> print(a)
[2]
[4, 3]
[6, 9, 3, 12]
[13, 14, 11, 10, 5, 5, 45]
"""


class BinHeap(object):
    """Binary Heap Tree based on python list"""

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def __str__(self):
        """Prints BinHeap per level, top to bottom."""
        level = 1
        result = ""
        while 2 ** level - 1 <= self.currentSize:
            result += str(self.heapList[2 ** (level - 1):2 ** level]) + "\n"
            level += 1
        return result + str(self.heapList[2 ** (level - 1):])

    def _percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self._percUp(self.currentSize)

    def _minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
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

    def BuildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
