import numpy as np

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


def hill_climbing():
    sol_atual = (0, 0, 0)

    while(True):
        vizinhos = gera_vizinhos(sol_atual)

        if not vizinhos:
            break

        melhor_vizinho = max(vizinhos, key=calcula_lucro)

        if calcula_lucro(melhor_vizinho) <= calcula_lucro(sol_atual):
            break
        
        sol_atual = melhor_vizinho

    return sol_atual


if __name__ == "__main__":
    solucao = hill_climbing()

    print(f"Melhor plano de produção encontrado:")
    print(f"Unidades do produto A: {solucao[0]}")
    print(f"Unidades do produto B: {solucao[1]}")
    print(f"Unidades do produto C: {solucao[2]}")
    print(f"Lucro calculado: {calcula_lucro(solucao)}")