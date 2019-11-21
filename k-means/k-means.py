
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sb
import csv
import math
import random


# !!!! FUNCOES DE TESTE
def imprimirCentroides(centroides):
    for centroide in centroides:
        print('(' + str(centroide.x) + ',' + str(centroide.y) + ')', end = ' - ')

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
    return math.sqrt( (p.x - q.x) ** 2 + (p.y - q.y) ** 2)

# Centróide do cluster
def centroide(cluster):

    somaX = 0.0
    somaY = 0.0
    n = len(cluster)

    for ponto in cluster:
        somaX += ponto.x

    for ponto in cluster:
        somaY += ponto.y
    
    return Objeto('', somaX / float(n), somaY / float(n))

# Calcula novos clusters
def calculaNovosClusters(centroides, pontos, clusters, k, n_atual, n_iteracoes):

    novosClusters = []
    for i in range(0, k):
        cluster = []
        novosClusters.append(cluster)

    # print(novosClusters)
    # print(centroides)

    for ponto in pontos:

        menor = 9999999999999999999

        # Indice do centroide encontrado
        i = 0
        
        for centroide in centroides:
            
            dist = distancia(ponto, centroide)
            # print('(' + str(ponto.x) + ',' + str(ponto.y) + ') e (' + str(centroide.x) + ',' + str(centroide.y) + ') = ' + str(dist))
            # print(dist)
            
            if dist < menor:
                menor = dist
                indice = i

            i += 1

        novosClusters[indice].append(ponto)

    
    # Compara se o cluster antigo é igual ao novo. Caso seja, para.
    # TODO
    # print(novosClusters)
    

    if n_atual == n_iteracoes:

        pontos = []
        for ponto in novosClusters[0]:
            pontos.append([
                ponto.x,
                ponto.y
            ])

        df = pd.DataFrame(pontos, columns = ['d1', 'd2'], dtype = float)
        sb.pairplot(df)
        pl.show()

        # print(novosClusters)

        return novosClusters
    else:
        novosCentroides = calculaNovosCentroides(novosClusters)
        # imprimirCentroides(novosCentroides)
        # print('')
        calculaNovosClusters(novosCentroides, pontos, novosClusters, k, n_atual + 1, n_iteracoes)


def calculaNovosCentroides(clusters):

    novosCentroides = []
    for cluster in clusters:
        cent = centroide(cluster)
        novosCentroides.append(cent)
    return novosCentroides


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

    # Pergunta o número de clusters
    k = int(input("Número de clusters: "))

    # Pergunta o número máximo de iterações
    n_iteracoes = int(input("Numero de iterações: "))

    # Escolhe 'k' pontos aleatórios
    centroides = []
    for i in range(0, k):
        centroides.append(random.choice(pontos))

    # Cria os clusters
    clusters = []
    for ponto in centroides:
        cluster = []
        cluster.append(ponto)
        clusters.append(cluster)

    
    novosClusters = calculaNovosClusters(centroides, pontos, clusters, k, 0, n_iteracoes)
    # print(novosClusters)

    # pontos = []
    # for ponto in novosClusters[0]:
    #     pontos.append([
    #         ponto.x,
    #         ponto.y
    #     ])

    # df = pd.DataFrame(pontos, columns = ['d1', 'd2'], dtype = float)
    # sb.pairplot(df)
    # pl.show()

    # print(clusters)

    # for p in centroides:
    #     print(str(p.x) + ' ' + str(p.y))


    # for i in range(1, len(linhas)):
    #     print(linhas[i])


if __name__ == "__main__":
    main()