import numpy as np
import math
from hill_climbing import hill_climbing

LOWER_BOUND = -32
UPPER_BOUND = 32
DIMENSAO = 30

def f(x):
    n = len(x)

    termo1 = -20*np.exp(-0.2*np.sqrt((1/n)*np.sum(x**2)))
    termo2 = -np.exp((1/n)*np.sum(np.cos(2*np.pi*x)))

    return termo1 + termo2 + 20 + np.e


def vizinho_aleatorio(x, T_atual, T_inicial=5.0):
    raio_passo = 16.0 * (T_atual/T_inicial)
    raio_passo = max(0.01, raio_passo)

    passos = np.random.uniform(-raio_passo, raio_passo, size=DIMENSAO)

    novo_x = x + passos

    return np.clip(novo_x, LOWER_BOUND, UPPER_BOUND)


def simmulated_annealing(T=5.0, T_min=0.1, alpha=0.99):
    sol_atual = np.random.uniform(LOWER_BOUND, UPPER_BOUND, size=DIMENSAO)
    melhor_sol_global = sol_atual

    while T > T_min:
        for _ in range(1000):
            vizinho = vizinho_aleatorio(sol_atual, T)

            delta = f(sol_atual) - f(vizinho)

            if delta > 0:
                sol_atual = vizinho
            else:
                prob = math.exp(delta/T)
                if np.random.random() < prob:
                    sol_atual = vizinho

            if f(sol_atual) < f(melhor_sol_global):
                melhor_sol_global = sol_atual

        T *= alpha
        # print(f"Temp: {T:.2f} | Melhor Global: {f(melhor_sol_global):.4f} | Solução Atual: {f(sol_atual):.4f}")

    return melhor_sol_global


if __name__ == "__main__":
    melhor_solucao = simmulated_annealing()

    for _ in range(10):
        solucao = simmulated_annealing()
        if f(solucao) < f(melhor_solucao):
            melhor_solucao = solucao

    solucao_refinada = hill_climbing(melhor_solucao)

    print("====== SIMMULATED ANNEALING ======\n")
    print(f"Melhor f(x) = {f(solucao_refinada):.4f}")