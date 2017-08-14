pos_preenchidas = []
PECA2 = " X "
PECA1 = " O "
VAZIA = " - "
matriz = []
linha = []
voltar = False
ultPeca = PECA2
player = PECA1 #Aqui o player começa recebendo " X "

def criarMatriz(matriz, linha):
    for i in range(LINHA):
        linha = []
        for j in range(COLUNA):
            linha.append(VAZIA)
        matriz.append(linha)
    return (matriz)

def escolheColuna(player,ultPeca):
    if voltar == True:                      #Aqui só entra se o usuário digitar uma coluna inválida
        if ultPeca == PECA1:
            player = PECA1
        if ultPeca == PECA2:
            player = PECA2
    if player == PECA1:                                                                    #Aqui entra quando o player é X, ou seja, na primeira rodada do jogo
            coluna = int(input("Player 1, escolha a coluna para seu próximo movimento: "))
            player = PECA2                                                                 #Aqui o player muda pra O
            ultPeca = PECA1                                                                #Aqui é a variável que indica se o último jogador foi X ou O
    else:                                                                                  #Aqui entra quando o player é O, ou seja, na segunda rodada do jogo
            coluna = int(input("Player 2, escolha a coluna para seu próximo movimento: "))
            player = PECA1                                                                 #Aqui o player muda pra X
            ultPeca = PECA2                                                                #Aqui é a variável que indica se o último jogador foi X ou O
    return coluna, ultPeca, player

def printar_matriz(LINHA, matriz):
    for i in range(LINHA):
        print(matriz[i])

def jogar(matriz, pos_preenchidas, coluna):
    matriz = criarMatriz(matriz, linha)
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
            LINHA = int(input("Digite o numero desejado de linhas: "))
            while (LINHA <1):
                LINHA = int(input("Numero incorreto de linhas, escolha outro: "))
            break
        except ValueError:
            print("Numero incorreto de linhas, escolha outro. ")
    return LINHA

def definir_coluna():
    while(True):
        try:
            COLUNA = int(input("Digite o numero desejado de colunas: "))
            while (COLUNA <1):
                COLUNA = int(input("Numero incorreto de colunas, escolha outro: "))
            break
        except ValueError:
                print("Numero incorreto de colunas, escolha outro. ")
    return COLUNA

COLUNA = definir_coluna()
LINHA = definir_linha()

for i in range(COLUNA):
    pos_preenchidas.append(LINHA-1)

while(True):
    coluna,ultPeca,player = escolheColuna(player,ultPeca)
    if coluna < 1 or coluna > COLUNA:
        print("Coluna inexistente, escolha outra.")
        voltar = True
    else:
        pos_preenchidas[coluna-1],voltar = jogar(matriz, pos_preenchidas[coluna-1],coluna)
