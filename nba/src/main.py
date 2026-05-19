import pandas as pd
import numpy as np

players = pd.read_csv("../nba.csv").dropna(subset=["Age", "Salary"]).to_numpy()

ages = players[:, 4]
salaries = players[:, 8]

mask = (ages > 32) & (salaries > 15000000)

print(players[mask])