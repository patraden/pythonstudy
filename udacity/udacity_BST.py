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
        """Insert new node to BST using helper method"""
        self._insert(self.root, new_val)

    def _insert(self, current, new_val):
        """Recursive BST insert"""
        if current.value < new_val:
            if current.right:
                self._insert(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self._insert(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        """Search node in BST using helper method"""
        return self._search(self.root, find_val)

    def _search(self, current, find_val):
        """Recursive BST search"""
        if current:
            if find_val == current.value:
                return True
            elif find_val < current.value:
                return self._search(current.left, find_val)
            else:
                return self._search(current.right, find_val)
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)
