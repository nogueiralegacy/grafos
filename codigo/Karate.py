import numpy as np
import random
import networkx as nx
from IPython import display
import matplotlib.pyplot as plt

G_karate = nx.karate_club_graph()
pos = nx.random_layout(G_karate)

nx.draw(G_karate, cmap = plt.get_cmap('rainbow'), with_labels = True, pos = pos)

print('Numero de nos:', G_karate.number_of_nodes())

print("Numero de arestas:", G_karate.number_of_edges())

sumGraus = 0
for indice in range(0, G_karate.number_of_nodes()):
    sumGraus += G_karate.degree(indice)
    
media = round(sumGraus / G_karate.number_of_nodes(), 2)
print("Grau medio:", media)

maiorGrau = 0
for indice in range(0, G_karate.number_of_nodes()):
    atual = G_karate.degree(indice)
    if (atual > maiorGrau):
        maiorGrau = atual
        
print('Maior grau:', maiorGrau)

menorGrau = maiorGrau
for indice in range(0, G_karate.number_of_nodes()):
    atual = G_karate.degree(indice)
    if (atual < menorGrau):
        menorGrau = atual

print('Menor grau:', menorGrau)

grauVertice7 = G_karate.degree(7)
print('Grau do vertice 7:', grauVertice7)
        
plt.show()