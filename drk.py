pos_preenchidas = []
PECA2 = " X "
PECA1 = " O "
VAZIA = " - "
matriz = []
linha = []
voltar = False
ult_peca = PECA2
player = PECA1 #Aqui o player começa recebendo " X "

def criarMatriz(matriz, linha):
    for i in range(LINHA):
        linha = []
        for j in range(COLUNA):
            linha.append(VAZIA)
        matriz.append(linha)
    return (matriz)

def escolheColuna(player, ult_peca):
    while True:
        if voltar == True:                                                                     #Aqui só entra se o usuário digitar uma coluna inválida
            if ult_peca == PECA1:
                player = PECA1
            if ult_peca == PECA2:
                player = PECA2
        if player == PECA1:                                                                    #Aqui entra quando o player é X, ou seja, na primeira rodada do jogo
            try:
                coluna = int(input("Player 1, escolha a coluna para seu próximo movimento: "))
                player = PECA2                                                                 #Aqui o player muda pra O
                ult_peca = PECA1                                                               #Aqui é a variável que indica se o último jogador foi X ou O
                break
            except ValueError:
                print("coluna invalida, escolha outra")
        else:                                                                                  #Aqui entra quando o player é O, ou seja, na segunda rodada do jogo
            try:
                coluna = int(input("Player 2, escolha a coluna para seu próximo movimento: "))
                player = PECA1                                                                 #Aqui o player muda pra X
                ult_peca = PECA2                                                                #Aqui é a variável que indica se o último jogador foi X ou O
                break
            except ValueError:
                print("coluna invalida, escolha outra")

    return coluna, ult_peca, player

def printar_matriz(LINHA, matriz):
    for i in range(LINHA):
        print(matriz[i])
def jogar(matriz, pos_preenchidas, coluna):
    if pos_preenchidas <0:
        print("Coluna cheia, escolha outra.")
        voltar = True
    elif matriz[pos_preenchidas][coluna-1]==VAZIA:
        matriz[pos_preenchidas][coluna - 1] = player
        printar_matriz(LINHA, matriz)
        voltar = False
        a = pos_preenchidas
        return a - 1,voltar
    return pos_preenchidas,voltar
def definir_linha():
    while(True):
        try:
            LINHA = int(input("Digite o numero desejado de linhas (sendo ele maior ou igual a 4): "))
            while (LINHA < 4):
                LINHA = int(input("Numero inválido de linhas, escolha outro (sendo ele maior ou igual a 4): "))
            break
        except ValueError:
            print("Numero inválido de linhas, escolha outro. ")
    return LINHA

def definir_coluna():
    while(True):
        try:
            COLUNA = int(input("Digite o numero desejado de colunas (sendo ele maior ou igual a 4): "))
            while (COLUNA < 4):
                COLUNA = int(input("Numero inválido de colunas, escolha outro (sendo ele maior ou igual a 4): "))
            break
        except ValueError:
                print("Numero inválido de colunas, escolha outro. ")
    return COLUNA

def fim_de_jogo(matriz, player, COLUNA, LINHA):
    contador_gameover = 0
    for i in range(LINHA):
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
    for t in range(COLUNA):
        for u in range(LINHA):
            if matriz[t][u] == player:
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

COLUNA = definir_coluna()
LINHA = definir_linha()
matriz = criarMatriz(matriz, linha)
for i in range(COLUNA):
    pos_preenchidas.append(LINHA-1)
while(True):
    coluna, ult_peca, player = escolheColuna(player, ult_peca)
    if coluna < 1 or coluna > COLUNA:
        print("Coluna inexistente, escolha outra.")
        voltar = True
    else:
        pos_preenchidas[coluna-1],voltar = jogar(matriz, pos_preenchidas[coluna-1],coluna)
    fim_de_jogo(matriz, player, COLUNA, LINHA)
