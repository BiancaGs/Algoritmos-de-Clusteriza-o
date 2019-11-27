import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import single, fcluster
from scipy.spatial.distance import pdist
import seaborn as sb
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

# Plotar gráficos
def plotarGrafico(novosClusters):

    numeroClusters = len(novosClusters)

    dataframe = []

    # Cria os dados
    data = []
    for indiceCluster, cluster in enumerate(novosClusters):
        x = []
        y = []
        for ponto in cluster:
            dataframe.append([
                ponto.nome,
                indiceCluster
            ])
            x.append(ponto.x)
            y.append(ponto.y)
        a = np.array(x)
        b = np.array(y)
        g = ( a, b )
        data.append(g)
    data = tuple(data)

    df = pd.DataFrame(dataframe, columns = ['nome', 'cluster'])
    # Escreve no arquivo de saída
    np.savetxt('saida.txt', df.values, fmt='%s %d', delimiter="\t", header="Nome\tCluster")

    # Cria as cores
    colors = []
    for i in range(0, numeroClusters):
        r = lambda: random.randint(0,255)
        color = '#%02X%02X%02X' % (r(),r(),r())
        colors.append(color)
    colors = tuple(colors)

    # Cria as labels
    labels = []
    for i in range(0, numeroClusters):
        nome = "cluster" + str(i)
        labels.append(nome)
    labels = tuple(labels)

    # Cria o gráfico
    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

    for data, color, group in zip(data, colors, labels):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

    pl.title('Gráfico de clusters')
    pl.legend(loc=2)
    pl.show()


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

    p = []
    for ponto in pontos:
        p.append([
            ponto.x, ponto.y
        ])

    # y = pdist(p)
    # Z = single(y)
    # print(Z)
    # fig = pl.figure(figsize=(25, 10))
    # dn = dendrogram(Z)
    # pl.show()
    # return

    while 1: #?

        if( len(clusters) >= kMin and len(clusters) <= kMax ):
            # print(len(clusters))
            # print(clusters)
            plotarGrafico(clusters)
            break

        mDistancia, c1, c2 = clusterProximo(clusters)

        # print(str(c1)+ ' '+ str(c2))

        print(len(clusters))

        # Integra os clusters mais próximos
        clusters[c1].extend(clusters[c2])

        # Verifica se de fato houve integração entre os clusters
        # for p in clusters[0]:
        #     print(str(p.x) + ' ' + str(p.y))

        del clusters[c2]

        # print(len(clusters))

if __name__ == "__main__":
    main()