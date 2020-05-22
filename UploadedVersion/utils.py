import matplotlib.pyplot as plt
import tsp_ga as ga
import pandas as pd
from random import sample
from gene import Gene


def get_genes_from(fn, sample_n=0):
    file = open(fn, 'r')
    cities = []
    for line in file:
        details = list(map(float, line.split()))
        cities.append(
            Gene(name=int(details[0]), src=details[1], des=details[2]))
    file.close()
    return cities


def plot(costs, individual, save_to=None):
    plt.figure(1)

    plot_ga_convergence(costs)
    plt.show()
    plt.figure(2)

    plot_route(individual)
    plt.show()

    

def plot_ga_convergence(costs):
    x = range(len(costs))
    plt.title("GA Convergence")
    plt.xlabel('generation')
    plt.ylabel('cost')
    plt.text(x[len(x) // 2], costs[0],
             'min cost: {}'.format(costs[-1]), ha='center', va='center')
    plt.plot(x, costs, '-')


def plot_route(individual):
    for i in range(len(individual.genes)-1):
        x = [individual.genes[i].src, individual.genes[i+1].src]
        y = [individual.genes[i].des, individual.genes[i+1].des]
        plt.plot(x, y)
    
    x = [individual.genes[0].src, individual.genes[-1].src]
    y = [individual.genes[0].des, individual.genes[-1].des]
    plt.plot(x,y)
    plt.show()
