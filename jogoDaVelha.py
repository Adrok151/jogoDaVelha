def mostrarTabuleiro(tabuleiro):
    print('-----'*5)
    print('  1 2 3')
    for linha in range(3):
        for coluna in range(4): 
            print(tabuleiro[linha][coluna], end=' ')
        print('')
    print('-----'*5)

def checarVencedor(tabuleiro):
    conjunto = []

    #checar as diagonais
    if tabuleiro[0][1] == tabuleiro[1][2] == tabuleiro[2][3] != '-':
        return True
    elif tabuleiro[0][3] == tabuleiro[1][2] == tabuleiro[2][1] != '-':
        return True
    
    #checar as linhas
    for linha in range(3):
        if len(set(tabuleiro[linha])) == 1 and set(tabuleiro[linha]) != {'-'}:
            return True
        
    #checar as colunas
    for coluna in range(1, 4):
        for linha in range(3):
            conjunto.extend(tabuleiro[linha][coluna])
        if len(set(conjunto)) == 1 and set(conjunto) != {'-'}:
            return True
        conjunto = []

def tabuleiroCheio(tabuleiro):
    estaCheio = True
    for linha in range(3):
        for coluna in range(1, 4):
            if tabuleiro[linha][coluna] == '-':
                estaCheio = False
    return estaCheio

def iniciarJogo():
    tabuleiro = [
        ['1', '-', '-', '-'],
        ['2', '-', '-', '-'],
        ['3', '-', '-', '-']
    ]
    jogador = 'X'
    linha = 0
    coluna = 0
    jogoAcabou = False

    while jogoAcabou == False:
        mostrarTabuleiro(tabuleiro)
        try:
            #Um menos um foi adicionado ao input da variavel linha 
            #para tornar o jogo mais intuitivo para o jogador
            linha = int(input(f'Jogador {jogador}, qual linha você deseja marcar?(1 - 3) ')) - 1
            coluna = int(input(f'Jogador {jogador}, qual coluna você deseja marcar?(1 - 3) '))
            if linha not in range(3) or coluna not in range(1, 4) or tabuleiro[linha][coluna] != '-':
                print('Movimento inválido, favor digite apenas números inteiros de 1 a 3')
            else:
                tabuleiro[linha][coluna] = jogador
                if checarVencedor(tabuleiro):
                    mostrarTabuleiro(tabuleiro)
                    print(f'O jogador {jogador} venceu!')
                    jogoAcabou = True
                elif tabuleiroCheio(tabuleiro):
                    mostrarTabuleiro(tabuleiro)
                    print(f'O jogo terminou em um empate')
                    jogoAcabou = True
                elif jogador == 'X':
                    jogador = 'O'
                else:
                    jogador = 'X'
        except:
            print('Valor invalido, favor digite apenas números para as linhas e colunas.')

print("Vamos jogar um pouco!")
iniciarJogo()