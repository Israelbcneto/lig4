pos_preenchidas = []
PECA2 = " X "
PECA1 = " O "
VAZIA = " - "
matriz = []
linha = []
voltar = False
ult_peca = PECA2
player = PECA1  # Aqui o player começa recebendo " X "
a = 0
b = 0
coluna = 1
contador_gameover = 0
voltar = False
from random import *
import time
import os
os.system("cls" if os.name == "nt" else "clear")
cont = 0
verificar = 0

def criarMatriz(matriz, linha):
    for i in range(LINHA):
        linha = []
        for j in range(COLUNA):
            linha.append(VAZIA)
        matriz.append(linha)
    return (matriz)


def escolheColuna(player, ult_peca):
    while True:
        if voltar == True:  # Aqui só entra se o usuário digitar uma coluna inválida
            if ult_peca == PECA1:
                player = PECA1
            if ult_peca == PECA2:
                player = PECA2
        if player == PECA1:  # Aqui entra quando o player é X, ou seja, na primeira rodada do jogo
            try:
                coluna = int(input("Player 1, escolha a coluna para seu próximo movimento: "))
                player = PECA2  # Aqui o player muda pra O
                ult_peca = PECA1  # Aqui é a variável que indica se o último jogador foi X ou O
                break
            except ValueError:
                print("coluna invalida, escolha outra")
        else:  # Aqui entra quando o player é O, ou seja, na segunda rodada do jogo
            try:
                coluna = int(input("Player 2, escolha a coluna para seu próximo movimento: "))
                player = PECA1  # Aqui o player muda pra X
                ult_peca = PECA2  # Aqui é a variável que indica se o último jogador foi X ou O
                break
            except ValueError:
                print("coluna invalida, escolha outra")

    return coluna, ult_peca, player

def escolheColuna_IA(player, ult_peca, voltar,coluna):
    cont = 0
    while True:
        if voltar == True:  # Aqui só entra se o usuário digitar uma coluna inválida
            if ult_peca == PECA1:
                player = PECA1
            if ult_peca == PECA2:
                player = PECA2
            voltar = False
        if player == PECA1:  # Aqui entra quando o player é X, ou seja, na primeira rodada do jogo
            try:
                coluna = int(input("Player 1, escolha a coluna para seu próximo movimento: "))
                player = PECA2  # Aqui o player muda pra O
                ult_peca = PECA1 # Aqui é a variável que indica se o último jogador foi X ou O
                voltar = False
                break
            except ValueError:
                print("coluna invalida, escolha outra")
        else:  # Aqui entra quando o player é O, ou seja, na segunda rodada do jogo
            try:
                b = randrange(1,4)
                if b == 1:
                    if matriz[coluna+1][pos_preenchidas[coluna-1]] == VAZIA:
                        coluna = coluna
                    else:
                        cont += 1
                elif b == 2:
                    if matriz[coluna][pos_preenchidas[coluna-1]+1] == VAZIA:
                        coluna = coluna + 1
                elif b == 3:
                    if matriz[coluna][pos_preenchidas[coluna - 1] - 1] == VAZIA:
                        coluna -= 1
                else:
                    coluna = int(randrange(1, COLUNA + 1))
            except:
                coluna = int(randrange(1, COLUNA+1))
            player = PECA1  # Aqui o player muda pra X
            ult_peca = PECA2  # Aqui é a variável que indica se o último jogador foi X ou O
            break
        voltar = False
    return coluna, ult_peca, player, voltar

def printar_matriz(LINHA, matriz):
    for i in range(LINHA):
        print(matriz[i])

def jogar(matriz, pos_preenchidas, coluna, IA, player,VAZIA,voltar):
    if voltar == True:
        escolheColuna_IA(player, ult_peca,voltar,coluna)
    if IA == "2":
        if pos_preenchidas < 0:
            print("Coluna cheia, escolha outra.")
            voltar = True
        elif matriz[pos_preenchidas][coluna - 1] == VAZIA:
            matriz[pos_preenchidas][coluna - 1] = player
            printar_matriz(LINHA, matriz)
            voltar = False
        else:
            voltar = False
    elif IA == "1":
        while (True):
            try:
                if pos_preenchidas < 0:
                    print("Coluna cheia, escolha outra.")
                    voltar = True
                elif matriz[pos_preenchidas][coluna - 1] == VAZIA:
                    matriz[pos_preenchidas][coluna - 1] = player
                    if player == PECA1:
                        time.sleep(2)

                        print("Vez da IA:")
                    printar_matriz(LINHA, matriz)
                    voltar = False
                break
            except Exception:
                pass
    return pos_preenchidas - 1, voltar

def definir_linha():
    while (True):
        try:
            LINHA = int(input("Digite o numero desejado de linhas (sendo ele maior ou igual a 4 e menor ou igual a 10): "))
            while (LINHA < 4 or LINHA > 10):
                LINHA = int(input("Numero inválido de linhas, escolha outro (sendo ele maior ou igual a 4 e menor ou igual a 10): "))
            break
        except ValueError:
            print("Numero inválido de linhas, escolha outro. ")
    return LINHA


def definir_coluna():
    while (True):
        try:
            COLUNA = int(input("Digite o numero desejado de colunas (sendo ele maior ou igual a 4 e menor ou igual a 10): "))
            while (COLUNA < 4 or COLUNA > 10):
                COLUNA = int(input("Numero inválido de colunas, escolha outro (sendo ele maior ou igual a 4 e menor ou igual a 10): "))
            break
        except ValueError:
            print("Numero inválido de colunas, escolha outro. ")
    return COLUNA


def fim_de_jogo(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover,b,preenchimento):
    contador_gameover = 0
    FUNCAO_LINHA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    FUNCAO_COLUNA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    contador_gameover = DIAGONAL_INFERIOR_DIREITA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    DIAGONAL_SUPERIOR_ESQUERDA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    contador_gameover = DIAGONAL_SUPERIOR_DIREITA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    DIAGONAL_INFERIOR_ESQUERDA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    EMPATE(COLUNA,preenchimento)

def FUNCAO_LINHA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas,contador_gameover,preenchimento):
    for i in range(LINHA):                                  #LINHA
        for j in range(COLUNA):
            if matriz[i][j] == player:
                contador_gameover += 1
            else:
                contador_gameover = 0
            if contador_gameover == 4:
                if player == PECA2:
                    print("Player 1 ganhou o jogo!")
                else:
                    print("Player 2 ganhou o jogo!")
                quit()
        contador_gameover = 0
def FUNCAO_COLUNA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover,preenchimento):
    for t in range(COLUNA):                                              #COLUNA
        for u in range(LINHA):
            if matriz[u][t] == player:
                contador_gameover += 1
            else:
                contador_gameover = 0
            if contador_gameover == 4:
                if player == PECA2:
                    print("Player 1 ganhou o jogo!")
                else:
                    print("Player 2 ganhou o jogo!")
                quit()
        contador_gameover = 0
def DIAGONAL_INFERIOR_DIREITA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover,preenchimento):
    try:                                                                 #INFERIOR DIREITA
        while contador_gameover < 3:
            pos_preenchidas += 1
            coluna += 1
            if matriz[pos_preenchidas][coluna] == player:
                contador_gameover += 1
            else:
                break
    except Exception:
        pass
    return contador_gameover
def DIAGONAL_SUPERIOR_ESQUERDA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover,preenchimento):
    try:                                                                 #superior esquerda
        while contador_gameover < 3:
            pos_preenchidas -= 1
            coluna -= 1
            if matriz[pos_preenchidas][coluna] == player and pos_preenchidas >= 0:
                contador_gameover += 1
            else:
                break
    except Exception:
        pass
    if contador_gameover == 3:
        if player == PECA2:
            print("Player 1 ganhou o jogo!")
        else:
            print("Player 2 ganhou o jogo!")
        quit()

def DIAGONAL_SUPERIOR_DIREITA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover,preenchimento):
    contador_gameover = 0
    try:
        while contador_gameover < 3:
            pos_preenchidas -= 1                        #diagonal superior direita
            coluna += 1
            if matriz[pos_preenchidas][coluna] == player:
                contador_gameover += 1

            else:
                break
    except Exception:
        pass
    return contador_gameover
def DIAGONAL_INFERIOR_ESQUERDA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento):
    try:
        while contador_gameover < 3:                        #diagonal inferior esquerda
            pos_preenchidas += 1
            coluna -= 1
            if matriz[pos_preenchidas][coluna] == player and coluna >=0:
                contador_gameover += 1
            else:
                break
    except Exception:
        pass
    if contador_gameover == 3:
        if player == PECA2:
            print("Player 1 ganhou o jogo!")
        else:
            print("Player 2 ganhou o jogo!")
        quit()

def EMPATE(COLUNA,preenchimento):
    cont = 0
    for i in preenchimento:
        if i < 0:
            cont += 1
        if cont == COLUNA:
            print("Empatou!!")
            quit()
def escolhe_IA():
    IA = input("Digite 1 para jogar com a IA e 2 para jogar com 2 players: ")
    while IA != "1" and IA != "2":
        IA = input("Numero invalido, digite 1 para jogar com a IA e 2 para jogar com 2 players: ")
    return IA
COLUNA = definir_coluna()
LINHA = definir_linha()
matriz = criarMatriz(matriz, linha)
IA = escolhe_IA()
for i in range(COLUNA):
    pos_preenchidas.append(LINHA - 1)
printar_matriz(LINHA, matriz)
while (True):
    if IA == "2":
        coluna, ult_peca, player = escolheColuna(player, ult_peca)
        if coluna < 1 or coluna > COLUNA:
            print("Coluna inexistente, escolha outra.")
            voltar = True
    else:
        coluna,ult_peca, player, voltar = escolheColuna_IA(player, ult_peca, voltar,coluna)
        if player == PECA2:
            while coluna < 1 or coluna > COLUNA:
                print("Coluna inexistente, escolha outra.")
                voltar = True
                if voltar == True:
                    coluna, ult_peca, player, voltar = escolheColuna_IA(player, ult_peca, voltar,coluna)
    pos_preenchidas[coluna - 1], voltar = jogar(matriz, pos_preenchidas[coluna - 1], coluna, IA,player,VAZIA,voltar)
    contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, coluna - 1, pos_preenchidas[coluna - 1] + 1, a, contador_gameover, b, pos_preenchidas)
