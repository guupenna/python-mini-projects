import numpy as np

GENES = 30
POPULATION = 100
GENERATION = 2000
CROSSOVER_RATE = 0.7
MUTATION_FACTOR = 0.5

LOWER_BOUND = -32
UPPER_BOUND = 32

def fitness(populacao):
    n = populacao.shape[1]

    termo1 = -20*np.exp(-0.2*np.sqrt((1/n)*np.sum(populacao**2, axis=1)))
    termo2 = -np.exp((1/n)*np.sum(np.cos(2*np.pi*populacao), axis=1))

    return termo1 + termo2 + 20 + np.e


def mutacao(populacao, F=MUTATION_FACTOR):
    mutantes = np.zeros_like(populacao)

    for i in range(populacao.shape[0]):
        indices = list(range(populacao.shape[0]))

        indices.remove(i)

        r1, r2, r3 = np.random.choice(indices, size=3, replace=False)

        mutantes[i] = populacao[r1] + F * (populacao[r2] - populacao[r3])

    return np.clip(mutantes, LOWER_BOUND, UPPER_BOUND)


def crossover(populacao, mutacoes, taxa=CROSSOVER_RATE):
    prob = np.random.rand(populacao.shape[0], populacao.shape[1])
    mask_prob = prob <= taxa

    filhos = populacao.copy()

    filhos[mask_prob] = mutacoes[mask_prob]

    return filhos


def selecao(populacao, filhos, notas_populacao, notas_filhos):
    mascara_vencedores = notas_filhos < notas_populacao

    mascara_reshape = mascara_vencedores.reshape(-1, 1)

    vencedores = np.where(mascara_reshape, filhos, populacao)

    return vencedores


if __name__ == "__main__":
    populacao = np.random.uniform(LOWER_BOUND, UPPER_BOUND, size=(POPULATION, GENES))

    for gen in range(GENERATION):
        notas = fitness(populacao)
        
        indice_melhor = np.argmin(notas)
        melhor_nota = notas[indice_melhor]
        print(f"Geração {gen} | Melhor nota: {melhor_nota:.6f}")
        
        if melhor_nota < 1e-5:
            print("Zero encontrado!")
            break

        mutantes = mutacao(populacao)
        
        filhos = crossover(populacao, mutantes)
        
        notas_filhos = fitness(filhos)
        
        populacao = selecao(populacao, filhos, notas, notas_filhos)

    print("\n--- FIM ---")
    print(f"Melhor resultado final: {np.min(fitness(populacao))}")