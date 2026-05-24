import numpy as np
import heapq

def heuristica(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def imprimir_mapa(matriz, caminho):
    print("\n  === ROTA ENCONTRADA === \n")
    
    for i in range(matriz.shape[0]):
        linha_terminal = ""
        for j in range(matriz.shape[1]):
            coord = (i, j)
            valor = str(matriz[coord])
            
            if len(valor) == 1:
                valor = " " + valor
                
            if coord in caminho:
                linha_terminal += f"\033[42m\033[97m {valor} \033[0m "
            elif valor.strip() == '*':
                linha_terminal += f"\033[100m\033[97m {valor} \033[0m "
            else:
                linha_terminal += f" {valor}  "
                
        print(linha_terminal)
        print()
        
    print("==================================\n")


matriz = np.array([
    ['I', 2, 1, 1, 1, 2],
    [1, '*', 2, '*', 3, 1],
    [1, 4, 15, '*', '*', 1],
    [2, '*', 15, '*', 4, 1],
    ['*', '*', 2, 2, 9, 2],
    ['*', '*', '*', '*', 'F', 1]
])

inicio = int(np.where(matriz == 'I')[0][0]), int(np.where(matriz == 'I')[1][0]) 
fim = int(np.where(matriz == 'F')[0][0]), int(np.where(matriz == 'F')[1][0]) 

fila = []

g_inicial = 0
f_inicial = g_inicial + heuristica(inicio, fim)

heapq.heappush(fila, (f_inicial, g_inicial, inicio, [inicio]))

custos_conhecidos = {inicio: 0}

while len(fila) > 0:
    f_n, g_n, n, caminho = heapq.heappop(fila)
    
    if n == fim:
        print(f"Fim encontrado! Custo: {g_n}")
        print(f"Caminho: {caminho}")
        imprimir_mapa(matriz, caminho)
        break

    movimentos = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for mov in movimentos:
        vizinho = (n[0] + mov[0], n[1] + mov[1])

        if 0 <= vizinho[0] < 6 and 0 <= vizinho[1] < 6:

            if matriz[vizinho] != '*':
                if matriz[vizinho] == 'F' or matriz[vizinho] == 'I':
                    custo_it = 0
                else:
                    custo_it = int(matriz[vizinho])

                novo_g = g_n + custo_it

                if vizinho not in custos_conhecidos or novo_g < custos_conhecidos[vizinho]:
                    custos_conhecidos[vizinho] = novo_g
                    heapq.heappush(fila, (novo_g + heuristica(vizinho, fim), novo_g, vizinho, caminho + [vizinho]))