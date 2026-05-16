import numpy as np

treinos = np.array([
    [40, 4],
    [43, 5],
    [37, 4.5],
    [38, 5],
    [37, 5],
    [29, 4],
    [30, 4.4],
    [29, 4.3],
    [36, 5]
])

paces = treinos[:, 0]/treinos[:, 1]

print(f"Pace médio: {round(paces.mean())}'{int((paces.mean() % 1) * 60)}\"")
print(f"Melhor pace: {round(paces.min())}'{int((paces.min() % 1) * 60)}\"")
print(f"Pior pace: {round(paces.max())}'{int((paces.max() % 1) * 60)}\"")
print(f"Distância total percorrida: {treinos[:, 1].sum()}km")