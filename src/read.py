import csv
import os
import networkx as nx
import matplotlib.pyplot as plt

matriz_municipios_ms = []
nomes_municipios = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'matriz_municipios_ms.csv')

with open(csv_path, 'r', encoding='utf-8') as file:
    leitor = csv.reader(file, delimiter=',')
    cabecalho = next(leitor)
    for linha in leitor:
        nome_municipio = linha[0]
        valores = linha[1:]
        linha_peso = [float(valor) for valor in valores]
        nomes_municipios.append(nome_municipio)
        matriz_municipios_ms.append(linha_peso)


G = nx.Graph()
G.add_nodes_from(nomes_municipios)

n = len(nomes_municipios)
for i in range(n):
    for j in range(i + 1, n):
        peso = matriz_municipios_ms[i][j]
        if peso != float('inf'):
            G.add_edge(nomes_municipios[i], nomes_municipios[j], weight=peso)

print("----------------------------------MAPA DE MUNICÍPIOS MS----------------------------------")
print("Municípios disponíveis:")
for municipio in nomes_municipios:
    print(municipio)
print("Digite S para sair do programa.")

print("---------------------------------------------------------------------------------------")
print("Qual município de saída?")
read_municipio_saida = input().strip()
if read_municipio_saida.upper() == 'S':
    exit()
print("Qual município de destino?")
read_municipio_destino = input().strip()
if read_municipio_destino.upper() == 'S':
    exit()
print("---------------------------------------------------------------------------------------")

if read_municipio_saida not in nomes_municipios:
    print(f"Município de saída '{read_municipio_saida}' não encontrado.")
    exit()

if read_municipio_destino not in nomes_municipios:
    print(f"Município de destino '{read_municipio_destino}' não encontrado.")
    exit()

if read_municipio_saida == read_municipio_destino:
    print("O município de saída e o município de destino não podem ser iguais.")
    exit()

# --- calcula o menor caminho considerando toda a rede ---
try:
    caminho = nx.dijkstra_path(G, read_municipio_saida, read_municipio_destino, weight='weight')
    distancia_total = nx.dijkstra_path_length(G, read_municipio_saida, read_municipio_destino, weight='weight')
except nx.NetworkXNoPath:
    print(f"Não existe caminho entre {read_municipio_saida} e {read_municipio_destino}.")
    exit()

print(f"Rota: {' -> '.join(caminho)}")
print(f"Custo total: {distancia_total} km")

# --- desenha o grafo destacando o caminho ---
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 9))

nx.draw_networkx_edges(G, pos, edge_color='lightgray')
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=300)
nx.draw_networkx_labels(G, pos, font_size=7)

arestas_caminho = list(zip(caminho, caminho[1:]))
nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, edge_color='red', width=2.5)
nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color='red', node_size=350)

plt.title(f"Menor caminho: {read_municipio_saida} → {read_municipio_destino} ({distancia_total} km)")
plt.axis('off')
plt.show()