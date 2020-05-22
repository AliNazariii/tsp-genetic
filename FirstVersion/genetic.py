import random
from Fittness import Fitness
import operator
import numpy as np


class genetic:
    def __init__(self, cities):
        self.cities = cities
        random.seed(78)

    # create a random path.
    def create_path(self):
        return random.sample(self.cities, len(self.cities))

    # initial population in first time.
    def initial_population(self, population_size):
        population = []
        for _ in range(population_size):
            population.append(self.create_path())
        return population

    def next_generation(self, current_population, elite_size, mutation_rate):
        population_raked = self.rank_path(current_population)
        selection_results = self.selection(population_raked, elite_size)
        print(selection_results)
        mating_pool = self.mating_pool(current_population, selection_results)
        for x in mating_pool:
            for y in x:
                print(y)
        children = self.breed_population(
            mating_pool, elite_size, len(current_population))
        next_population = self.mutate_population(children, mutation_rate)
        return next_population

    def rank_path(self, current_population):
        results = {}
        for index, path in enumerate(current_population):
            results[index] = Fitness(path).getFitness()
        # return the list of cities as tuple (index, fitness) sorted.
        return sorted(results.items(), key=operator.itemgetter(1), reverse=True)

    def selection(self, population_raked, elite_size):
        cities = [city for city, _ in population_raked]
        fitnesses = [fitness for _, fitness in population_raked]
        fitness_sum = sum(fitnesses)
        probabilities = np.array(
            [fitness / fitness_sum for _, fitness in population_raked])
        return np.random.choice(cities, elite_size, p=probabilities).tolist()

    def mating_pool(self, current_population, selection_results):
        matingpool = []
        for path_id in selection_results:
            matingpool.append(current_population[path_id])
        return matingpool

    def breed_population(self, mating_pool, elite_size, pop_size):
        children = []
        length = pop_size - elite_size
        pool = random.sample(mating_pool, len(mating_pool))

        children.extend(mating_pool)

        for i in range(length):
            first_parent, second_parent = random.randint(
                0, len(mating_pool)-1), random.randint(0, len(mating_pool)-1)

            child = self.breed(mating_pool[first_parent], mating_pool[second_parent])
            print("============================")
            for city in child:
                print(city)
            children.append(child)
        
        return children

    def mutate_population(self, children, mutation_rate):
        mutatedPop = []

        for ind in range(0, len(children)):
            mutatedInd = self.mutate(children[ind], mutation_rate)
            mutatedPop.append(mutatedInd)
        return mutatedPop

    def mutate(self, individual, mutation_rate):
        for swapped in range(len(individual)):
            if(random.random() < mutation_rate):
                swapWith = int(random.random() * len(individual))

                city1 = individual[swapped]
                city2 = individual[swapWith]

                individual[swapped] = city2
                individual[swapWith] = city1
        return individual

    def breed(self, parent1, parent2):
        child = []
        childP1 = []
        childP2 = []

        geneA = int(random.random() * len(parent1))
        geneB = int(random.random() * len(parent1))

        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)

        for i in range(startGene, endGene):
            childP1.append(parent1[i])

        childP2 = [item for item in parent2 if item not in childP1]

        child = childP1 + childP2
        return child
