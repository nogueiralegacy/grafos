import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()

grafo.add_nodes_from([0, 1, 2, 3, 4, 5])

def grafo_roda(grafo, elementoCentral):
    conjuntoK = list(grafo.nodes())
    conjuntoK.remove(elementoCentral)
    
    for vertice in conjuntoK:
            grafo.add_edge(elementoCentral, vertice)
        
    for indice in range(0, len(conjuntoK) - 1):
        grafo.add_edge(conjuntoK[indice], conjuntoK[indice + 1])
    
    grafo.add_edge(conjuntoK[len(conjuntoK) - 1], conjuntoK[0])


elementoCentral = 3
grafo_roda(grafo=grafo, elementoCentral=elementoCentral)

node_color = ['red' if node == elementoCentral else 'blue' for node in grafo.nodes()]

nx.draw_spectral(grafo, with_labels=True, node_color=node_color)

plt.savefig('Roda.png')
plt.show()