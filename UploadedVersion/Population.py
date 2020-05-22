from chromosome import Chromosome
from random import sample

class Population:  # Population of individuals
    def __init__(self, individuals):
        self.individuals = individuals

    @staticmethod
    def gen_individuals(sz, genes):
        individuals = []
        for _ in range(sz):
            individuals.append(Chromosome(sample(genes, len(genes))))
        return Population(individuals)

    def add(self, route):
        self.individuals.append(route)

    def rmv(self, route):
        self.individuals.remove(route)

    def get_fittest(self):
        fittest = self.individuals[0]
        for route in self.individuals:
            if route.fitness > fittest.fitness:
                fittest = route

        return fittest
