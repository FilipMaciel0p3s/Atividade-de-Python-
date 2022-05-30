import random
def jogar():

    print("*******************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*******************************")

    numero_aleatorio = random.randrange(1,101)
    rodada = 1
    pontos = 1000

    print("Qual o nivel? ")
    print("(1) Facil (2)Médio (3) difícil")
    nivel = int(input("Qual nivel deseja jogar? "))

    if(nivel == 1):
        numero_de_chances = 20
    elif(nivel == 2):
        numero_de_chances = 10
    else:
        numero_de_chances = 3

    for rodada in range(1, numero_de_chances + 1):
        print("tentativa {} de {}" .format(rodada, numero_de_chances))



        chute_strg = input("Digite a sua resposta(1 a 100): ")
        chute =int(chute_strg)

        if (chute < 1 or chute > 100):
            print("Apenas numeros entre 1 a 100 são validos")
            continue
        acerto = chute == numero_aleatorio
        maior =  chute > numero_aleatorio
        menor =  chute < numero_aleatorio

        if(acerto):
            print ("Tu acertou!! sua pontuação foi:{}" .format(pontos))
            break
        else:
            if(maior):
                print("Esta errado! Sua resposta foi maior que o numero procurado")

            elif(menor):
                print("Esta errado! Sua resposta foi menor que o numero procurado")


            pontos_perdidos = abs(numero_aleatorio - chute)
            pontos = pontos - pontos_perdidos

if (__name__ == "__main__"):
    jogar()