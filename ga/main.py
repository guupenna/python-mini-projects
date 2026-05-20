import numpy as np
import random

def fitness(population):
    score = np.sum(population, axis=1)
    return score

def selection(population):
    return random.choices(population, k=2)

population = np.random.randint(low=0, high=2, size=(10, 5))

score = fitness(population)

# print(population)