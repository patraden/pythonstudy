"""
Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.

>>> hash_table = HashTable()
>>> print (hash_table.calculate_hash_value('UDACITY'))
8568
>>> print (hash_table.lookup('UDACITY'))
-1
>>> hash_table.store('UDACITY')
>>> print (hash_table.lookup('UDACITY'))
8568
>>> hash_table.store('UDACIOUS')
>>> print (hash_table.lookup('UDACIOUS'))
8568
"""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        _hash = self.calculate_hash_value(string)
        if self.table[_hash]:
            self.table[_hash].append(string)
        else:
            self.table[_hash]=[string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        _hash = self.calculate_hash_value(string)
        if self.table[_hash]:
            for item in self.table[_hash]:
                if item==string:
                    return _hash
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return ord(string[0])*100+ord(string[1])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
