# Write your solution here!
class DogPack:
    def __init__(self):
        self._dogs = []

    def add_dog(self, Dog):
        self._dogs.append(Dog)

    def all_bark(self):
        for i in self._dogs:
            # i have no clue why this can be used without importing?
            barking = i.bark()
        return barking
