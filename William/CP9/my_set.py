
class MySet:
    '''
    MySet should have the following behaviors:

    The MySet class should only store non-negative
    int values in its hash table.

    You may assume the input values dont collide in the hash table.
    This means you do not need to implement separate chaining.
    Recall that a collision is when two
    different values end up at the same index.

    Your hash table should be fixed-size and you shouldnt ever rehash.
    Make your hash table be size 10 and store it as a field with type list.

    You should implement these functions so that they all have complexity O(1).
    For this checkpoint, this means your program should not have any loops!

    All fields should be private.

    You should not use the set class in any way in your implementation.
    You should implement MySet using a list as your hash table.
    '''

    def __init__(self):
        """
        Initialize the hash set
        """
        self._hash_table = [0] * 10
        self._length = 0

    def add(self, v):
        """_summary_

        Args:
            v (_type_): _description_
        """
        hash = v % 10
        if (v not in self) and (self._hash_table[hash] == 0):
            self._length += 1
            self._hash_table[hash] = v

    def __contains__(self, v):
        """
        Args:
            v (_type_): _description_
        """
        return v in self._hash_table

    def __len__(self):
        """_summary_
        """
        return self._length
