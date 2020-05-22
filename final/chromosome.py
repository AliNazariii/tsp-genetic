class Chromosome: 
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0

    def swap(self, first, second):
        self.genes[first], self.genes[second] = self.genes[second], self.genes[first]
    
    def calc_fitness(self):
        distance = 0
        for i in range(len(self.genes) - 1):
            distance += self.genes[i].distance(self.genes[i + 1])
        distance += self.genes[-1].distance(self.genes[0])
        self.fitness = -distance