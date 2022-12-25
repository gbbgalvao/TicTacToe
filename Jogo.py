tabuleiro = ['-','-','-', 
            '-','-','-', 
            '-','-','-']
Jogador = 'X'
Vencedor = None
Continua = True

def velha(tabuleiro):
    print(tabuleiro[0], ' | ', tabuleiro[1], ' | ', tabuleiro[2])
    print('- - - - - - - -')
    print(tabuleiro[3], ' | ', tabuleiro[4], ' | ', tabuleiro[5])
    print('- - - - - - - -')
    print(tabuleiro[6], ' | ', tabuleiro[7], ' | ', tabuleiro[8])
    print ('\n')
print(velha(tabuleiro))

def VezJogador(tabuleiro):
    print (f'A vez é do jogador: {Jogador}\n')
    entrada = int(input('Escolha um número de 1 a 9: '))
    if (entrada>=1 and entrada<=9 and tabuleiro[entrada-1] == '-'):
        tabuleiro[entrada-1] = Jogador
    else:
        print('Posição inválida!')

def Horizontal(tabuleiro):
    global Vencedor
    if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] and tabuleiro[1]!= '-'):
        Vencedor=tabuleiro[0]
        return True
    elif (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] and tabuleiro[3]!= '-'):
        Vencedor=tabuleiro[3]
        return True
    elif (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] and tabuleiro[6]!= '-'):
        Vencedor=tabuleiro[6]
        return True

def Vertical(tabuleiro):
    global Vencedor
    if (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] and tabuleiro[0]!= '-'):
        Vencedor=tabuleiro[0]
        return True
    elif (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] and tabuleiro[1]!= '-'):
        Vencedor=tabuleiro[1]
        return True
    elif (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] and tabuleiro[2]!= '-'):
        Vencedor=tabuleiro[2]
        return True

def Diagonal(tabuleiro):
    global Vencedor
    if (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] and tabuleiro[0]!= '-'):
        Vencedor=tabuleiro[0]
        return True
    elif (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] and tabuleiro[2]!= '-'):
        Vencedor=tabuleiro[3]
        return True

def Empate(tabuleiro):
    global Continua
    if '-' not in tabuleiro:
        velha(tabuleiro)
        print('Empate!')
        Continua = False

def VerificarVitoria():
    global Continua
    if (Diagonal(tabuleiro) or Vertical(tabuleiro) or Horizontal(tabuleiro)):
        Continua = False
        velha(tabuleiro)
        print(f'O vencedor é o {Vencedor}')

def TrocarJogador():
    global Jogador
    if Jogador == 'X':
        Jogador = 'O'
    else:
        Jogador = 'X'

while Continua:
    velha(tabuleiro)
    VezJogador(tabuleiro)
    VerificarVitoria()
    Empate(tabuleiro)
    TrocarJogador()  