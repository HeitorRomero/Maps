# Menor Caminho entre Municípios de Mato Grosso do Sul

Trabalho desenvolvido para a disciplina **Teoria dos Grafos** (UFGD).

O programa modela os municípios de Mato Grosso do Sul como um grafo ponderado (distâncias em km) e utiliza o **algoritmo de Dijkstra** para encontrar o menor caminho entre dois municípios escolhidos pelo usuário, exibindo a rota, o custo total e uma visualização gráfica do caminho encontrado.

## Como funciona

1. O programa lê a matriz de distâncias de `matriz_municipios_ms.csv` e monta um grafo com [NetworkX](https://networkx.org/), onde cada município é um nó e cada aresta representa uma ligação direta com peso igual à distância em km (`inf` indica que não há ligação direta entre os dois municípios).
2. O usuário informa o município de **saída** e o de **destino** (ou `S` para sair).
3. O programa calcula o menor caminho na rede inteira com `nx.dijkstra_path` / `nx.dijkstra_path_length`, considerando também rotas indiretas por outros municípios.
4. O resultado é exibido no terminal (rota e custo total) e representado visualmente com [Matplotlib](https://matplotlib.org/), destacando em vermelho os nós e arestas do caminho encontrado sobre o grafo completo.

## Estrutura do projeto

```
.
├── main.py                     # script principal (leitura do grafo, cálculo e visualização)
├── matriz_municipios_ms.csv    # matriz de distâncias (km) entre os municípios de MS
└── README.md
```

> Ajuste o nome do script principal acima caso seja diferente de `main.py` no repositório.

## Requisitos

- Python 3.x
- [NetworkX](https://networkx.org/)
- [Matplotlib](https://matplotlib.org/)

Instalação:

```bash
pip install networkx matplotlib
```

## Como executar

```bash
python3 main.py
```

Exemplo de interação:

```
Qual município de saída?
Dourados
Qual município de destino?
Corumba
---------------------------------------------------------------------------------------
Rota: Dourados -> ... -> Corumba
Custo total: XXX km
```

Uma janela do Matplotlib será aberta com o grafo completo e o caminho mínimo destacado.

## Formato dos dados de entrada

`matriz_municipios_ms.csv` é uma matriz de adjacência entre os 79 municípios de MS:

- A primeira linha e a primeira coluna contêm os nomes dos municípios.
- Cada célula `[i][j]` contém a distância direta (em km) entre o município `i` e o município `j`.
- O valor `inf` indica que não existe ligação direta entre os dois municípios (não impede o cálculo do menor caminho, que pode passar por municípios intermediários).
- A diagonal principal é sempre `0` (distância de um município para ele mesmo).

## Observações

- Nomes de municípios devem ser digitados exatamente como aparecem na lista impressa pelo programa (sem acentuação, conforme o CSV).
- Se não existir nenhum caminho entre os dois municípios escolhidos, o programa informa e encerra.
