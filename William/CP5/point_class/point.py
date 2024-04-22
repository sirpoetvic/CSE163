# Point Class, CP4, Lesson 13
#
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def display(self):
        x = self.get_x()
        y = self.get_y()
        return (x, y)


p = Point(1, 2)
print(p.get_x())    # 1
p.set_y(4)
print(p.display())  # '(1, 4)'
