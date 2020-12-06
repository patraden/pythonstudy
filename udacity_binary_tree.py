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
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
#        return self.preorder_search(self.root, find_val)
#        return self.inorder_search(self.root, find_val)
        return self.postorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
#        return self.preorder_print(self.root,"")[:-1]
#        return self.inorder_print(self.root,"")[:-1]
        return self.postorder_print(self.root,"")[:-1]

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left,find_val) or self.preorder_search(start.right,find_val)
        return False

    def inorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            return self.inorder_search(start.left,find_val) or start.value == find_val or self.inorder_search(start.right,find_val)
        return False

    def postorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            return self.inorder_search(start.left,find_val) or self.inorder_search(start.right,find_val) or start.value == find_val
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
