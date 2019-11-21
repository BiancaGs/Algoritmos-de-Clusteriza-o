import numpy as np
import pandas as pd
# import matplotlib.pyplot as pl
# import seaborn as sb
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
        self.cluster = -1


# # Classe AverageLink
# class AverageLink:

    

# ====================================
# ============= MAIN =================
# ====================================

def main():

# Entrada: Um arquivo texto com o conjunto de dados, kMin e kMax 
# - Intervalo de valores para k (número de clusters) em que serão produzidas partições a partir de cortes no dendrograma


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

    # kMin
    # kMin = int(input("kMin: "))

    # kMax
    # kMax = int(input("kMax: "))




if __name__ == "__main__":
    main()