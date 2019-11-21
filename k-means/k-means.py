
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sb
import csv
import math

# Classe Objeto
class Objeto:

    # Construtor
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
        
    # Distância Euclidiana
    def distancia(self, p, q):
        dx = p.x - q.x
        dy = p.y - q.y
        return math.sqrt(dx ** 2 + dy ** 2)



# Classe KMeans
class KMeans:

    def __init__(self, k = 3, tolerancia = 0.0001, max_iteracoes = 500):
        self.k = k
        self.tolerancia = tolerancia
        self.max_iteracoes = max_iteracoes


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

    #!! Gera um gráfico
    # df = pd.DataFrame(pontos, columns = ['d1', 'd2'], dtype = float)
    # sb.pairplot(df)
    # pl.show()

    # print(linhas[1].split())

    # k = int(input("Número de clusters: "))
    # n_iteracoes = int(input("Numero de iterações: "))


    # for i in range(1, len(linhas)):
    #     print(linhas[i])


if __name__ == "__main__":
    main()