import pandas as pd
import numpy as np

df = pd.read_csv('random_walk.csv')
#print(df.head())

df["distance"] = (df["x"]**2 + df["y"]**2)
print(" Максимальна відстань: ", df["distance"].max(), "\n", "Мінімальна відстань: ", df["distance"].min(), "\n", "Середня відстань: ", df["distance"].mean(), "." )
