
grid = [
    ['I', '#', '.', '#', 'L', 'L', 'T'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.'],
]

pos_inicial = (0, 0)
pos_tesouro = (0, 6)
import heapq

def busca_a_estrela(grid, pos_inicial, pos_tesouro):
    obstaculo = "#"
    linhas = len(grid)
    colunas = len(grid[0])

    def heuristica(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])  # distância de Manhattan

    # Encontra início e fim automaticamente se necessário
    for i in range(linhas):
        for j in range(colunas):
            if grid[i][j] == "I":
                pos_inicial = (i, j)
            if grid[i][j] == "T":
                pos_tesouro = (i, j)

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
    visitado = {}
    fila = []

    # heap: (f = g + h, g, posição, caminho)
    heapq.heappush(fila, (heuristica(pos_inicial, pos_tesouro), 0, pos_inicial, [pos_inicial]))

    while fila:
        f, g, atual, caminho = heapq.heappop(fila)
        x, y = atual

        # Se já visitou com custo menor, ignora
        if atual in visitado and visitado[atual] <= g:
            continue
        visitado[atual] = g

        if atual == pos_tesouro:
            return caminho

        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and grid[nx][ny] != obstaculo:
                nova_pos = (nx, ny)
                custo_terreno = 5 if grid[nx][ny] == "L" else 1
                novo_g = g + custo_terreno
                h = heuristica(nova_pos, pos_tesouro)
                heapq.heappush(fila, (novo_g + h, novo_g, nova_pos, caminho + [nova_pos]))

    return []

caminho = busca_a_estrela(grid, pos_inicial, pos_tesouro)
print(caminho)
