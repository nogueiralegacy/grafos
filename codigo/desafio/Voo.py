import pandas as pd
import os
import networkx as nx
import matplotlib.pyplot as plt

NOME_DO_ARQUIVO = "flights.csv"

diretorio_atual = os.getcwd()

path = os.path.join(diretorio_atual, NOME_DO_ARQUIVO)

df = pd.read_csv(path,
                low_memory=False,
                encoding='UTF-8',
                sep=',',
                header=0,
                usecols=['ORIGIN_AIRPORT', 'DESTINATION_AIRPORT']
                )

G = nx.from_pandas_edgelist(df,
                            source='ORIGIN_AIRPORT',
                            target='DESTINATION_AIRPORT',
                            )

nx.draw(G, with_labels=True)

plt.savefig('Voo.png')
plt.show()

def maior_grau(grafo):
    conjuntoK = list(grafo.nodes())
    maiorGrau = 0
    for indice in range(0, len(conjuntoK)):
        atual = grafo.degree(conjuntoK[indice])
        if (atual > maiorGrau):
            maiorGrau = atual
    return maiorGrau
    
print('Maior grau:', maior_grau(G))

caminho_ONT_to_EWR = list(nx.all_simple_paths(G, 'ONT', 'EWR'))

print('Todos os caminhos possiveis entre ONT e EWR:', caminho_ONT_to_EWR)