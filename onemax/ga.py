import numpy as np

def fitness(population):
    score = np.sum(population, axis=1)
    return score

def selection(population, scores):
    tournament = np.random.choice(len(population), size=(len(population), 2))

    winner_tournament = np.argmax(scores[tournament], axis=1)
    
    selected = tournament[np.arange(len(population)), winner_tournament]

    return population[selected]


def crossover(parents, rate=0.7):
    half = len(parents) // 2
    parents_a = parents[:half]
    parents_b = parents[half:]

    prob = np.random.rand(half)
    mask_prob = prob <= rate

    cross_point = np.random.randint(low=1, high=parents.shape[1])

    childs_1 = parents_a.copy()
    childs_2 = parents_b.copy()

    childs_1[mask_prob] = np.hstack((parents_a[mask_prob, :cross_point], parents_b[mask_prob, cross_point:]))
    childs_2[mask_prob] = np.hstack((parents_b[mask_prob, :cross_point], parents_a[mask_prob, cross_point:]))

    return np.vstack((childs_1, childs_2))


def mutation(population, rate=0.05):
    prob = np.random.rand(population.shape[0], population.shape[1])

    mask_prob = prob <= rate

    population[mask_prob] = population[mask_prob] ^ 1

    return population

