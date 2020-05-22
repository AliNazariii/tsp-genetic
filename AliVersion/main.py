from knapsack import Knapsack
from tsp import TSP

# knapsack_input_data = './knapsack_1.txt'
# knapsack = Knapsack(input_data=knapsack_input_data, population_size=800, max_generation=50)
# knapsack.run()

# knapsack_input_data = './knapsack_2.txt'
# knapsack = Knapsack(input_data=knapsack_input_data, population_size=800, max_generation=50)
# knapsack.run()

# knapsack_input_data = './knapsack_3.txt'
# knapsack = Knapsack(input_data=knapsack_input_data, population_size=800, max_generation=50)
# knapsack.run()

tsp_input_data = './tsp_data.txt'
tsp = TSP(input_data=tsp_input_data, population_size=100, max_generation=200)
tsp.run()
