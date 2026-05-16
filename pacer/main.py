import numpy as np

def floatToPace(pace_float: float):
    return f"{int(pace_float)}'{int((pace_float % 1) * 60)}\""

treinos = np.array([
    [12, 1.71],
    [14, 2],
    [11, 1.55],
    [9, 1.3],
    [9, 1.32]
])

print("=================================")
print("=========     PACER     =========")
print("=================================\n\n")

distancia_meta = input("Para calcular informações sobre seu treino e sobre sua meta, primeiro informe a distância que pretende percorrer (em km): ")
tempo_meta = input("Agora, sua meta de tempo para essa distância (em minutos): ")
pace_meta =  float(tempo_meta) / float(distancia_meta)

paces = treinos[:, 0]/treinos[:, 1]

print(f"Pace médio: {floatToPace(paces.mean())}")
print(f"Melhor pace: {floatToPace(paces.min())}")
print(f"Pior pace: {floatToPace(paces.max())}")
print(f"Distância total percorrida: {treinos[:, 1].sum()} km")

print(f"\nPara chegar no seu pace alvo de {floatToPace(pace_meta)}, você precisa abaixar seu pace em {floatToPace(paces.mean() - pace_meta)} para {distancia_meta} km.")