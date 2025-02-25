import random
import numpy

# Datos del problema de la mochila
valores = [300000, 15000, 600, 600, 9000, 15000]  # Valores de los objetos
volumenes = [50, 1750, 80, 15, 200, 600]  # Volumen de cada objeto en ml
maximos_objetos = [1, 20, 4, 12, 20, 10]
capacidad_maxima = 10000  # Capacidad máxima de la mochila
n_objetos = len(valores)

# Inicialización de un individuo con variables discretas (número de objetos)
def createIndividual():
    return numpy.array([numpy.random.randint(0, maximos_objetos[i] + 1) for i in range(n_objetos)])

# Función de evaluación (fitness) que calcula el valor total y penaliza si excede la capacidad
def evaluate(individual):
    valor_total = numpy.dot(individual, valores)
    volumen_total = numpy.dot(individual, volumenes)
    if volumen_total > capacidad_maxima:
        return -1  # Penalización por exceder la capacidad
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
            individual[i] = numpy.random.randint(0, maximos_objetos[i] + 1)
    return individual

# Función de selección por torneo
def select(population, evaluation, tournamentSize):
    winner = numpy.random.randint(0, len(population))
    for _ in range(tournamentSize - 1):
        rival = numpy.random.randint(0, len(population))
        if evaluation[rival] > evaluation[winner]:
            winner = rival
    return population[winner]

# Algoritmo genético para el problema de la mochila
def geneticAlgorithm(populationSize, cRate, mRate, generations):
    # Crear la población inicial
    population = [createIndividual() for _ in range(populationSize)]
    evaluation = [evaluate(ind) for ind in population]

    # Mantener registro del mejor individuo
    bestIndividual = population[numpy.argmax(evaluation)]
    bestEvaluation = max(evaluation)
    
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
        max_eval_idx = numpy.argmax(evaluation)
        if evaluation[max_eval_idx] > bestEvaluation:
            bestEvaluation = evaluation[max_eval_idx]
            bestIndividual = population[max_eval_idx]
            no_improvement_count = 0  # Reiniciar el contador si hay mejora
        else:
            no_improvement_count += 1
        
        # Verificar si se alcanzó el número máximo de generaciones sin mejora
        if no_improvement_count >= max_no_improvement:
            break
        
        current_generation += 1

    # Volumen de la solución encontrada
    l = numpy.dot(numpy.array(bestIndividual), numpy.array(volumenes))
    
    return bestIndividual, bestEvaluation, l, current_generation

# Resolver el problema de la mochila
solution, evaluation, l, generaciones_finalizadas = geneticAlgorithm(30, 0.7, 0.2, 1000)
print("Mejor solución encontrada:", solution)
print("Valor de la solución:", evaluation)
print("Volumen:", l)
print("Generaciones completadas:", generaciones_finalizadas)
