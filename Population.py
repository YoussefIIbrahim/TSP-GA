from Tour import Tour


class Population:
    def __init__(self, tourManager, populationSize, initialise):
        self.tours = []
        for i in range(0, populationSize):
            self.tours.append(None)

        if initialise:
            for i in range(populationSize):
                newTour = Tour(tourManager)
                newTour.generateIndividual()
                self.saveTour(i, newTour)

    def saveTour(self, index, tour):
        self.tours[index] = tour


