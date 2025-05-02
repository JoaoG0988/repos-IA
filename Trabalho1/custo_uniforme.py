import heapq

grid = [
    ['I', '.', 'L', 'L', 'L', '.', 'T'],
    ['.', '.', '.', 'L', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
]

pos_inicial = (0, 0)
pos_tesouro = (0, 6)

def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
    lama = "L"
    obstaculo = "#"
    linhas = len(grid)
    colunas = len(grid[0])

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
        print(f"Fila: {fila}")
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
                novo_custo = custo + (5 if grid[nx][ny] == lama else 1)
                heapq.heappush(fila, (novo_custo, (nx, ny), caminho + [(nx, ny)]))

    return []

# Executar
caminho = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)
print(caminho)
