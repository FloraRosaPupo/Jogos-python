import adivinhacao
import forca
import velha

def escolhe_jogo():
    jogos={'1':forca.jogar,'2':adivinhacao.jogar,'3':velha.jogar}
    while True:
        opcao=input('0. Sair | 1. Forca | 2. Adivinhação | 3. Velha: ').strip()
        if opcao=='0': return
        jogo=jogos.get(opcao)
        if jogo is None:
            print('Opção inválida.')
            continue
        jogo()

def menu():
    escolhe_jogo()

if __name__=='__main__': escolhe_jogo()
