import numpy as np

class City:
    def __init__(self, data):
        self.x = data[1]
        self.y = data[2]

    def distance(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        return np.sqrt((x_distance ** 2) + (y_distance ** 2))
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"