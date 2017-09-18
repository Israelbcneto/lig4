import socket
import sys

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

def criarMatriz(matriz, linha):
    for i in range(LINHA):
        linha = []
        for j in range(COLUNA):
            linha.append(VAZIA)
        matriz.append(linha)
    return (matriz)

def jogar(matriz, pos_preenchidas, coluna):
    if pos_preenchidas < 0:
        print("Coluna cheia, escolha outra.")
        voltar = True
    elif matriz[pos_preenchidas][coluna - 1] == VAZIA:
        matriz[pos_preenchidas][coluna - 1] = player
        printar_matriz(LINHA, matriz)
        voltar = False
    else:
        voltar = False
    return pos_preenchidas - 1, voltar

def printar_matriz(LINHA, matriz):
    for i in range(LINHA):
        print(matriz[i])

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
            
COLUNA = definir_coluna()
LINHA = definir_linha()
matriz = criarMatriz(matriz, linha)
for i in range(COLUNA):
    pos_preenchidas.append(LINHA - 1)
printar_matriz(LINHA, matriz)

resp = int(input("Voce vai jogar online? Digite 1 pra sim e 0 pra nao: "))

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

                contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, data-1, pos_preenchidas[data - 1]+1,a,contador_gameover,b,pos_preenchidas)


                coluna, ult_peca, player = escolheColuna(PECA1, PECA2)

                while coluna < 1 or coluna > COLUNA:
                    print("Coluna inexistente, escolha outra.")

                    coluna, ult_peca, player = escolheColuna(PECA1, PECA2)

                pos_preenchidas[coluna - 1], voltar = jogar(matriz, pos_preenchidas[coluna - 1], coluna)

                connection.send(str(coluna).encode())

                contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, coluna-1, pos_preenchidas[coluna - 1]+1,a,contador_gameover,b,pos_preenchidas)

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

                contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, coluna-1, pos_preenchidas[coluna - 1]+1,a,contador_gameover,b,pos_preenchidas)

                data = int(data)

                player, ult_peca = PECA1, PECA2

                pos_preenchidas[data - 1], voltar = jogar(matriz, pos_preenchidas[data - 1], data)

                contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, data-1, pos_preenchidas[data - 1]+1,a,contador_gameover,b,pos_preenchidas)

        finally:
            sock.close()
else:
    while (True):
        coluna, ult_peca, player = escolheColuna(player, ult_peca)
        if coluna < 1 or coluna > COLUNA:
            print("Coluna inexistente, escolha outra.")
            voltar = True
        else:
            pos_preenchidas[coluna - 1], voltar = jogar(matriz, pos_preenchidas[coluna - 1], coluna)
            contador_gameover = fim_de_jogo(matriz, player, COLUNA, LINHA, coluna-1, pos_preenchidas[coluna - 1]+1,a,contador_gameover,b,pos_preenchidas)
