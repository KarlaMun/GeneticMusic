import random
import numpy
import math
import matplotlib.pyplot as plt

# Inicialización de un individuo con variables discretas (número de objetos)
def createIndividual():
    return numpy.array([numpy.random.uniform(-1, 1), numpy.random.uniform(-1, 1)])

# Función de evaluación (fitness) que calcula el valor total y penaliza si excede la capacidad
def evaluate(individual):
    b = 10
    x = individual[0]
    y = individual[1]
    valor_total = (x ** 2 + y ** 2)/4000.0 - math.cos(x) * math.cos(y / math.sqrt(2)) + 1.0
    return valor_total

# Función de cruce (one point crossover) para individuos con cantidades de objetos
def combine(parentA, parentB, cRate):
    if random.random() <= cRate:
        cPoint = numpy.random.randint(1, len(parentA))
        offspringA = numpy.append(parentA[:cPoint], parentB[cPoint:])
        offspringB = numpy.append(parentB[:cPoint], parentA[cPoint:])
    else:
        offspringA = numpy.copy(parentA)
        offspringB = numpy.copy(parentB)
    return offspringA, offspringB

# Función de mutación que cambia aleatoriamente la cantidad de un objeto
def mutate(individual, mRate):
    for i in range(len(individual)):
        if random.random() <= mRate:
            # La cantidad de mutación está limitada por el máximo disponible para ese objeto
            individual[i] = numpy.random.uniform(-1, 1)
    return individual

# Función de selección por torneo
def select(population, evaluation, tournamentSize):
    winner = numpy.random.randint(0, len(population))
    for _ in range(tournamentSize - 1):
        rival = numpy.random.randint(0, len(population))
        if evaluation[rival] < evaluation[winner]:
            winner = rival
    return population[winner]

# Algoritmo genético para el problema de la mochila
def geneticAlgorithm(populationSize, cRate, mRate, generations):
    # Crear la población inicial
    population = [createIndividual() for _ in range(populationSize)]
    evaluation = [evaluate(ind) for ind in population]

    # Mantener registro del mejor individuo
    bestIndividual = population[numpy.argmin(evaluation)]
    bestEvaluation = min(evaluation)
    
    # Variables para la parada temprana
    no_improvement_count = 0
    max_no_improvement = 25  # Número máximo de generaciones sin mejora
    current_generation = 0
    
    # Proceso evolutivo
    while current_generation < generations:
        newPopulation = []
        for _ in range(populationSize // 2):
            parentA = select(population, evaluation, 3)
            parentB = select(population, evaluation, 3)
            offspringA, offspringB = combine(parentA, parentB, cRate)
            newPopulation.append(offspringA)
            newPopulation.append(offspringB)
        
        population = [mutate(ind, mRate) for ind in newPopulation]
        evaluation = [evaluate(ind) for ind in population]
        
        # Actualizar el mejor individuo encontrado
        min_eval_idx = numpy.argmin(evaluation)
        if evaluation[min_eval_idx] < bestEvaluation:
            bestEvaluation = evaluation[min_eval_idx]
            bestIndividual = population[min_eval_idx]
            no_improvement_count = 0  # Reiniciar el contador si hay mejora
        else:
            no_improvement_count += 1
        
        # Verificar si se alcanzó el número máximo de generaciones sin mejora
        if no_improvement_count >= max_no_improvement:
            break
        
        current_generation += 1

    return bestIndividual, bestEvaluation, current_generation


# Resolver el problema una vez
solution, evaluation, generaciones_finalizadas = geneticAlgorithm(30, 0.7, 0.2, 1000)
print("Mejor solución encontrada:", solution)
print("Valor de la solución:", evaluation)
print("Generaciones completadas:", generaciones_finalizadas)


# Resolver el problema array
scores = []
for i in range(30):
    solution, evaluation, generaciones_finalizadas = geneticAlgorithm(30, 0.7, 0.2, 1000)
    scores.append(evaluation)
print("Promedio valor minimo: ", numpy.mean(scores))
print("Desviacion estandar: ", numpy.std(scores))
plt.hist(scores)
plt.show()
