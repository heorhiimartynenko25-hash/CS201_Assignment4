import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('random_walk.csv')
#print(df.head())

df["distance"] = (df["x"]**2 + df["y"]**2)
mean = df["distance"].mean()
print(" Максимальна відстань: ", df["distance"].max(), "\n", "Мінімальна відстань: ", df["distance"].min(), "\n", "Середня відстань: ", mean, "." )

df_filter = df[df["distance"] > mean]
print("Відфільтровані за відстанню дані: ")
print(df_filter.to_string(index=False, justify="left"))

df_filter.to_json("filtered_walk.json", indent=4)

plt.figure(figsize=(8, 6))
plt.plot(df["x"], df["y"], color="green", label="Траєкторія")
plt.scatter(df.head(1)['x'], df.head(1)['y'], color="blue", label="Start")
plt.scatter( df.tail(1)['x'], df.tail(1)['y'], color="red", label="End")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate", rotation=0, labelpad=10) #rotation - параметр повороту тексту
plt.title("Графік випадкового блукання")
plt.legend()
plt.minorticks_on()
plt.grid(which='major', color='gray', linewidth=0.8)
plt.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5) #minor - додаткові лінії сітки
plt.show()
