# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:20:11 2024

@author: karla
"""

import matplotlib.pyplot as plt
import math
import numpy as np

# Lista de listas de tuplas
adj = {
    'A': [('B', 3), ('E', 21)],
    'B': [('A', 3),('D', 6),('C', 5)],
    'C': [('B', 5),('D', 5),('E', 7)],
    'D': [('B', 6), ('C', 5), ('E', 4)],
    'E': [('C', 7), ('D', 4), ('A', 21)]
}

def euc_2d(c1, c2):
    """returns the rounded Euclidian distance between two 2D points"""
    for tupla in adj[c1]:
        if(tupla[0]==c2):
            return tupla[1]
    return 1e8
    
def cost(permutation, cities):
    """returns the length of a tour of cities"""
    distance = 0
    ncities = len(cities)
    for i in range(ncities):
        c1 = permutation[i]
        if i+1 == ncities:
            c2 = permutation[0]
        else:
            c2 = permutation[i+1]
        distance += euc_2d(cities[c1], cities[c2])
    return distance

def random_permutation(cities):
    """generate a tour as a random permutation of cities"""
    perm = list(range(len(cities)))
    np.random.shuffle(perm)
    return perm

def initialise_pheromone_matrix(num_cities, naive_score):
    """initialises the pheromone matrix"""
    v = num_cities / naive_score
    return v * np.ones(num_cities*num_cities).reshape((num_cities,num_cities))

def calculate_choices(cities, last_city, exclude, pheromone, c_heur, c_hist):
    """calculate the selection probability for a group of cities"""
    choices = []
    for i,coord in enumerate(cities):
        if i in exclude: continue
        prob = {'city' : i}
        prob['history'] = pheromone[last_city, i] ** c_hist
        prob['distance'] = euc_2d(cities[last_city], coord)
        prob['heuristic'] = (1.0 / prob['distance']) ** c_heur
        prob['prob'] = prob['history'] * prob['heuristic']
        choices.append(prob)
    return choices
        
def select_next_city(choices):
    """selects the next city for a partial tour"""
    psum = 0.0
    for element in choices: psum += element['prob']
    if psum == 0.0:
        return choices[np.random.randint(len(choices))]['city']
    v = np.random.random()
    for i,choice in enumerate(choices):
        v -= choice['prob'] / psum
        if v <= 0.0: return choice['city']
    return choices[-1]['city']

def stepwise_const(cities, phero, c_heur, c_hist):
    """construct a tour for an ant"""
    ncities = len(cities)
    perm = []
    perm.append(np.random.randint(ncities))
    while len(perm) < ncities:
        choices = calculate_choices(cities, perm[-1], perm, phero, c_heur, c_hist)
        next_city = select_next_city(choices)
        perm.append(next_city)
    return perm

def decay_pheromone(pheromone, decay_factor):
    """reduce all the pheromone values"""
    factor = 1.0 - decay_factor
    for i in range(len(pheromone)):
        for j in range(len(pheromone[0])):
            pheromone[i, j] *= factor
    
def update_pheromone(pheromone, solutions):
    """increase the pheromone values in the ants tours"""
    for other in solutions:
        for i,x in enumerate(other['vector']):
            if i == len(other['vector'])-1:
                y = other['vector'][0]
            else:
                y = other['vector'][i+1]
            pheromone[x,y] += 1.0 / other['cost']
            pheromone[y,x] += 1.0 / other['cost']

    
def ant_system(cities, max_it, num_ants, decay_factor, c_heur, c_hist):
    """implements an Ant System"""
    best = {'vector' : random_permutation(cities)}
    best['cost'] = cost(best['vector'], cities)
    pheromone = initialise_pheromone_matrix(len(cities), best['cost'])
    for i in range(max_it):
        solutions = []
        for ant in range(num_ants):
            candidate = {}
            candidate['vector'] = stepwise_const(cities, pheromone, c_heur, c_hist)
            candidate['cost'] = cost(candidate['vector'], cities)
            if candidate['cost'] < best['cost']:
                best = candidate
            solutions.append(candidate)
        decay_pheromone(pheromone, decay_factor)
        update_pheromone(pheromone, solutions)
        print(" > iteration=%d, best=%g" % (i+1,best['cost']))
    return best

# problem configuration
# Taken from TSPLIB with Optimal solution = 7542 units
ciudades = np.array(['A','B','C','D','E'])
# algorithm configuration
max_it = 50 # maximum number of iterations
num_ants = 3  # number of ants
decay_factor = 0.6 # reduction of pheromone
c_heur = 2.5 # heuristic coefficient
c_hist = 1.0 # pheromone coefficient
# execute the algorithm
plt.ion()
fig = plt.figure()
best = ant_system(ciudades, max_it, num_ants, decay_factor, c_heur, c_hist)
print("Done.\nBest Solution: c=%g, v=%s" % (best['cost'], best['vector']))
best = ant_system(ciudades, max_it, num_ants, decay_factor, c_heur, c_hist)
print("Done.\nBest Solution: c=%g, v=%s" % (best['cost'], best['vector']))
#plt.show()


