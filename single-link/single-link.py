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

# Distância Euclidiana
def distancia(p, q):
    # print(str(p.x) + ' ' + str(q.x))
    return math.sqrt( (p.x - q.x) ** 2 + (p.y - q.y) ** 2)

# # Classe SingleLink
# class SingleLink:



# Distância entre Clusters
# Métrica de Integração: Menor distância entre objetos dos clusters
def distanciaClusters(cluster1, cluster2):
    
    # Menor Distância
    mDistancia = 999999999999

    for pontoC1 in cluster1:
        for pontoC2 in cluster2:
            # Distância
            d = distancia(pontoC1, pontoC2)

            if d < mDistancia:
                mDistancia = d

    return mDistancia


# Calcula distância entre cada par de clusters
def clusterProximo(clusters):

    # Menor Distância
    mDistancia = 999999999999

    # Indice do Cluster 1 e 2, respectivamente
    i = 0
    j = 0

    for cluster1 in clusters:
        j = 0
        for cluster2 in clusters:
            d = distanciaClusters(cluster1, cluster2)
            # print(d)

            if cluster1 != cluster2:
                if d < mDistancia:
                    # print(mDistancia)
                    mDistancia = d
                    c1 = i
                    c2 = j
            j += 1        
        i += 1
    
    return mDistancia, c1, c2

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

    # Inicia com cada objeto em um cluster
    clusters = []
    for ponto in pontos:
        cluster = []
        cluster.append(ponto)
        clusters.append(cluster)

    # print(clusters)

    # kMin
    kMin = int(input("kMin: "))

    # kMax
    kMax = int(input("kMax: "))


    while len(clusters) > kMax: #?

        # if( len(clusters) >= kMin and len(clusters) >= kMax )
            # Escreve arquivo

        mDistancia, c1, c2 = clusterProximo(clusters)

        # print(str(c1)+ ' '+ str(c2))

        print(len(clusters))

        # Integra os clusters mais próximos
        clusters[c1].extend(clusters[c2])

        # Verifica se de fato houve integração entre os clusters
        # for p in clusters[0]:
        #     print(str(p.x) + ' ' + str(p.y))

        del clusters[c2]

        print(len(clusters))

    


if __name__ == "__main__":
    main()