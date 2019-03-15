from Population import Population
from Tour import Tour
import random

class GeneticAlgorithm:
    def __init__(self, tourManager):
        self.tourManager = tourManager
        self.mutationRate = 0.015
        self.tournamentSize = 5
        self.elitism = True

    def evolvePopulation(self, inPopulation):
        population = Population(self.tourManager, inPopulation.populationSize(), False)
        elitismOffset = 0
        if self.elitism:
            population.saveTour(0, inPopulation.getFittest())
            elitismOffset = 1

        for i in range(elitismOffset, population.populationSize()):
            parenti = self.tournamentSelection(inPopulation)
            parentii = self.tournamentSelection(inPopulation)
            child = self.crossover(parenti, parentii)
            population.saveTour(i, child)

        for i in range(population.populationSize()):
            self.mutate(population.getTour(i))

        return population

    def crossover(self, parenti, parentii):
        child = Tour(self.tourManager)
        startPos = int(random.random() * parenti.tourSize())
        endPos = int(random.random() * parentii.tourSize())
        # STOP HERE, TO-DO:
        # FINISH CROSSOVER, MUTATION AND TOURNAMENT SELECTION

    def tournamentSelection(self, pop):
        pass
        # WRITE HERE

    def mutate(self, tour):
        pass
        # WRITE CODE