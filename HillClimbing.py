from random import *
import numpy

countCities = 20;
# 2D Array
cities = numpy.zeros(shape=(20,20))
# endgueltige Sortierung der Staedte
tour = [int]*countCities
# zum Testen der Sortierung
hypothesis = [int]*countCities
visitedCities = []

threshold = 19
lastFitness = 0
trials = 0
cityIndex = 1

# vergleicht die Distanzen von tour und hypothesis; beide sind bis auf die letzte Stadt identisch sortiert;
# die letzte Stadt in hypothesis ist zufaellig gewaehlt; geringere Distanz = bessere Fitness
def getFitness(cityIndex, tour, hypothesis, cities):

    fitness = cityIndex-1
    print()
    print("Alt")
    currentOrder = getDistance(cities, tour, cityIndex)
    print()
    print("Aktuell")
    possibleOrder = getDistance(cities, hypothesis, cityIndex)
    print()

    if(currentOrder > 0 and possibleOrder > 0):
        if (currentOrder < possibleOrder):
            fitness -= 1
        elif(currentOrder != possibleOrder):
            fitness += 1

    return fitness

# waehle zufaellige Stadt von Position cityIndex (in hypothesis)
def doRandomStep():
    global hypothesis
    randomStep = randint(1,countCities-1)
    hypothesis[cityIndex] = randomStep

# uebertrage die Aenderung auf die Liste mit der endgueltigen Sortierung der Staedte
def changeItemPos(item, newItemPos):
    global tour
    global visitedCities
    visitedCities.append(item)
    tour.remove(item)
    tour.insert(newItemPos,item)
    for i in range(len(tour)):
        print("[",tour[i],"] ",end="")

# gehe zur naechsten Stadt
def increment():
    global lastFitness
    global cityIndex
    global visitedCities
    if (cityIndex < countCities - 2):
        cityIndex += 1
    else:
        visitedCities.clear()
        cityIndex = 1
        lastFitness = 0

# berechne Distanz von der ersten Stadt bis zur Stadt an der Stelle cityIndex (z.B. A -> B -> C, also von A -> C)
def getDistance(cities, tour, cityIndex):
    distance = 0
    for i in range(cityIndex+1):
        if (i < cityIndex):
            distance += cities[tour[i]][tour[i+1]]
            print("[",tour[i],"]",distance,"km ",end="")
        else:
            print("[",tour[i],"]",end="")

    return distance

if __name__ == '__main__':

    for i in range(countCities):

        tour[i] = i
        hypothesis[i] = i

        for j in range(countCities):
            if (j > i):
                cities[i][j] = randint(1,100)
            elif(j < i):
                cities[i][j] = cities[j][i]

    print("=== START ===");
    while(lastFitness < threshold):

        doRandomStep()
        currentFitness = getFitness(cityIndex, tour, hypothesis, cities)

        print("Aktuelle Fitness ",currentFitness)
        print("Alte Fitness ",lastFitness)

        if (currentFitness > lastFitness and (hypothesis[cityIndex] not in visitedCities)):
            versuche = 0
            lastFitness = currentFitness
            changeItemPos(hypothesis[cityIndex], cityIndex)
            increment()
        elif(trials < 5):
            trials += 1
        else:
            hypothesis[cityIndex] = tour[cityIndex]
            visitedCities.append(tour[cityIndex])
            lastFitness += 1
            trials = 0
            increment()


