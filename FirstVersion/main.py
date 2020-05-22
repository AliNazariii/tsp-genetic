# import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt
from City import City
from genetic import genetic
import matplotlib.pyplot as plt


'''
    test city and fitness
'''

file = open('tsp_data.txt', 'r')
cities = []
for line in file:
    details = list(map(float, line.split()))
    cities.append(City(index=int(details[0]), x=details[1], y=details[2]))
file.close()

# cities = [City(0, 0, 0), City(2, 2, 2), City(
#     4, 3, 3), City(5,5,5)]
# , City(3, 3, 3), City(4, 4, 4), City(
# 5, 5, 5), City(6, 6, 6), City(7, 7 ,7), City(
# 8, 8, 8), City(9, 9, 9), City(10, 10, 10)

popSize = 5
eliteSize = 2
mutationRate = 0.001
generations = 50

genetic = genetic(cities)
pop = genetic.initial_population(popSize)
# for i, choromom in enumerate(pop):
#     print(str(i) + " chr -> ")
#     for city in choromom:
#         print("\t" + str(city)
#               )

# print(genetic.rank_path(pop))
# print("Initial distance: " + str(1 / genetic.rank_path(pop)[0][1]))

# for i in range(0, generations):
#     pop = genetic.next_generation(pop, eliteSize, mutationRate)

# print("Final distance: " + str(1 / genetic.rank_path(pop)[0][1]))

# bestRouteIndex = genetic.rank_path(pop)[0][0]
# bestRoute = pop[bestRouteIndex]
# print("ssssssssssssssssssssssssssss , "+ str(genetic.rank_path(pop)[0][1]))
# for x in bestRoute:
#     print(x)

progress = []
progress.append(1 / genetic.rank_path(pop)[0][1])

for i in range(generations):
    pop = genetic.next_generation(pop, eliteSize, mutationRate)
    progress.append(1 / genetic.rank_path(pop)[0][1])

plt.plot(progress)
plt.ylabel('Distance')
plt.xlabel('Generation')
plt.show()
