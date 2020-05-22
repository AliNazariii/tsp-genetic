from abc import ABCMeta, abstractmethod

class EvolutionaryAlgorithmsInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def crossover(self): 
        raise NotImplementedError

    @abstractmethod
    def mutate(self): 
        raise NotImplementedError