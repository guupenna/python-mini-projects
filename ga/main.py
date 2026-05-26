import numpy as np

GENES = 30
POPULATION = 100
GENERATION = 10000
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.01

LOWER_BOUND = -32
UPPER_BOUND = 32

def fitness(population):
    n = population.shape[1]

    termo1 = -20*np.exp(-0.2*np.sqrt((1/n)*np.sum(population**2, axis=1)))
    termo2 = -np.exp((1/n)*np.sum(np.cos(2*np.pi*population), axis=1))

    return termo1 + termo2 + 20 + np.e


def selection(population, scores):
    tournament = np.random.choice(population.shape[0], size=(population.shape[0], 3))

    winner_tournament = np.argmin(scores[tournament], axis=1)

    selected = tournament[np.arange(population.shape[0]), winner_tournament]

    return population[selected]


def crossover(parents, taxa=CROSSOVER_RATE):
    half = parents.shape[0] // 2
    parents_a = parents[half:]
    parents_b = parents[:half]

    prob = np.random.rand(half)
    mask_prob = prob <= taxa

    childs_1 = parents_a.copy()
    childs_2 = parents_b.copy()

    for i in range(half):
        if mask_prob[i]:
            alpha = np.random.uniform(-0.1, 1.1)

            childs_1[i] = alpha * parents_a[i] + (1 - alpha) * parents_b[i]
            childs_2[i] = alpha * parents_b[i] + (1 - alpha) * parents_a[i]

    return np.vstack((childs_1, childs_2))


def mutation(population, taxa=MUTATION_RATE):
    prob = np.random.rand(population.shape[0], population.shape[1])

    mask_prob = prob <= taxa

    noise = np.random.uniform(-1.0, 1.0, size=population.shape)

    population[mask_prob] += noise[mask_prob] 

    return np.clip(population, LOWER_BOUND, UPPER_BOUND)


if __name__ == "__main__":
    population = np.random.uniform(low=-32, high=32, size=(POPULATION, GENES))

    for gen in range(GENERATION):
        scores = fitness(population)

        index_best = np.argmin(scores)
        score_best = scores[index_best]
        best = population[index_best]

        elite = best.copy()

        print(f"Generation {gen} | Best fitness: {score_best}")

        if score_best < 1e-5:
            print(f"\nOptimal solution encountered in generation {gen}!")
            break

        selected = selection(population, scores)

        childs = crossover(selected)

        population = mutation(childs)

        population[0] = elite

    print("\n====== FINAL ======")
    print(fitness(population))