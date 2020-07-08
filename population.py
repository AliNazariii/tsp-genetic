from chromosome import Chromosome
from random import sample

class Population:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes

    @staticmethod
    def initial_population(cities, population_size):
        routes = []
        for _ in range(population_size):
            routes.append(Population.router(cities))
        return Population(routes)

    @staticmethod
    def router(cities):
        return sample(cities, len(cities))

    def __repr__(self):
        return str(self.chromosomes).replace(",", " ")