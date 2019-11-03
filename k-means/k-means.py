
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sb
import csv

# Open .txt with the data
file = open('../Instrucoes/datasets/c2ds1-2sp.txt', 'r')

# Split file data into lines
lines = file.read().split('\n')

# Generate array of points
points = []
for i in range(1, len(lines)):
    points.append([lines[i].split()[0], lines[i].split()[1], lines[i].split()[2]])

# Plot graph
df = pd.DataFrame(points, columns = ['sample_label', 'd1', 'd2'], dtype = float)
sb.pairplot(df)
pl.show()

print(lines[1].split())

# k = int(input("Número de clusters: "))

# for i in range(1, len(lines)):
#     print(lines[i])