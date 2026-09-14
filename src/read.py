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

for nome, linha in zip(nomes_municipios, matriz_municipios_ms):
    print(nome, linha)