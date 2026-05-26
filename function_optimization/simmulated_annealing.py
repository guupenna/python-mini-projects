import random
import math
import numpy as np

LOWER_BOUND = -1
UPPER_BOUND = 2

def f(x):
    return x * np.sin(10*np.pi*x) + 1


def vizinho_aleatorio(x):
    passo = random.uniform(-0.1, 0.1)

    novo_x = x + passo

    novo_x = max(LOWER_BOUND, min(UPPER_BOUND, novo_x))
    return novo_x


def simmulated_annealing(T=100.0, T_min=0.1, alpha=0.95):
    sol_atual = random.uniform(LOWER_BOUND, UPPER_BOUND)
    melhor_sol_global = sol_atual

    while T > T_min:

        for _ in range(50):
            vizinho = vizinho_aleatorio(sol_atual)

            delta = f(vizinho) - f(sol_atual)

            if delta > 0:
                sol_atual = vizinho
            else:
                prob = math.exp(delta/T)
                if random.random() < prob:
                    sol_atual = vizinho

            if f(sol_atual) > f(melhor_sol_global):
                melhor_sol_global = sol_atual

        T *= alpha

    return melhor_sol_global


if __name__ == "__main__":
    solucao = simmulated_annealing()

    print("====== SIMMULATED ANNEALING ======\n")
    print(f"Melhor valor para x encontrado: {solucao}")
    print(f"f(x) = {f(solucao)}")