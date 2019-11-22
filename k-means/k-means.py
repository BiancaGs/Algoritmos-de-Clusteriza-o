
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sb
import csv
import math
import random

from sklearn.metrics.cluster import adjusted_rand_score


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

    mudou = 0

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

        if ponto.cluster != indice:
            mudou = 1

        # Atualiza o cluster do ponto
        ponto.cluster = indice
        # Adiciona o ponto ao novo cluster
        novosClusters[indice].append(ponto)


    # Compara se o cluster antigo é igual ao novo. Caso seja, para.
    if mudou == 0:
        print('clusters não mudaram na iteracao: ' + str(n_atual))
        plotarGrafico(novosClusters, centroides)
        return novosClusters

    # Verifica se não está na última iteração
    if n_atual == n_iteracoes:

        plotarGrafico(novosClusters, centroides)
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


# Plotar gráficos
def plotarGrafico(novosClusters, centroides):

    numeroClusters = len(novosClusters)

    cent = []
    for centroide in centroides:
        cent.append([
            centroide.x,
            centroide.y
        ])
    cent = np.array(cent)

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
    # # Escreve no arquivo de saída
    # np.savetxt('saida.txt', df.values, fmt='%s %d', delimiter="\t", header="Nome\tCluster")

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
    ax.scatter(cent[:, 0], cent[:, 1], c='red', s=50)

    pl.title('Gráfico de clusters')
    pl.legend(loc=2)
    pl.show()


# ====================================
# ============= MAIN =================
# ====================================

def main():

    # Abre o arquivo .txt com os dados
    arquivo = open('../Instrucoes/datasets/monkey.txt', 'r')

    # Separa as linhas do arquivo
    linhas = arquivo.read().split('\n')

    # Gera o vetor de pontos
    pontos = []
    for i in range(1, len(linhas) - 1):
        pontos.append( Objeto(linhas[i].split()[0], float(linhas[i].split()[1]), float(linhas[i].split()[2])) )

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


if __name__ == "__main__":
    main()