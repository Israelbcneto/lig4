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


def printar_matriz(LINHA, matriz):
    for i in range(LINHA):
        print(matriz[i])


def jogar(matriz, pos_preenchidas, coluna):
    if pos_preenchidas < 0:
        print("Coluna cheia, escolha outra.")
        voltar = True
    elif matriz[pos_preenchidas][coluna-1] == VAZIA:
        matriz[pos_preenchidas][coluna-1] = player
        printar_matriz(LINHA, matriz)
        voltar = False
        a = pos_preenchidas
        return a - 1, voltar
    return pos_preenchidas, voltar


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


def LINHA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover,b,preenchimento):
    contador_gameover = 0
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
def COLUNA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover,b,preenchimento):
    contador_gameover = 0
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

def diagonalIDSE(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover,b,preenchimento,c):
    c = 0
    contador_gameover = 0
    try:                                                                 #INFERIOR DIREITA
        while contador_gameover < 3:
            pos_preenchidas += 1
            coluna += 1
            a += 1
            if matriz[pos_preenchidas][coluna] == player:
                contador_gameover += 1
            else:
                break
    except Exception:
        pass
    pos_preenchidas -= a
    coluna -= a
    try:                                                                 #superior esquerda
        while contador_gameover < 3:
            pos_preenchidas -= 1
            coluna -= 1
            c += 1
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
    contador_gameover = 0
    pos_preenchidas += c
    coluna += c
def diagonalSDIE(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover,b,preenchimento):
    contador_gameover = 0
    try:
        while contador_gameover < 3:
            pos_preenchidas -= 1                        #diagonal superior direita
            coluna += 1
            b += 1
            if matriz[pos_preenchidas][coluna] == player and pos_preenchidas >= 0:
                contador_gameover += 1

            else:
                break
    except Exception:
        pass
    coluna -= b
    pos_preenchidas += b
    try:
        while contador_gameover < 3:                        #diagonal inferior esquerda
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
            print("Player 1 ganhou o jogo!")
        else:
            print("Player 2 ganhou o jogo!")
        quit()
def EMPATE(COLUNA, preenchimento):
    cont = 0
    for i in preenchimento:
        if i < 0:
            cont += 1
        if cont == COLUNA:
            print("Empatou!!")
            quit()
    return contador_gameover
def fim_de_jogo(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas,contador_gameover,preenchimento):
    contador_gameover = 0
    a = 0
    b = 0
    c = 0
    LINHA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover, b, pos_preenchidas)
    COLUNA(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover, b, pos_preenchidas)
    diagonalIDSE(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover, b, pos_preenchidas, c)
    diagonalSDIE(matriz, player, COLUNA, LINHA, coluna, pos_preenchidas, a,contador_gameover, b, pos_preenchidas)
    EMPATE(COLUNA, preenchimento)

COLUNA = definir_coluna()
LINHA = definir_linha()
matriz = criarMatriz(matriz, linha)
for i in range(COLUNA):
    pos_preenchidas.append(LINHA - 1)
printar_matriz(LINHA, matriz)
while (True):
    coluna, ult_peca, player = escolheColuna(player, ult_peca)
    if coluna < 1 or coluna > COLUNA:
        print("Coluna inexistente, escolha outra.")
        voltar = True
    else:
        pos_preenchidas[coluna - 1], voltar = jogar(matriz, pos_preenchidas[coluna - 1], coluna)
        fim_de_jogo(matriz, player, COLUNA, LINHA, coluna-1, pos_preenchidas[coluna - 1]+1, contador_gameover, pos_preenchidas)
