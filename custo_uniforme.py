import heapq

grid = [
    ['I', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '#', 'L', '.'],
    ['.', 'L', '#', 'T', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

pos_inicial = (0, 0)  # Posição inicial do agente
pos_tesouro = (3, 3)  # Posição do tesouro

def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
  linhas = len(grid)
  colunas = len(grid[0])
  inicio = fim = None

  # Definindo os movimentos possíveis (cima, baixo, esquerda, direita)
  movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  visitados = set()

  # Encontra a posição inicial e a do tesouro
  for i in range(linhas):
    for j in range(colunas):
      if grid[i][j] == "I":
        pos_inicial = (i, j)
      if grid[i][j] == "T":
        pos_tesouro = (i, j)

  def pos_valida(x,y):
    return 0 <= x < linhas and 0 <= y < colunas and grid[x][y] != "#"

  fila = [(0, pos_inicial)]  # (custo, posição)
  visitados.add(pos_inicial)















