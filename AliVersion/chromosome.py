import numpy as np

class  Chromosome():
    def __init__(self, length):
        self.genes = np.zeros(length, dtype=int)
        self.fitness = 0

    def fill(self, fill_method):
        self.genes = fill_method(self.genes)

    def calculate_fitness(self, weight_bound, data):
        value = np.sum(np.dot(self.genes, data[:, 0]))
        weight = np.sum(np.dot(self.genes, data[:, 1]))
        if weight <= weight_bound:
            self.fitness = value
        else:
            self.fitness = 0 

    def show(self):
        print(self.genes)
        print(self.fitness)