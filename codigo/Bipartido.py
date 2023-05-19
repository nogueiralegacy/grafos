import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

grafo = nx.Graph()

grafo.add_nodes_from([0, 1, 2, 3 ,4, 5, 6, 7, 8, 9])

# V é o conjunto de vertices
# K é o conjunto de vertices
# K e V são conjuntos disjuntos
# Qualquer par de vertices formando por um elemento do conjunto K e um elemento
# do conjunto V formam uma aresta
# Nenhum par de vertices formados por elementos de um mesmo conjunto tem
# uma aresta os ligando
def grafo_bipartido_completo(V, K, grafo):
    for verticeV in V:
        for verticeK in K:
            grafo.add_edge(verticeV, verticeK)
    
grafo_bipartido_completo(V=[0, 1, 2, 3], K=[4, 5, 6, 7, 8, 9], grafo=grafo)

node_color = ['red' if node < 4 else 'blue' for node in grafo.nodes()]

nx.draw_circular(grafo, with_labels=True, node_color=node_color)

plt.savefig('Bipartido.png')
plt.show()