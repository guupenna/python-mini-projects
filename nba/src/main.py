import pandas as pd
import numpy as np

def calcule_mean_salary(players_position):
    return round(players_position[:, 8].mean(), 2)

players = pd.read_csv("../nba.csv").dropna(subset=["Salary"]).to_numpy()

positions = players[:, 3]

print(f"NBA average salary by position (in $):")
for p in np.unique(positions):
    print(f"{p}: ${calcule_mean_salary(players[positions == p]):,}")