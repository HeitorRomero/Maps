import csv
import os

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

#for nome, linha in zip(nomes_municipios, matriz_municipios_ms):
#    print(nome, linha)

print("----------------------------------MAPA DE MUNICÍPIOS MS----------------------------------")
print("Municíos disponíveis:")
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

if read_municipio_saida in nomes_municipios and read_municipio_destino in nomes_municipios:
    index_saida = nomes_municipios.index(read_municipio_saida)
    index_destino = nomes_municipios.index(read_municipio_destino)
    distancia = matriz_municipios_ms[index_saida][index_destino]
    print(f"A distância entre {read_municipio_saida} e {read_municipio_destino} é: {distancia} km")