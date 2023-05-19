import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()
grafo.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])

grafo.add_edge('A', 'B')
grafo.add_edge('C', 'E')
grafo.add_edge('E', 'D')
grafo.add_edge('F', 'G')
grafo.add_edge('F', 'H')
grafo.add_edge('G', 'J')
grafo.add_edge('G', 'I')
grafo.add_edge('H', 'J')
grafo.add_edge('H', 'L')
grafo.add_edge('H', 'M')
grafo.add_edge('M', 'L')
grafo.add_edge('L', 'K')
grafo.add_edge('K', 'J')
grafo.add_edge('I', 'K')

print('Lista das arestas:', grafo.edges())

subgrafos = [grafo.subgraph(s) for s in nx.connected_components(grafo)]
print('Quantidade decomponentes conexos:', len(subgrafos))

# Os subgrafos seram desenhados em um layout de 2 linhas e 2 colunas
# O subgrafo 1 sera desenhado nas coordenadas (1, 1)
subArea1 = plt.subplot(2, 2, 1)
nx.draw_planar(
    subgrafos[0],
    with_labels = True, # Mostra o nome dos vertices
    node_size = 300, # Define o tamanho dos vertices em 300
    node_color = 'r', # Define a cor dos vertices em vermelho
    )

# O subgrafo 2 sera desenhado nas coordenadas (1, 2)
subarea2 = plt.subplot(2, 2, 2)
nx.draw_spectral(
    subgrafos[1],
    with_labels = True,
    node_size = 300,
    node_color = 'b',
    )

# O subgrafo 3 sera desenhado nas coordenadas (2, 1)
subarea3 = plt.subplot(2, 2, 3)
nx.draw_spectral(
    subgrafos[2],
    with_labels = True,
    node_size = 300,
    node_color = 'g',
    )

menorCaminhoKF = nx.all_shortest_paths(grafo, 'K', 'F')
print('Menor caminho entre K e F:', list(menorCaminhoKF))

caminhoAM = nx.all_simple_paths(grafo, 'A', 'M')
print('Caminho entre A e M:', list(caminhoAM))

caminhoIM = nx.all_simple_paths(grafo, 'I', 'M')
print('Caminho entre I e M:', list(caminhoIM))

plt.savefig('Alfabeto.png')
plt.show()