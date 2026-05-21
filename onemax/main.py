import numpy as np

from ga import *

GENES = 30
POPULATION = 100
GENERATIONS = 200
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.05

def main():
    population = np.random.randint(low=0, high=2, size=(POPULATION, GENES))

    for gen in range(GENERATIONS):
        scores = fitness(population)

        index_best = np.argmax(scores)
        score_best = scores[index_best]
        best = population[index_best]

        print(f"Generation {gen} | Best fitness: {round((score_best/GENES)*100, 2)}% | Genes: {best}")

        if score_best == GENES:
            print(f"\nOptimal solution encountered in generation {gen}!")
            break

        selected = selection(population, scores)

        childs = crossover(selected, CROSSOVER_RATE)

        population = mutation(childs, MUTATION_RATE)

    print("\n=== FINAL POPULATION ===")
    print(population)


if __name__ == "__main__":
    main()