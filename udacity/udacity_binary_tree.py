"""
    Test cases for module.
>>> tree = BinaryTree(1)
>>> tree.root.left = Node(2)
>>> tree.root.right = Node(3)
>>> tree.root.right.right = Node(13)
>>> tree.root.left.left = Node(4)
>>> tree.root.left.right = Node(5)
>>> tree.root.left.left.left = Node(6)
>>> tree.root.left.left.right = Node(16)
>>> print (tree.search(4))
True
>>> print (tree.search(5))
True
>>> print (tree.search(6))
True
>>> print (tree.search(26))
False
>>> print (tree.search(16))
True
>>> print (tree.print_tree())
6-16-4-5-2-13-3-1
"""


class Node(object):
    """Individual Node for Binary tree class"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    """Basic Binary tree class"""

    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Search tree nodes using helper method"""
        #        return self._preorder_search(self.root, find_val)
        return self._inorder_search(self.root, find_val)

    #        return self._postorder_search(self.root, find_val)

    def print_tree(self):
        """Print tree nodes using helper method"""
        #        return self._preorder_print(self.root,"")[:-1]
        return self._inorder_print(self.root, "")[:-1]

    #        return self._postorder_print(self.root,"")[:-1]

    def _preorder_search(self, start, find_val):
        """Search tree nodes in
        a pre-order traversal.
        Return True if the value
        is in the tree, return
        False otherwise."""
        return start.value == find_val or self._preorder_search(start.left, find_val) or self._preorder_search(
            start.right, find_val) if start else False

    def _inorder_search(self, start, find_val):
        """Search tree nodes in
        an in-order traversal.
        Return True if the value
        is in the tree, return
        False otherwise."""
        return self._inorder_search(start.left, find_val) or start.value == find_val or self._inorder_search(
            start.right, find_val) if start else False

    def _postorder_search(self, start, find_val):
        """Search tree nodes in
        a post-order traversal.
        Return True if the value
        is in the tree, return
        False otherwise."""
        return (self._postorder_search(start.left, find_val) or
                self._postorder_search(start.right, find_val) or start.value == find_val if start else False)

    def _preorder_print(self, start, traversal):
        """Print tree nodes in a pre-order traversal."""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self._preorder_print(start.left, traversal)
            traversal = self._preorder_print(start.right, traversal)
        return traversal

    def _inorder_print(self, start, traversal):
        """Print tree nodes in in-order traversal."""
        if start:
            traversal = self._inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self._inorder_print(start.right, traversal)
        return traversal

    def _postorder_print(self, start, traversal):
        """Print tree nodes in a post-order traversal."""
        if start:
            traversal = self._postorder_print(start.left, traversal)
            traversal = self._postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)
