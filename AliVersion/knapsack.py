import numpy as np
from evolutionary_algorithm import EvolutionaryAlgorithm
from chromosome import Chromosome

class Knapsack(EvolutionaryAlgorithm):
    def __init__(self, input_data, population_size, max_generation):
        super().__init__(population_size, max_generation)
        self.data = self.read_input_file(input_data)

    def read_input_file(self, input_data):
        input_file = open(input_data, "r")
        self.length, self.weight_bound = np.array(input_file.readline().split(), dtype=int)

        data = np.empty((self.length, 2))
        for i in range(self.length):
            data[i][0], data[i][1] = np.array(input_file.readline().split())

        return data.astype(int)

    def fill_random(self, genes):
        for i in range(self.length):
            index = np.random.randint(genes.shape[0])
            genes[index] = 1
            if np.sum(np.dot(genes, self.data[:, 1])) > self.weight_bound:
                genes[index] = 0
        return genes

    def calculate_fitness(self):
        for i in range(self.population_size):
            self.population[i].calculate_fitness(self.weight_bound, self.data)
    
    def run(self):
        self.initial_population(self.length, self.fill_random)
        super().run()

    def crossover(self):
        father = self.population[np.random.randint(self.population_size)]
        mother = self.population[np.random.randint(self.population_size)]

        crossover_point = np.random.randint(self.length)

        child = Chromosome(self.length)
        child.genes[:crossover_point] = father.genes[:crossover_point] 
        child.genes[crossover_point:] = mother.genes[crossover_point:] 
        return child

    def mutation(self):
        mutation_chance = 0.05
        for i in range(self.population_size):
            if mutation_chance > np.random.normal(0, 1):
                gene_index = np.random.randint(self.length)
                if self.population[i].genes[gene_index] == 1:
                    self.population[i].genes[gene_index] = 0
                else:
                    self.population[i].genes[gene_index] = 1