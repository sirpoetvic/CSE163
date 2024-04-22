class Dog:
    """
    Represents a dog with a name
    """

    def __init__(self, name):
        """
        Initializes a new dog with the given name
        """
        self._name = name

    def bark(self):
        """
        Prints a message saying this dog barked
        """
        print(self._name + ': Woof')
