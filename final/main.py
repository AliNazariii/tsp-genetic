import utils
import tsp

population_size = 50
n_generation = 100
tournament_size = 20
mutation_rate = 0.01 
input_path = './tsp_data.txt'   

def main():
    genes = utils.parse_input(input_path)

    print("Running Genetic Algorithm on TSP problem with {} cities.".format(len(genes)))

    # result = tsp.run(genes, population_size, n_generation, tournament_size, mutation_rate)

    # utils.plot(result['cost'], result['route'])

if __name__ == "__main__":
    main()