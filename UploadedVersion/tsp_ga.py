from sys import maxsize
from time import time
from random import random, randint, sample
from haversine import haversine
from Population import Population 
from chromosome import Chromosome


def evolve(pop, tourn_size, mut_rate):
    new_generation = Population([])
    pop_size = len(pop.individuals)
    elitism_num = pop_size // 2

    # Elitism
    for _ in range(elitism_num):
        fittest = pop.get_fittest()
        new_generation.add(fittest)
        pop.rmv(fittest)

    # Crossover
    for _ in range(elitism_num, pop_size):
        parent_1 = selection(new_generation, tourn_size)
        parent_2 = selection(new_generation, tourn_size)
        child = crossover(parent_1, parent_2)
        new_generation.add(child)

    # Mutation
    for i in range(elitism_num, pop_size):
        mutate(new_generation.individuals[i], mut_rate)

    return new_generation


def crossover(parent_1, parent_2):
    def fill_with_parent1_genes(child, parent, genes_n):
        start_at = randint(0, len(parent.genes)-genes_n-1)
        finish_at = start_at + genes_n
        for i in range(start_at, finish_at):
            child.genes[i] = parent_1.genes[i]

    def fill_with_parent2_genes(child, parent):
        j = 0
        for i in range(0, len(parent.genes)):
            if child.genes[i] == None:
                while parent.genes[j] in child.genes:
                    j += 1
                child.genes[i] = parent.genes[j]
                j += 1

    genes_n = len(parent_1.genes)
    child = Chromosome([None for _ in range(genes_n)])
    fill_with_parent1_genes(child, parent_1, genes_n // 2)
    fill_with_parent2_genes(child, parent_2)

    return child


def mutate(individual, rate):
    for _ in range(len(individual.genes)):
        if random() < rate:
            sel_genes = sample(individual.genes, 2)
            individual.swap(sel_genes[0], sel_genes[1])


def selection(population, competitors_n):
    return Population(sample(population.individuals, competitors_n)).get_fittest()


def run_ga(genes, pop_size, n_gen, tourn_size, mut_rate):
    population = Population.gen_individuals(pop_size, genes)
    history = {'cost': [population.get_fittest().travel_cost]}
    counter, generations, min_cost = 0, 0, maxsize
    while counter < n_gen:
        population = evolve(population, tourn_size, mut_rate)
        cost = population.get_fittest().travel_cost

        if cost < min_cost:
            counter, min_cost = 0, cost
        else:
            counter += 1

        generations += 1
        history['cost'].append(cost)

    history['generations'] = generations
    history['route'] = population.get_fittest()

    return history