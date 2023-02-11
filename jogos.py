import forca
import adivinhacao
import velha

def menu():
    continuar=1
    while continuar:
        continuar = int(input("0. Sair \n"+
                              "1. Continuar Jogando\n"))
        if continuar:
            escolhe_jogo()
        else:
            print("Saindo...")

def escolhe_jogo():

    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3)Velha")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo == 3):
        print("Jogando da Velha")
        velha.jogar()

    menu()
    

if(__name__ == "__main__"):
    escolhe_jogo()
