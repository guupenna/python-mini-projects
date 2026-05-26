import numpy as np

DIMENSOES = 30
POPULACAO = 100
GERACOES = 10000
COEF_INERCIA = 0.7
COMP_COGNITIVA = 2.0
COMP_SOCIAL = 2.0

LOWER_BOUND = -32
UPPER_BOUND = 32


def fitness(populacao):
    n = populacao.shape[1]

    termo1 = -20*np.exp(-0.2*np.sqrt((1/n)*np.sum(populacao**2, axis=1)))
    termo2 = -np.exp((1/n)*np.sum(np.cos(2*np.pi*populacao), axis=1))

    return termo1 + termo2 + 20 + np.e


if __name__ == "__main__":
    posicao = np.random.uniform(LOWER_BOUND, UPPER_BOUND, size=(POPULACAO, DIMENSOES))
    velocidade = np.zeros([POPULACAO, DIMENSOES])

    pbest = posicao.copy()
    notas_pbest = fitness(pbest)

    indice_lider = np.argmin(notas_pbest)
    gbest = pbest[indice_lider].copy()
    nota_gbest = notas_pbest[indice_lider]

    for gen in range(GERACOES):
        r1 = np.random.rand(POPULACAO, DIMENSOES)
        r2 = np.random.rand(POPULACAO, DIMENSOES)

        velocidade = (COEF_INERCIA*velocidade) + (COMP_COGNITIVA*r1*(pbest - posicao)) + (COMP_SOCIAL*r2*(gbest - posicao))

        posicao = posicao + velocidade

        posicao = np.clip(posicao, LOWER_BOUND, UPPER_BOUND)

        notas_atuais = fitness(posicao)

        mascara_melhorou = notas_atuais < notas_pbest
        notas_pbest = np.where(mascara_melhorou, notas_atuais, notas_pbest)
        mascara_reshape = mascara_melhorou.reshape(-1, 1)
        pbest = np.where(mascara_reshape, posicao, pbest)

        indice_melhor_nota = np.argmin(notas_pbest)
        if notas_pbest[indice_melhor_nota] < nota_gbest:
            nota_gbest = notas_pbest[indice_melhor_nota]
            gbest = pbest[indice_melhor_nota].copy()

        print(f"Geração {gen+1} | Melhor nota global: {nota_gbest:.6f}")
        
        if nota_gbest < 1e-5:
            print("Zero encontrado pelo enxame!")
            break

    print("\n====== FIM ======")
    print(f"Melhor resultado final: {nota_gbest}")

    