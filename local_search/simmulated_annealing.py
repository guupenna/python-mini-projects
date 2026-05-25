import math
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


def vizinho_aleatorio(sol):
    while True:
        nova = list(sol)
        i = random.randint(0, 2)
        delta = random.choice([-1, 1])

        nova[i] += delta

        if verifica_restricoes(nova):
            return tuple(nova)    


def simmulated_annealing(T=100.0, T_min=0.1, alpha=0.95):
        sol_atual = (0, 0, 0)
        melhor_sol_global = sol_atual

        while T > T_min:
            vizinho = vizinho_aleatorio(sol_atual)

            delta = calcula_lucro(vizinho) - calcula_lucro(sol_atual)
            
            if delta > 0:
                sol_atual = vizinho
            else:
                prob = math.exp(delta/T)
                if random.random() < prob:
                    sol_atual = vizinho

            if calcula_lucro(sol_atual) > calcula_lucro(melhor_sol_global):
                melhor_sol_global = sol_atual

            T *= alpha

        return melhor_sol_global


if __name__ == "__main__":
    solucao = simmulated_annealing()

    print("====== SIMMULATED ANNEALING ======\n")
    print(f"Melhor plano de produção encontrado:")
    print(f"Unidades do produto A: {solucao[0]}")
    print(f"Unidades do produto B: {solucao[1]}")
    print(f"Unidades do produto C: {solucao[2]}")
    print(f"Lucro calculado: {calcula_lucro(solucao)}")