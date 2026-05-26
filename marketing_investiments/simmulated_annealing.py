import random
import math
from hill_climbing import hill_climbing

def calcula_retorno(sol):
    x1, x2, x3, x4 = sol
    return 50*x1 - 1.2*(x1**2) + 45*x2 - 1.0*(x2**2) + 40*x3 - 0.8*(x3**2) + 55*x4 - 1.5*(x4**2)


def verifica_restricoes(sol):
    x1, x2, x3, x4 = sol

    if min(sol) < 0:
        return False

    inv_total = x1 + x2 + x3 + x4
    inv_linkedin_yt = x3 + x4
    horas = 2*x1 + 1*x2 + 3*x3 + 2*x4

    return inv_total <= 50 and inv_linkedin_yt <= 25 and horas <= 80
    

def vizinho_aleatorio(sol):
    while True:
        nova = list(sol)
        i = random.randint(0, 3)
        delta = random.choice([-1, 1])

        nova[i] += delta

        if verifica_restricoes(nova):
            return tuple(nova)


def simmulated_annealing(T=100.0, T_min=0.1, alpha=0.95):
    sol_atual = (0, 0, 0, 0)
    melhor_sol_global = sol_atual

    while T > T_min:
        vizinho = vizinho_aleatorio(sol_atual)

        delta = calcula_retorno(vizinho) - calcula_retorno(sol_atual)

        if delta > 0:
            sol_atual = vizinho
        else:
            prob = math.exp(delta/T)
            if random.random() < prob:
                sol_atual = vizinho

        if calcula_retorno(sol_atual) > calcula_retorno(melhor_sol_global):
            melhor_sol_global = sol_atual

        T *= alpha

    return melhor_sol_global


if __name__ == "__main__":
    melhor_solucao = simmulated_annealing()
    
    for i in range(100):
        solucao = simmulated_annealing()
        if calcula_retorno(solucao) > calcula_retorno(melhor_solucao):
            melhor_solucao = solucao

    solucao_refinada = hill_climbing(melhor_solucao)

    print("====== SIMMULATED ANNEALING ======\n")
    print(f"Melhor plano de investimento encontrado:")
    print(f"Google Ads: {solucao_refinada[0]}")
    print(f"Instagram Ads: {solucao_refinada[1]}")
    print(f"LinkedIn Ads: {solucao_refinada[2]}")
    print(f"YouTube Ads: {solucao_refinada[3]}")
    print(f"Lucro calculado: {calcula_retorno(solucao_refinada)}")
