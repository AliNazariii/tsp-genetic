from Chromosome import Route
from random import sample


class Population:
    def __init__(self, routes):
        self.routes = routes

    @staticmethod
    def initial_population(pop_size, cities):
        individuals = []
        for _ in range(pop_size):
            individuals.append(Route(sample(cities, len(cities))))
        return Population(individuals)

    def get_fittest_route(self):
        fittest = self.routes[0]
        for route in self.routes:
            if route.fitness > fittest.fitness:
                fittest = route
        return fittest

    def remove_route(self, route):
        self.routes.remove(route)

    def add_route(self, route):
        self.routes.append(route)
