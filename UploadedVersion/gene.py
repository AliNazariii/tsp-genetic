
import math
class Gene:  # City
    def __init__(self, name, src, des):
        self.name = name
        self.src = src
        self.des = des

    def get_distance_to(self, dest):
        dist = math.sqrt((dest.src - self.src)**2 + (dest.des - self.des)**2)
        return dist
