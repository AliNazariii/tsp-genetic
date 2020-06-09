import math

class Gene:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return 'City ' + str(self.name) + ':\t ' + str(self.x) + '\t' + str(self.y) + '\n'

    def distance(self, dest):
        return math.sqrt( ((dest.x - self.x) ** 2) + ((dest.y - self.y) ** 2) )