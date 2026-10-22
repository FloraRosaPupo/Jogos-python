"""Jogo da velha com validação de jogadas e detecção de empate."""
board = [[0]*3 for _ in range(3)]

def vencedor(tabuleiro):
    linhas = list(tabuleiro) + [list(coluna) for coluna in zip(*tabuleiro)]
    linhas += [[tabuleiro[i][i] for i in range(3)], [tabuleiro[i][2-i] for i in range(3)]]
    for linha in linhas:
        if linha[0] != 0 and all(valor==linha[0] for valor in linha):
            return linha[0]
    return 0

def ganhou():
    return int(vencedor(board)!=0)

def jogar():
    global board
    board = [[0]*3 for _ in range(3)]
    jogadas = 0
    while jogadas<9 and not ganhou():
        exibe()
        print("Jogador", jogadas%2+1)
        try:
            linha=int(input("Linha (1-3): "))-1
            coluna=int(input("Coluna (1-3): "))-1
        except ValueError:
            print("Informe números de 1 a 3.")
            continue
        if not (0<=linha<3 and 0<=coluna<3):
            print("Posição fora do tabuleiro.")
            continue
        if board[linha][coluna]!=0:
            print("Posição ocupada.")
            continue
        board[linha][coluna]=1 if jogadas%2==0 else -1
        jogadas+=1
    exibe()
    print("Empate!" if not ganhou() else f"Jogador {(jogadas-1)%2+1} ganhou!")

def exibe():
    for linha in board:
        print(' '.join({0:'_',1:'X',-1:'O'}[valor] for valor in linha))

if __name__=='__main__': jogar()
