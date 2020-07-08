from chromosome import Chromosome
from ea import EvolutionaryAlgorithmsInterface
from population import Population

class TSP(EvolutionaryAlgorithmsInterface):
    @staticmethod
    def run(genes, population_size, n_generation, tournament_size, mutation_rate): 
        population = Population.initial_population(genes, population_size)

    def evolve(self): 
        pass

    def crossover(self): 
        pass

    def mutate(self): 
        pass