# -*- coding: utf-8 -*-
"""PSO_funcion5_Getzemani.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QHJW1fJ4L-VhVT5H8dllYPT9BCHwWz-0

Rosenbrock’s Function
"""

import numpy as np
import matplotlib.pyplot as plt

b = 100

def objective_function(vector):
    """Returns value of the modified objective function: f(x, y) = (x - 1)^2 + b * (y - x^2)^2"""
    x, y = vector[0], vector[1]
    return (x - 1)**2 + b * (y - x**2)**2

def random_vector(minmax):
    """Generate a bounded random approximation to the solution."""
    return minmax[:, 0] + (minmax[:, 1] - minmax[:, 0]) * np.random.random(len(minmax))

def create_particle(search_space, vel_space):
    """Create a particle in a random position."""
    particle = {}
    particle['position'] = random_vector(search_space)
    particle['cost'] = objective_function(particle['position'])
    particle['b_position'] = np.copy(particle['position'])
    particle['b_cost'] = particle['cost']
    particle['velocity'] = random_vector(vel_space)
    return particle

def get_global_best(population, current_best=None):
    """Get the best global particle."""
    population.sort(key=lambda p: p['cost'])
    best = population[0]
    if current_best is None or best['cost'] <= current_best['cost']:
        current_best = {}
        current_best['position'] = np.copy(best['position'])
        current_best['cost'] = best['cost']
    return current_best

def update_velocity(particle, gbest, max_v, c1, c2):
    for i, v in enumerate(particle['velocity']):
        v1 = c1 * np.random.random() * (particle['b_position'][i] - particle['position'][i])
        v2 = c2 * np.random.random() * (gbest['position'][i] - particle['position'][i])
        particle['velocity'][i] = v + v1 + v2
        if particle['velocity'][i] > max_v:
            particle['velocity'][i] = max_v
        if particle['velocity'][i] < -max_v:
            particle['velocity'][i] = -max_v

def update_position(particle, bounds):
    """Update the position of a particle."""
    for i, v in enumerate(particle['position']):
        particle['position'][i] = v + particle['velocity'][i]
        if particle['position'][i] > bounds[i][1]:
            particle['position'][i] = bounds[i][1] - abs(particle['position'][i] - bounds[i][1])
            particle['velocity'][i] *= -1.0
        elif particle['position'][i] < bounds[i][0]:
            particle['position'][i] = bounds[i][0] + abs(particle['position'][i] - bounds[i][0])
            particle['velocity'][i] *= -1.0

def update_best_position(particle):
    """Update the best position of a particle."""
    if particle['cost'] <= particle['b_cost']:
        particle['b_cost'] = particle['cost']
        particle['b_position'] = np.copy(particle['position'])

def pso(max_gens, search_space, vel_space, pop_size, max_vel, c1, c2):
    """Implements the Particle Swarm Optimization Algorithm."""
    pop = [create_particle(search_space, vel_space) for _ in range(pop_size)]
    gbest = get_global_best(pop)
    xp, yp = [], []

    for gen in range(max_gens):
        for i, particle in enumerate(pop):
            update_velocity(particle, gbest, max_vel, c1, c2)
            update_position(particle, search_space)
            particle['cost'] = objective_function(particle['position'])
            xp.append(particle['position'][0])
            yp.append(particle['position'][1])
            update_best_position(particle)
            pop[i] = particle
        gbest = get_global_best(pop, gbest)
        print(" > gen=%d, fitness=%g" % (gen + 1, gbest['cost']))

    plt.axis([search_space[0, 0], search_space[0, 1],
              search_space[1, 0], search_space[1, 1]])
    plt.plot(xp, yp, 'ro', [gbest['position'][0]], [gbest['position'][1]], 'bs')

    return gbest

# problem configuration
problem_size = 2  # number of variables
search_space = np.array([[-5, +5] for _ in range(problem_size)], float)  # domains
# algorithm configuration
vel_space = np.array([[-1, +1] for _ in range(problem_size)], float)
max_gens = 100  # maximum number of generations
pop_size = 50  # number of particles
max_vel = 100.0  # maximum velocity
c1, c2 = 2.0, 2.0

# execute the algorithm
best = pso(max_gens, search_space, vel_space, pop_size, max_vel, c1, c2)
print("Done.\nBest Solution: c=%g, v=%s" % (best['cost'], best['position']))
plt.show()