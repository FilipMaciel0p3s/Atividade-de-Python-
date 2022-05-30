import forca
import Advinhacao
import forca

def escolha_jogo():
    print("*******************************")
    print("Bem-vindo! escolha seu jogo")
    print("*******************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        Advinhacao.jogar()

if (__name__ == "__main__"):
    escolha_jogo()