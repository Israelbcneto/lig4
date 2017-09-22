import socket
import sys
coluna = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
contador_gameover = 0
from random import *
import time
def escolheColuna(player, ult_peca):
    while True:
        if voltar == True:  # Aqui só entra se o usuário digitar uma coluna inválida
            if ult_peca == PECA1:
                player = PECA1
            if ult_peca == PECA2:
                player = PECA2
        if player == PECA1:  # Aqui entra quando o player é X, ou seja, na primeira rodada do jogo
            try:
                if resp == 0:
                    print()
                    coluna = int(input("Player 1, escolha a coluna para seu próximo movimento: "))
                else:
                    print()
                    coluna = int(input("Player, escolha a coluna para seu próximo movimento: "))
                player = PECA2  # Aqui o player muda pra O
                ult_peca = PECA1  # Aqui é a variável que indica se o último jogador foi X ou O
                break
            except ValueError:
                print()
                print("coluna invalida, escolha outra")
        else:  # Aqui entra quando o player é O, ou seja, na segunda rodada do jogo
            try:
                print()
                coluna = int(input("Player 2, escolha a coluna para seu próximo movimento: "))
                player = PECA1  # Aqui o player muda pra X
                ult_peca = PECA2  # Aqui é a variável que indica se o último jogador foi X ou O
                break
            except ValueError:
                print()
                print("coluna invalida, escolha outra")

    return coluna, ult_peca, player


def criarMatriz(matriz, linha):
    for i in range(LINHA):
        linha = []
        for j in range(COLUNA):
            linha.append(VAZIA)
        matriz.append(linha)
    return (matriz)


def jogar(matriz, pos_preenchidas, coluna):
    if pos_preenchidas < 0:
        if IA == 2:
            print()
            print("Coluna cheia, escolha outra.")
        else:
            if player == PECA2:
                print()
                print("Coluna cheia, escolha outra.")
        voltar = True
    elif matriz[pos_preenchidas][coluna - 1] == VAZIA:
        matriz[pos_preenchidas][coluna - 1] = player
        printar_matriz(LINHA, matriz)
        voltar = False
    else:
        voltar = True
        while matriz[pos_preenchidas][coluna - 1] == VAZIA:
            if IA == 1:
                escolheColuna_IA(player,ult_peca,voltar,coluna)
            else:
                escolheColuna(player,ult_peca)
    return pos_preenchidas - 1, voltar

def printar_matriz(LINHA, matriz):
    x = 1
    print()
    for j in range(COLUNA):
        print("   %i   "%x, end = "")
        x += 1
    print()
    for i in range(LINHA):
        print(matriz[i])


def definir_linha():
    while (True):
        try:
            print()
            LINHA = int(input("Digite o numero desejado de linhas (sendo ele maior ou igual a 4 e menor ou igual a 10): "))
            while (LINHA < 4 or LINHA > 10):
                print()
                LINHA = int(input("Numero inválido de linhas, escolha outro (sendo ele maior ou igual a 4 e menor ou igual a 10): "))
            break
        except ValueError:
            print()
            print("Numero inválido de linhas, escolha outro. ")
    return LINHA


def definir_coluna():
    while (True):
        try:
            print()
            COLUNA = int(input("Digite o numero desejado de colunas (sendo ele maior ou igual a 4 e menor ou igual a 10): "))
            while (COLUNA < 4 or COLUNA > 10):
                print()
                COLUNA = int(input("Numero inválido de colunas, escolha outro (sendo ele maior ou igual a 4 e menor ou igual a 10): "))
            break
        except ValueError:
            print()
            print("Numero inválido de colunas, escolha outro. ")
    return COLUNA


def fim_de_jogo(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a, contador_gameover, b, preenchimento):
    contador_gameover = 0
    FUNCAO_LINHA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    FUNCAO_COLUNA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    contador_gameover = DIAGONAL_INFERIOR_DIREITA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas,contador_gameover, preenchimento)
    DIAGONAL_SUPERIOR_ESQUERDA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    contador_gameover = DIAGONAL_SUPERIOR_DIREITA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas,contador_gameover, preenchimento)
    DIAGONAL_INFERIOR_ESQUERDA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento)
    EMPATE(COLUNA, preenchimento)

def FUNCAO_LINHA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento):
    for i in range(LINHA):  # LINHA
        for j in range(COLUNA):
            if matriz[i][j] == player:
                contador_gameover += 1
            else:
                contador_gameover = 0
            if contador_gameover == 4:
                if player == PECA2:
                    print()
                    print("Player 1 ganhou o jogo!")
                else:
                    print()
                    print("Player 2 ganhou o jogo!")
                quit()
        contador_gameover = 0


def FUNCAO_COLUNA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento):
    for t in range(COLUNA):  # COLUNA
        for u in range(LINHA):
            if matriz[u][t] == player:
                contador_gameover += 1
            else:
                contador_gameover = 0
            if contador_gameover == 4:
                if player == PECA2:
                    print()
                    print("Player 1 ganhou o jogo!")
                else:
                    print()
                    print("Player 2 ganhou o jogo!")
                quit()
        contador_gameover = 0


def DIAGONAL_INFERIOR_DIREITA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento):
    try:  # INFERIOR DIREITA
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


def DIAGONAL_SUPERIOR_ESQUERDA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover,
                               preenchimento):
    try:  # superior esquerda
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
            print()
            print("Player 1 ganhou o jogo!")
        else:
            print()
            print("Player 2 ganhou o jogo!")
        quit()


def DIAGONAL_SUPERIOR_DIREITA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover, preenchimento):
    contador_gameover = 0
    try:
        while contador_gameover < 3:
            pos_preenchidas -= 1  # diagonal superior direita
            coluna += 1
            if matriz[pos_preenchidas][coluna] == player:
                contador_gameover += 1

            else:
                break
    except Exception:
        pass
    return contador_gameover


def DIAGONAL_INFERIOR_ESQUERDA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, contador_gameover,
                               preenchimento):
    try:
        while contador_gameover < 3:  # diagonal inferior esquerda
            pos_preenchidas += 1
            coluna -= 1
            if matriz[pos_preenchidas][coluna] == player and coluna >= 0:
                contador_gameover += 1
            else:
                break
    except Exception:
        pass
    if contador_gameover == 3:
        if player == PECA2:
            print()
            print("Player 1 ganhou o jogo!")
        else:
            print()
            print("Player 2 ganhou o jogo!")
        quit()


def EMPATE(COLUNA, preenchimento):
    cont = 0
    for i in preenchimento:
        if i < 0:
            cont += 1
        if cont == COLUNA:
            print()
            print("Empatou!!")
            quit()

def escolheColuna_IA(player, ult_peca, voltar,coluna):
    while True:
        if voltar == True:  # Aqui só entra se o usuário digitar uma coluna inválida
            if ult_peca == PECA1:
                player = PECA1
            if ult_peca == PECA2:
                player = PECA2
            voltar = False
        if player == PECA1:  # Aqui entra quando o player é X, ou seja, na primeira rodada do jogo
            try:
                print()
                coluna = int(input("Player 1, escolha a coluna para seu próximo movimento: "))
                player = PECA2  # Aqui o player muda pra O
                ult_peca = PECA1 # Aqui é a variável que indica se o último jogador foi X ou O
                voltar = False
                break
            except ValueError:
                print()
                print("Coluna invalida, escolha outra")
        else:  # Aqui entra quando o player é O, ou seja, na segunda rodada do jogo
            coluna1, cont1 = IA_linha(matriz,player,COLUNA,coluna,pos_preenchidas[coluna-1])
            coluna2, cont2 = IA_coluna(matriz,player,COLUNA,coluna,pos_preenchidas[coluna-1])
            print()
            time.sleep(1)
            print("Vez da IA:")
            if cont1 > cont2 and cont1<LINHA:
                coluna = coluna1
            elif cont2 > cont1 and cont2<COLUNA:
                coluna = coluna2
            elif cont1>=LINHA and cont2<COLUNA:
                coluna = coluna2
            elif cont2>=COLUNA and cont1<LINHA:
                coluna = coluna1
            elif cont2>=COLUNA and cont1>=LINHA:
                print()
                print("Empatou!!!")
                quit()
            else:
                coluna = randrange(1,3)
                if coluna == 1:
                    coluna = coluna1
                else:
                    coluna = coluna2
            while pos_preenchidas[coluna-1] <= -1:
                coluna = randrange(1,COLUNA+1)
            player = PECA1  # Aqui o player muda pra X
            ult_peca = PECA2  # Aqui é a variável que indica se o último jogador foi X ou O
            break
        voltar = False
    return coluna, ult_peca, player, voltar

def IA_linha(matriz, player, COLUNA, coluna, pos_preenchidas1):
    maior = -1
    ind = -1
    contlinha_IA = 0
    try:
        for i in range(COLUNA):  # LINHA
            if matriz[pos_preenchidas1+1][i] == player:
                contlinha_IA += 1
    except Exception:
        pass
    for j in range(COLUNA):
        if pos_preenchidas[j]>-1 and pos_preenchidas[j]>maior:
            maior = pos_preenchidas[j]
            ind = j+1

    return ind, contlinha_IA

def IA_coluna(matriz, player, COLUNA, coluna, pos_preenchidas):
    contlinha_IA = 0
    try:
        for i in range(LINHA):
            if matriz[i][coluna-1] == player:
                contlinha_IA += 1
    except Exception:
        pass
        if contlinha_IA >=1:
            coluna = coluna
    return coluna,contlinha_IA

COLUNA = definir_coluna()
LINHA = definir_linha()
matriz = criarMatriz(matriz, linha)
for i in range(COLUNA):
    pos_preenchidas.append(LINHA - 1)
printar_matriz(LINHA, matriz)
while(True):
    try:
        print()
        resp = int(input("Voce vai jogar online? Digite 1 pra sim e 0 pra nao: "))
        if resp == 1 or resp == 0:
            break
        else:
            print("Opcao invalida, escolha outra.")
    except Exception:
        print("Opcao invalida, escolha outra.")

if resp:
    resp = int(input("Voce vai ser o servidor? Digite 1 pra sim e 0 pra nao: "))
    if resp:
        resp = int(input("Digite a porta (4 digitos): "))

        server_address = ('localhost', resp)
        sock.bind(server_address)

        sock.listen(1)

        print("Esperando Cliente!")
        connection, client_address = sock.accept()

        try:
            while True:
                data = int(connection.recv(32).decode())

                player, ult_peca = PECA1, PECA2

                pos_preenchidas[data - 1], voltar = jogar(matriz, pos_preenchidas[data - 1], data)

                contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, data - 1, pos_preenchidas[data - 1] + 1,
                                                a, contador_gameover, b, pos_preenchidas)

                coluna, ult_peca, player = escolheColuna(PECA1, PECA2)

                while coluna < 1 or coluna > COLUNA:
                    print("Coluna inexistente, escolha outra.")

                    coluna, ult_peca, player = escolheColuna(PECA1, PECA2)

                pos_preenchidas[coluna - 1], voltar = jogar(matriz, pos_preenchidas[coluna - 1], coluna)

                connection.send(str(coluna).encode())

                contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, coluna - 1,pos_preenchidas[coluna - 1] + 1, a, contador_gameover, b,pos_preenchidas)

        finally:
            connection.close()
    else:
        ip = input("Digite o IP do servidor com os pontos: ")
        porta = int(input("Digite a porta do servidor: "))

        sock = socket.create_connection((ip, porta))

        try:
            while True:
                coluna, ult_peca, player = escolheColuna(PECA1, PECA2)

                while coluna < 1 or coluna > COLUNA:
                    print("Coluna inexistente, escolha outra.")
                    coluna, ult_peca, player = escolheColuna(PECA1, PECA2)
                pos_preenchidas[coluna - 1], voltar = jogar(matriz, pos_preenchidas[coluna - 1], coluna)
                sock.send(str(coluna).encode())
                data = sock.recv(32).decode()

                contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, coluna - 1,
                                                pos_preenchidas[coluna - 1] + 1, a, contador_gameover, b,
                                                pos_preenchidas)

                data = int(data)

                player, ult_peca = PECA1, PECA2

                pos_preenchidas[data - 1], voltar = jogar(matriz, pos_preenchidas[data - 1], data)

                contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, data - 1, pos_preenchidas[data - 1] + 1,a, contador_gameover, b, pos_preenchidas)

        finally:
            sock.close()
else:
    while(True):
        try:
            print()
            IA = int(input("Deseja jogar com a IA ou com 2 players? Digite 1 para a IA e 2 para 2 players: "))
            if IA == 1 or IA == 2:
                break
            else:
                print()
                print("Opcao invalida, escolha outra.")
        except Exception:
            print()
            print("Opcao invalida, escolha outra.")
    while (True):
        if IA == 2:
            coluna, ult_peca, player = escolheColuna(player, ult_peca)
        else:
            coluna, ult_peca, player, voltar = escolheColuna_IA(player, ult_peca, voltar,coluna)
        while (True):
            if coluna < 1 or coluna > COLUNA:
                if (IA == 2) or (IA == 1 and player == PECA2):
                    print()
                    print("Coluna inexistente, escolha outra.")
                    voltar = True
                if IA == 2:
                    coluna, ult_peca, player = escolheColuna(player, ult_peca)
                else:
                    coluna, ult_peca, player, voltar = escolheColuna_IA(player, ult_peca, voltar, coluna)
            else:
                break
        pos_preenchidas[coluna - 1], voltar = jogar(matriz, pos_preenchidas[coluna - 1], coluna)
        fim_de_jogo(matriz, player, COLUNA, LINHA, coluna - 1, pos_preenchidas[coluna - 1] + 1,a, contador_gameover, b, pos_preenchidas)
