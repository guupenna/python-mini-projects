import numpy as np

def fitness(population):
    score = np.sum(population, axis=1)
    return score

def selection(population, scores):
    tournament = np.random.choice(len(population), size=(len(population), 2))

    winner_tournament = np.argmax(scores[tournament], axis=1)
    
    selected = tournament[np.arange(len(population)), winner_tournament]

#    selected = []
#    for i in range(0, len(population)):
#        tournament = np.random.choice(len(population), size=2, replace=False)
#        if (scores[tournament[0]] > scores[tournament[1]]):
#            selected.append(tournament[0])
#        else:
#            selected.append(tournament[1])

    return population[selected]


def crossover(parents, rate=0.7):
    half = len(parents) // 2
    parents_a = parents[:half]
    parents_b = parents[half:]

    prob = np.random.rand(half)
    mask_prob = prob <= rate

    cross_point = np.random.randint(low=1, high=4)

    childs_1 = parents_a.copy()
    childs_2 = parents_b.copy()

    childs_1[mask_prob] = np.hstack((parents_a[mask_prob, :cross_point], parents_b[mask_prob, cross_point:]))
    childs_2[mask_prob] = np.hstack((parents_b[mask_prob, :cross_point], parents_a[mask_prob, cross_point:]))

    return np.vstack((childs_1, childs_2))

#    childs_1 = []
#    for i in range(0, half):
#        childs_1.append(np.concatenate((parents_a[i][:cross_point], parents_b[i][cross_point:])))   
#    childs_2 = []
#    for i in range(0, half):
#        childs_2.append(np.concatenate((parents_b[i][:cross_point], parents_a[i][cross_point:])))

def mutation(population, rate=0.05):
    prob = np.random.rand(population.shape[0], population.shape[1])

    mask_prob = prob <= rate

    population[mask_prob] = population[mask_prob] ^ 1

    return population


GENES = 5
POPULATION = 10
GENERATIONS = 50

population = np.random.randint(low=0, high=2, size=(POPULATION, GENES))

for gen in range(GENERATIONS):
    scores = fitness(population)

    index_best = np.argmax(scores)
    score_best = scores[index_best]
    best = population[index_best]

    print(f"Generation {gen} | Best fitness: {(score_best/GENES)*100}% | Genes: {best}")

    # if score_best == GENES:
    #     print(f"Optimal solution encountered in generation {gen}!")
    #     break

    selected = selection(population, scores)

    childs = crossover(selected)

    population = mutation(childs)

print("\n=== FINAL POPULATION ===")
print(population)