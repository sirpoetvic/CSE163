# Write your solution here!
class Pair:
    # You can assume the client will only access index 0 or 1 for a Pair
    def __init__(self, v1, other):
        self._values = (v1, other)

    def __eq__(self, other):
        return self._values == other

    def __repr__(self):
        return (f'{self._values}')

    def __getitem__(self, idx):
        return self._values[idx]

    def __setitem__(self, idx, val):
        print('Error: Pair is immutable!')
        return -1
