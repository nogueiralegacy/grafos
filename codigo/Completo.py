import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()

grafo.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])

def grafo_completo(grafo):
    conjuntoK = list(grafo.nodes())

    for indice in range(0, len(conjuntoK)):
        for indice2 in range(indice + 1, len(conjuntoK)):
            grafo.add_edge(conjuntoK[indice], conjuntoK[indice2])
            
grafo_completo(grafo=grafo)
nx.draw_circular(grafo, with_labels=True, node_size=300, node_color='grey')

plt.savefig("completo.png")
plt.show()