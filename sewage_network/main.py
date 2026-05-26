import numpy as np

GENES = 10
POPULATION = 100
GENERATION = 200
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.3

COEF_MANNING = 0.013
DECLIVIDADE = 0.005

vazoes = np.array([2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0])
comprimentos = np.array([20, 54, 98, 120, 34, 12, 88, 122, 33, 40])

diametros = np.array([150, 200, 250, 300, 400])
custos = np.array([65.0, 98.0, 150.0, 210.0, 340.0])


def fitness(populacao):
    custo = np.sum(custos[populacao] * comprimentos, axis=1)

    diametro = diametros[populacao]/1000
    area = (np.pi*diametro**2)/4
    rh = diametro/4

    q_max = (1/COEF_MANNING) * area * rh**(2/3) * DECLIVIDADE**(1/2)

    mascara_punicao = np.any(vazoes/1000 > 0.75*q_max, axis=1)

    custo[mascara_punicao] += 1000000

    return custo


def selecao(populacao, notas):
    torneio = np.random.choice(len(populacao), size=(len(populacao), 2))

    vencedor_torneio = np.argmin(notas[torneio], axis=1)

    selecionados = torneio[np.arange(len(populacao)),vencedor_torneio]

    return populacao[selecionados]


def crossover(pais, taxa=CROSSOVER_RATE):
    metade = len(pais) // 2
    pais_a = pais[:metade]
    pais_b = pais[metade:]

    prob = np.random.rand(metade)
    mask_prob = prob <= taxa

    ponto_cross = np.random.randint(low=1, high=pais.shape[1])

    filhos_1 = pais_a.copy()
    filhos_2 = pais_b.copy()

    filhos_1[mask_prob] = np.hstack((pais_a[mask_prob, :ponto_cross], pais_b[mask_prob, ponto_cross:]))
    filhos_2[mask_prob] = np.hstack((pais_b[mask_prob, :ponto_cross], pais_a[mask_prob, ponto_cross:]))

    return np.vstack((filhos_1, filhos_2))


def mutacao(populacao, taxa=MUTATION_RATE):
    prob = np.random.rand(populacao.shape[0], populacao.shape[1])

    mask_prob = prob <= taxa

    populacao[mask_prob] = np.random.randint(low=0, high=5, size=np.sum(mask_prob))

    return populacao


if __name__ == "__main__":
    populacao = np.random.randint(low=0, high=5, size=(POPULATION, GENES))

    for gen in range(GENERATION):
        notas = fitness(populacao)

        indice_melhor = np.argmin(notas)
        nota_melhor = notas[indice_melhor]
        melhor = populacao[indice_melhor]

        elite = melhor.copy()

        print(f"Geração {gen} | Melhor fitness: {nota_melhor} | Genes: {melhor}")

        selecionados = selecao(populacao, notas)

        filhos = crossover(selecionados, CROSSOVER_RATE)

        populacao = mutacao(filhos, MUTATION_RATE)

        populacao[0] = elite

    print("\n=== MELHOR PROJETO ENCONTRADO ===")
    print(f"Índices dos tubos escolhidos: {melhor}")
    print(f"Custo total da obra: R$ {nota_melhor:.2f}")
