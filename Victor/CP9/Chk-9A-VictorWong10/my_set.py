class MySet:
    """
    MySet should have the following behaviors:

    The MySet class should only store non-negative int values in its hash table.

    You may assume the input values don’t collide in the hash table. This means you
    do not need to implement separate chaining. Recall that a collision is when two
    different values end up at the same index.

    Your hash table should be fixed-size and you shouldn’t ever rehash. Make your
    hash table be size 10 and store it as a field with type list.

    You should implement these functions so that they all have complexity O(1).
    For this checkpoint, this means your program should not have any loops!

    All fields should be private.

    You should not use the set class in any way in your implementation. You
    should implement MySet using a list as your hash table.
    """

    def __init__(self):
        """
        Create the HashSet
        """
        self._hashtable = [0] * 10
        self._length = 0

    def add(self, v):
        """
        adds "v" to the HashSet if not already in

        Args:
            v (_type_): value to add
        """
        hash = v % 10
        # chaining not necessary
        if (v not in self._hashtable) and (self._hashtable[hash] == 0):
            self._length += 1
            self._hashtable[hash] = v

    def __contains__(self, v):
        """
        returns if v is present in the HashSet

        Args:
            v (_type_): value to check presence of
        """
        return v in self._hashtable

    def __len__(self):
        """
        returns the number of items in the HashSet
        """
        return self._length
