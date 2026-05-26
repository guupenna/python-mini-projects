import numpy as np
import math

LOWER_BOUND = -32
UPPER_BOUND = 32
DIMENSAO = 30

def f(x):
    n = len(x)

    termo1 = -20*np.exp(-0.2*np.sqrt((1/n)*np.sum(x**2)))
    termo2 = -np.exp((1/n)*np.sum(np.cos(2*np.pi*x)))

    return termo1 + termo2 + 20 + np.e


def gera_vizinhos(x):
    vizinhos = []

    passo = 0.0001

    for i in range(DIMENSAO):
        for delta in [-passo, passo]:
            novo_x = np.copy(x)

            novo_x[i] += delta

            novo_x = np.clip(novo_x, LOWER_BOUND, UPPER_BOUND)

            vizinhos.append(novo_x)

    return vizinhos


def hill_climbing(x):
    sol_atual = x

    while True:
        vizinhos = gera_vizinhos(sol_atual)

        if not vizinhos:
            break

        melhor_vizinho = min(vizinhos, key=f)

        if f(melhor_vizinho) >= f(sol_atual):
            break

        sol_atual = melhor_vizinho

    return sol_atual