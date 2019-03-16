import random
from City import City
from GeneticAlgorithm import GeneticAlgorithm
from Population import Population
from TourManager import TourManager


def generateRandom():
    return int(random.random()*500)


if __name__ == '__main__':

    tourmanager = TourManager()

    # Create and add our cities
    for i in range(30):
        city = City(generateRandom(), generateRandom())
        tourmanager.addCity(city)

    # Initialize population
    pop = Population(tourmanager, 50, True)
    print("Initial distance: " + str(pop.getFittest().getDistance()))

    # Evolve population for 50 generations
    ga = GeneticAlgorithm(tourmanager)
    pop = ga.evolvePopulation(pop)
    for i in range(0, 100):
        pop = ga.evolvePopulation(pop)

    # Print final results
    print("Finished")
    print("Final distance: " + str(pop.getFittest().getDistance()))
    print("Solution:")
    print(pop.getFittest())