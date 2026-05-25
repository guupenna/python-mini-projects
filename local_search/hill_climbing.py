import numpy as np
import random

def calcula_lucro(sol):
    A, B, C = sol
    return 30*A + 50*B + 40*C


def verifica_restricoes(sol):
    A, B, C = sol

    if min(sol) < 0:
        return False

    horas = 2*A + 4*B + 3*C
    recursos = 3*A + 2*B + 4*C

    return horas <= 100 and recursos <= 90


def gera_vizinhos(sol):
    vizinhos = []

    for i in range(3):
        for delta in [-1, 1]:
            nova = list(sol)
            nova[i] += delta

            if verifica_restricoes(nova):
                vizinhos.append(nova)
    
    return vizinhos


def vanilla_hill_climbing():
        sol_atual = (0, 0, 0)

        while True:
            vizinhos = gera_vizinhos(sol_atual)

            if not vizinhos:
                break

            melhor_vizinho = max(vizinhos, key=calcula_lucro)

            if calcula_lucro(melhor_vizinho) <= calcula_lucro(sol_atual):
                break
            
            sol_atual = melhor_vizinho

        return sol_atual


def random_restart_hill_climbing():
    melhor_solucao_global = None
    melhor_lucro_global = -1

    for i in range(100):
        # Procura solução inicial aleatória válida
        while True:
            array = np.random.randint(0, 50, size=3)
            sol_atual = (array[0], array[1], array[2])
            if verifica_restricoes(sol_atual):
                break

        # Executa hill climbin com a solução inicial normalmente
        while True:
            vizinhos = gera_vizinhos(sol_atual)

            if not vizinhos:
                break

            melhor_vizinho = max(vizinhos, key=calcula_lucro)

            if calcula_lucro(melhor_vizinho) <= calcula_lucro(sol_atual):
                break

            sol_atual = melhor_vizinho
            
        # Após uma "escalada", ele verifica se é a melhor solução já encontrada
        lucro_atual = calcula_lucro(sol_atual)
        if lucro_atual > melhor_lucro_global:
            melhor_lucro_global = lucro_atual
            melhor_solucao_global = sol_atual

    return melhor_solucao_global


def stochastic_hill_climbing():
    sol_atual = (0, 0, 0)

    while True:
        vizinhos = gera_vizinhos(sol_atual)

        if not vizinhos:
            break

        melhores_vizinhos = [v for v in vizinhos if calcula_lucro(v) > calcula_lucro(sol_atual)]

        if not melhores_vizinhos:
            break

        sol_atual = random.choice(melhores_vizinhos)

    return sol_atual


if __name__ == "__main__":
    # solucao = vanilla_hill_climbing()

    # print("====== VANILLA HILL CLIMBING ======\n")
    # print(f"Melhor plano de produção encontrado:")
    # print(f"Unidades do produto A: {solucao[0]}")
    # print(f"Unidades do produto B: {solucao[1]}")
    # print(f"Unidades do produto C: {solucao[2]}")
    # print(f"Lucro calculado: {calcula_lucro(solucao)}")

    solucao_rr = random_restart_hill_climbing()

    print("\n====== RANDOM RESTART HILL CLIMBING ======\n")
    print(f"Melhor plano de produção encontrado:")
    print(f"Unidades do produto A: {solucao_rr[0]}")
    print(f"Unidades do produto B: {solucao_rr[1]}")
    print(f"Unidades do produto C: {solucao_rr[2]}")
    print(f"Lucro calculado: {calcula_lucro(solucao_rr)}")

    solucao_stochastic = stochastic_hill_climbing()

    print("\n====== STOCHASTIC HILL CLIMBING ======\n")
    print(f"Melhor plano de produção encontrado:")
    print(f"Unidades do produto A: {solucao_stochastic[0]}")
    print(f"Unidades do produto B: {solucao_stochastic[1]}")
    print(f"Unidades do produto C: {solucao_stochastic[2]}")
    print(f"Lucro calculado: {calcula_lucro(solucao_stochastic)}")
