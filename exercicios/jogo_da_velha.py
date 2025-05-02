from time import sleep
from random import randint

grid = [[' ' for i in range(3)] for i in range(3)]  # Representa o tabuleiro do jogo da velha


player = "x"
cont = 0


def print_grid():
    for linha in grid:
        for col in linha:
            print(f"|{col}", end=" ")
        print("|")


def vencedor_x():
    # Verifica linhas
    for linha in grid:
        if linha[0] == linha[1] == linha[2] == "x": 
            return True

    # Verifica colunas
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] == "x":
            return True

    # Verifica diagonais
    if grid[0][0] == grid[1][1] == grid[2][2] == "x" or grid[0][2] == grid[1][1] == grid[2][0] == "x":
        return True

    return False

def vencedor_o():
    # Verifica linhas
    for linha in grid:
        if linha[0] == linha[1] == linha[2] == "o": 
            return True

    # Verifica colunas
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] == "o":
            return True

    # Verifica diagonais
    if grid[0][0] == grid[1][1] == grid[2][2] == "o" or grid[0][2] == grid[1][1] == grid[2][0] == "o":
        return True

    return False


while True:
    if cont == 9:
        print("Empate!")
        break
    
    if vencedor_x():
        print("O jogador X venceu!")
        break
    if vencedor_o():
        print("O jogador O venceu!")
        break
    
    if player == "x":
        print("Vez do jogador X")
        while True:
            try:
                linha = int(input("Escolha a linha: "))
                coluna = int(input("Escolha a coluna: "))
                if grid[linha][coluna] == " ":
                    grid[linha][coluna] = player
                    player = "o"
                    break
                else:
                    print("Essa posição já está ocupada. Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente.")
        sleep(1)
        
    elif player == "o":
        print("Vez do jogador O")
        while True:
            linha = randint(0, 2)
            coluna = randint(0, 2)
            if grid[linha][coluna] == " ":
                grid[linha][coluna] = player
                player = "x"
                break
        sleep(1)
    

    
    cont += 1
    print_grid()

