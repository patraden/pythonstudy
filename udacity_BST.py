"""
>>> tree = BST(4)
>>> tree.insert(2)
>>> tree.insert(1)
>>> tree.insert(3)
>>> tree.insert(5)
>>> print (tree.search(4))
True
>>> print (tree.search(3))
True
>>> print (tree.search(6))
False
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        pass

    def search(self, find_val):
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
