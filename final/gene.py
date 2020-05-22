import math

class Gene:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.name) + '-> (' + str(self.x) + ', ' + str(self.y) + ')'

    def distance(self, dest):
        return math.sqrt( ((dest.x - self.x) ** 2) + ((dest.y - self.y) ** 2) )