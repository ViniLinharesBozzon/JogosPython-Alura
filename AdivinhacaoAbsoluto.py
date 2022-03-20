import random

def jogar_adivinhacao():
    print("=================================")
    print("Bem vindo ao jogo de Adivinhação")
    print("=================================")
    print("")
    Chutes = 0
    # Menu
    print("Qual a dificuldade que voce deseja ?:")
    print("[1] Fácil")
    print("[2] Médio")
    print("[3] Difícil")
    print("")

    Pontos = 1000
    nivel = int(input(""))

    if (nivel == 1):
        Chutes = 20
    elif(nivel == 2):
        Chutes = 10
    else:
        Chutes = 5

    Max_Chute = Chutes
    Numero_Secreto = random.randrange(1,101)
    print("=================================")
    for Chutes in range(1,Chutes + 1,1):
        print("Voce está usando a {} º tentativa de {}".format(Chutes, Max_Chute))
        print("")


        Tentativa = int(input("Digite o seu número (1 até 100): "))
        print("Voce digitou o valor:", Tentativa)
        print("Verificando")
        if (Tentativa < 1):
            print("Esse valor é menor que o limite")
            print("Os valores aceitos são entre 1 e 100")
            print("=================================")
            continue
        elif (Tentativa > 100):
            print("Esse valor é maior que o limite")
            print("Os valores aceitos são entre 1 e 100")
            print("=================================")
            continue
        Numero = int(Tentativa)
        Acertou = Numero_Secreto == Numero
        if (Acertou):
            print("Voce acertou !")
            print("Parabens !!!!!!")
            print("=================================")
            print("")
            break
        else:
            print("Voce errou !")
            print("")
            print("Dica !")
            if (Numero > Numero_Secreto):
                print("Voce passou do valor secreto")
                print("=================================")
            elif(Numero < Numero_Secreto):
                print("Voce não passou perto do valor secreto")
                print("=================================")
            Pontos_Perdidos = Numero_Secreto - Tentativa
            Pontos = Pontos - abs(Pontos_Perdidos)
    print("\t\t Fim do Jogo !")
    print("")
    print("=================================")
    print("Voce pontuou:  {}".format(Pontos))

if(__name__ == "__main__"):
    jogar_adivinhacao()