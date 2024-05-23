class Pair:
    def __init__(self, point1: int, point2: int) -> None:
        self._pair = (point1, point2)

    def __setitem__(self, i, v):
        print("Error: Pair is immutable!")

    def __getitem__(self, i):
        return self._pair[i]

    def __repr__(self):
        return f"{self._pair}"

    def __eq__(self, y):
        return self[0] == y[0] and self[1] == y[1]
