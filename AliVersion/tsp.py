import numpy as np
from evolutionary_algorithm import EvolutionaryAlgorithm
from chromosome import Chromosome
from city import City
from itertools import permutations
from random import shuffle
import matplotlib.pyplot as plt
import math

class TSP(EvolutionaryAlgorithm):
    def __init__(self, input_data, population_size, max_generation):
        super().__init__(population_size, max_generation)
        self.cities = self.read_input_file(input_data)    
        self.chromosome_number = 0

    def read_input_file(self, input_data):
        input_file = open(input_data, "r")
        data = np.empty((0, 3)).astype(float)
        for line in input_file:
            data = np.vstack([data, np.array(line.split()).astype(float)])

        self.length = data.shape[0]

        cities = np.empty(self.length, dtype=City)
        for i in range(self.length):
            cities[i] = City(data[i])
        return cities

    def run(self):
        self.initial_population(self.length + 1, self.fill_greedy)
        super().run()

    def fill_random(self, genes):
        city_range = list(range(self.length))
        shuffle(city_range)
        for i in permutations(city_range):
            route = i + (i[0],)
            return np.array(route)

    def fill_greedy(self, genes):
        route = np.zeros(self.length + 1, dtype=int)

        current = self.chromosome_number % self.length

        route[0] = current
        route[self.length] = current

        remained_cities = list(range(self.length))
        
        for i in range(1, self.length - 1):
            remained_cities.remove(current)
            current = self.nearest_neighbor(self.cities[current], remained_cities)
            route[i] = current

        route[self.length - 1] = remained_cities[0]
        self.chromosome_number += 1
        return route

    def nearest_neighbor(self, city, city_list):
        nearest = None
        distance = math.inf
        for i in city_list:
            if city.distance(self.cities[i]) < distance:
                distance = city.distance(self.cities[i])
                nearest = i
        return nearest

    def calculate_fitness(self):
        for i in range(self.population_size):
            distance = 0
            for j in range(self.length):
                current_city = self.cities[self.population[i].genes[j]]
                next_city = self.cities[self.population[i].genes[j + 1]]
                distance += current_city.distance(next_city)
            self.population[i].fitness = -distance

    def crossover(self):
        father = self.population[np.random.randint(int(self.population_size / 2), self.population_size)]
        mother = self.population[np.random.randint(int(self.population_size / 2), self.population_size)]
        turn = 'father'

        child = Chromosome(self.length + 1)
        visited = np.zeros(self.length, dtype=int)


        copied = 0

        while copied < self.length:
            index = 0
            while visited[index] == 1:
                index += 1
            while visited[index] == 0:
                visited[index] = 1
                if turn == 'father':
                    child.genes[index] = father.genes[index]
                    index = np.where(father.genes == mother.genes[index])[0][0]
                else:
                    child.genes[index] = mother.genes[index]
                    index = np.where(mother.genes == father.genes[index])[0][0]
                copied += 1
            turn = 'mother'

        child.genes[self.length] = child.genes[0]
        return child

    def mutation(self):
        mutation_chance = 0.05
        for i in range(self.population_size):
            if mutation_chance > np.random.normal(0, 1):
                first_city = np.random.randint(1, self.length)
                second_city = np.random.randint(1, self.length)
                self.population[i].genes[first_city], self.population[i].genes[second_city] = self.population[i].genes[second_city], self.population[i].genes[first_city]

    def draw(self, path):
        plt.close()
        for i in range(self.length):
            begin_city_index = path[i]
            end_city_index = path[i + 1]
            x = [self.cities[begin_city_index].x, self.cities[end_city_index].x]
            y = [self.cities[begin_city_index].y, self.cities[end_city_index].y]
            plt.plot(x, y)
        plt.show()