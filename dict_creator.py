import pandas as pd

df = pd.read_csv("main.csv")
final_list = []

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
distance = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

temp_list = {}

for i in range(0, len(name)):
    temp_list["name"] = name[i]
    temp_list["mass"] = mass[i]
    temp_list["radius"] = radius[i]
    temp_list["distance"] = distance[i]
    temp_list["gravity"] = gravity[i]

    final_list.append(temp_list)
    
    temp_list = {}

print(final_list)