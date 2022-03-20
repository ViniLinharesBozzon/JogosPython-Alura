import random
def jogar_forca():
    bem_vindo()
    palavra_secreta = decidepalavrasecreta()
    ListaAcertada = palavrazerada(palavra_secreta)
    Enforcou = False
    Acertou = False
    Erros = 0
    print(ListaAcertada)
    print("")
    while(not Enforcou and not Acertou):
        Tentativa = pede_chute()

        if(Tentativa in palavra_secreta):
            marca_posicao_certo(Tentativa,ListaAcertada,palavra_secreta)
        else:
            Erros += 1
            desenha_forca(Erros)
        print(ListaAcertada)
        Enforcou = Erros == 7
        Acertou = "_" not in ListaAcertada


    if(Acertou):
        textoVitoria()
    else:
        textoDerrota()
        print("A palavra era: {}".format(palavra_secreta))

    print("=================================")
    print("")
    print("\t\t Fim do Jogo !")
    print("")
    print("=================================")



def bem_vindo():
    print("=================================")
    print("\n\tBem vindo ao jogo de forca\n")
    print("=================================\n")

def decidepalavrasecreta():
    Arquivo = open("palavras.txt", "r")
    ListaPalavras = []
    for linha in Arquivo:
        linha = linha.strip()
        ListaPalavras.append(linha)
    Arquivo.close()
    numero = random.randrange(0, len(ListaPalavras))
    palavra_secreta = ListaPalavras[numero]
    palavra_secreta = palavra_secreta.upper()
    return palavra_secreta

def pede_chute():
    Tentativa = input("Qual letra ?")
    Tentativa = Tentativa.strip().upper()
    return Tentativa

def palavrazerada(palavra):
    lista = ["_" for letra in palavra]
    return lista

def marca_posicao_certo(Tentativa,ListaAcertada,palavra_secreta):
    cont = 0
    for letra in palavra_secreta:
        if (Tentativa.upper() == letra.upper()):
            ListaAcertada[cont] = Tentativa
        cont += 1

def textoVitoria():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\ :      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \[::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def textoDerrota():
        print("Puxa, você foi enforcado!")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

if(__name__ == "__main__"):
    jogar_forca()
