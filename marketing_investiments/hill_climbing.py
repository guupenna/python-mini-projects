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
    

def gera_vizinhos(sol):
    vizinhos = []

    for i in range(4):
        for delta in [-1, 1]:
            nova = list(sol)
            nova[i] += delta

            if verifica_restricoes(nova):
                vizinhos.append(nova)

    return vizinhos


def hill_climbing(sol):
    sol_atual = sol

    while True:
        vizinhos = gera_vizinhos(sol_atual)

        if not vizinhos:
            break

        melhor_vizinho = max(vizinhos, key=calcula_retorno)

        if calcula_retorno(melhor_vizinho) <= calcula_retorno(sol_atual):
            break

        sol_atual = melhor_vizinho

    return sol_atual


if __name__ == "__main__":
    solucao = hill_climbing()

    print("====== HILL CLIMBING ======\n")
    print(f"Melhor plano de investimento encontrado:")
    print(f"Google Ads: {solucao[0]}")
    print(f"Instagram Ads: {solucao[1]}")
    print(f"LinkedIn Ads: {solucao[2]}")
    print(f"YouTube Ads: {solucao[3]}")
    print(f"Lucro calculado: {calcula_retorno(solucao)}")
