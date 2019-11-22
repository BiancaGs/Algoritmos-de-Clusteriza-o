import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sb
from scipy.spatial import distance_matrix
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
import csv
import math
import random

# Classe Objeto
class Objeto:

    # Construtor
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
    

# ====================================
# ============= MAIN =================
# ====================================

def main():

    # Abre o arquivo .txt com os dados
    arquivo = open('../Instrucoes/datasets/c2ds1-2sp.txt', 'r')

    # Separa as linhas do arquivo
    linhas = arquivo.read().split('\n')

    # Gera o vetor de pontos
    pontos = []
    for i in range(1, len(linhas) - 1):
        pontos.append( Objeto(linhas[i].split()[0], float(linhas[i].split()[1]), float(linhas[i].split()[2])) )

    p = []
    for ponto in pontos:
        p.append([
            ponto.x, ponto.y
        ])


    df = pd.DataFrame(p, columns = ['x', 'y'], dtype = float)
    
    kmeans = KMeans(n_clusters=3).fit(df)
    centroids = kmeans.cluster_centers_
    print(type(centroids))
    print(centroids)

    pl.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
    pl.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    pl.show()


if __name__ == "__main__":
    main()