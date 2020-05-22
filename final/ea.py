from abc import ABCMeta, abstractmethod

class EvolutionaryAlgorithmsInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self): 
        raise NotImplementedError

    @abstractmethod
    def evolve(self): 
        raise NotImplementedError

    @abstractmethod
    def crossover(self): 
        raise NotImplementedError

    @abstractmethod
    def mutate(self): 
        raise NotImplementedError