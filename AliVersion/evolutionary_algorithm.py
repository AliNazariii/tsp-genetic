import numpy as np
from chromosome import Chromosome

class  EvolutionaryAlgorithm():
    def __init__(self, population_size, max_generation):
        self.length = None
        self.weight_bound = None
        self.population_size = population_size
        self.population = np.empty(self.population_size, dtype=Chromosome)
        self.max_generation = max_generation
        self.children_length = int(0.6 * self.population_size)

    def initial_population(self, length, fill_method):
        for i in range(self.population_size):
            self.population[i] = Chromosome(length)
            self.population[i].fill(fill_method)
            
    def run(self):
        for i in range(self.max_generation):
            self.selection()
            self.generation_report(i + 1, self.population[self.population_size - 1], self.population[0])

            children = np.empty(self.children_length, dtype=Chromosome)
            for i in range(self.children_length):
                children[i] = self.crossover()

            self.population[0:self.children_length] = children
            self.mutation()
        
        self.selection()
        self.generation_report(self.max_generation, self.population[self.population_size - 1], self.population[0])
        self.draw(self.population[self.population_size - 1].genes)

    def selection(self):
        self.calculate_fitness()
        for i in range(self.population_size):
            for j in range(i, self.population_size):
                if self.population[i].fitness > self.population[j].fitness:
                    self.population[i], self.population[j] = self.population[j], self.population[i]

    def crossover(self):
        pass

    def mutation(self):
        pass

    def calculate_fitness(self):
        pass

    def generation_report(self, generation_number, best_chromosome, worst_chromosome):
        print("\n")
        print("Generation #" + str(generation_number) + ":")
        print("Worst: " + str(abs(worst_chromosome.fitness)))
        print("Best: " + str(abs(best_chromosome.fitness)))

    def draw(self, path):
        pass