# Write your solution here!
class DogPack:
    def __init__(self) -> None:
        """Initializes the DogPack"""
        self._dogs = []

    def add_dog(self, dog):
        """Adds dog to the end of the list _dogs
        Args:
            dog (Dog): Object dog to be added
        """
        self._dogs.append(dog)

    def all_bark(self):
        for dog in self._dogs:
            dog.bark()
