import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()

grafo.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9]) 

def grafo_ciclo(grafo):
    conjuntoK = list(grafo.nodes())
    for indice in range(0, len(conjuntoK) - 1):
        grafo.add_edge(conjuntoK[indice], conjuntoK[indice + 1])
        
    grafo.add_edge(conjuntoK[len(conjuntoK) - 1], conjuntoK[0])
        
grafo_ciclo(grafo=grafo)

nx.draw(grafo, with_labels=True, node_color='blue')

plt.savefig('Ciclo.png')
plt.show()