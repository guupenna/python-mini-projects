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

population = np.random.randint(low=0, high=2, size=(10, 5))

scores = fitness(population)

print(selection(population, scores))