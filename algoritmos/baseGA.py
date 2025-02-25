import random
import numpy

# Implements the random initialization of individuals using the binary representation.
def createIndividual(nbBits):
  return numpy.random.randint(2, size = nbBits)

# Implements the one point crossover on individuals using the binary representation.
def combine(parentA, parentB, cRate):
  if (random.random() <= cRate):
    cPoint = numpy.random.randint(1, len(parentA))   
    offspringA = numpy.append(parentA[0:cPoint], parentB[cPoint:])
    offspringB = numpy.append(parentB[0:cPoint], parentA[cPoint:])
  else:
    offspringA = numpy.copy(parentA)
    offspringB = numpy.copy(parentB)
  return offspringA, offspringB

# Implements the flip mutation on individuals using the binary representation.
def mutate(individual, mRate):
  for i in range(len(individual)):
    if (random.random() <= mRate):
      if (individual[i] == 0):
        individual[i] = 1        
      else:
        individual[i] = 0        
  return individual

# Implements the fitness function of individuals using the binary representation and solving the max-one problem.
def evaluate(individual):
  return sum(individual)

# Implements the tournament selection.
def select(population, evaluation, tournamentSize):
  winner = numpy.random.randint(0, len(population))
  for i in range(tournamentSize - 1):
    rival = numpy.random.randint(0, len(population))
    if (evaluation[rival] > evaluation[winner]):
      winner = rival
  return population[winner]

# Implements a genetic algorithm for solving the max-one problem with individuals using the binary representation.
def geneticAlgorithm(n, populationSize, cRate, mRate, generations):
  # Creates the initial population (it also evaluates it)
  population = [None] * populationSize
  evaluation = [None] * populationSize  
  for i in range(populationSize):
    individual = createIndividual(n)
    population[i] = individual
    evaluation[i] = evaluate(individual)
  # Keeps a record of the best individual found so far
  index = 0;
  for i in range(1, populationSize):
    if (evaluation[i] < evaluation[index]):
      index = i;
  bestIndividual = population[index]
  bestEvaluation = evaluation[index]
  # Runs the evolutionary process    
  for i in range(generations):
    k = 0
    newPopulation = [None] * populationSize    
    for j in range(populationSize // 2):
      parentA = select(population, evaluation, 3)
      parentB = select(population, evaluation, 3)
      newPopulation[k], newPopulation[k + 1] = combine(parentA, parentB, cRate)       
      k = k + 2    
    population = newPopulation
    for j in range(populationSize):
      population[j] = mutate(population[j], mRate)
      evaluation[j] = evaluate(population[j])
      # Keeps a record of the best individual found so far
      if (evaluation[j] > bestEvaluation):
        bestEvaluation = evaluation[j]
        bestIndividual = population[j]
  return bestIndividual, bestEvaluation

# solves the problem using the genetic algorithm
solution, evaluation = geneticAlgorithm(100, 20, 0.9, 0.01, 100)
print(solution)
print(evaluation)
