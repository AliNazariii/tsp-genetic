from abc import ABCMeta, abstractmethod

class EvolutionaryAlgorithmsInterface:
    """ 
    This is an Interface that should be implemented by Genetic Algorithms 
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self): 
        """ This method must be overridden """
        raise NotImplementedError

    @abstractmethod
    def evolve(self): 
        """ This method must be overridden """
        raise NotImplementedError

    @abstractmethod
    def crossover(self): 
        """ This method must be overridden """
        raise NotImplementedError

    @abstractmethod
    def mutate(self): 
        """ This method must be overridden """
        raise NotImplementedError