import heapq

# h(n) = |x1 - x2| + |y1 - y2|

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

def busca_gulosa(grid, pos_inicial, pos_tesouro):
    obstaculo = "#"
    linhas = len(grid)
    colunas = len(grid[0])

    def heuristica(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    # Encontra posições de início e objetivo
    for i in range(linhas):
        for j in range(colunas):
            if grid[i][j] == "I":
                pos_inicial = (i, j)
            if grid[i][j] == "T":
                pos_tesouro = (i, j)

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # cima, baixo, esquerda, direita
    visitado = set()
    fila = []
    heapq.heappush(fila, (0, pos_inicial, [pos_inicial]))  # custo, posição, caminho

    while fila:
        custo, atual, caminho = heapq.heappop(fila)
        x, y = atual

        if atual in visitado:
            continue
        visitado.add(atual)

        if atual == pos_tesouro:
            return caminho

        for dx, dy in movimentos: # cima, baixo, esquerda, direita
            nx, ny = x + dx, y + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and grid[nx][ny] != obstaculo:
                nova_posicao = (nx, ny)
                if nova_posicao not in visitado:
                    heapq.heappush(fila, (heuristica(nova_posicao,pos_tesouro),nova_posicao, caminho + [nova_posicao]))

    return []

# Executar
caminho = busca_gulosa(grid, pos_inicial, pos_tesouro)
print(caminho)
