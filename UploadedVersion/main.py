import utils
import random
import argparse
import tsp_ga as ga
from datetime import datetime

pop_size = 50
n_gen = 100
tourn_size = 20
mut_rate = 0.01

def run(pop_size, n_gen, tourn_size, mut_rate):
    genes = utils.get_genes_from('tsp_data.txt')

    print("-- Running TSP-GA with {} cities --".format(len(genes)))

    history = ga.run_ga(genes, pop_size, n_gen,
                        tourn_size, mut_rate)

    utils.plot(history['cost'], history['route'])


run(pop_size, n_gen, tourn_size, mut_rate)
