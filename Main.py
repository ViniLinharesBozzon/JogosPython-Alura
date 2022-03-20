import AdivinhacaoAbsoluto
import forca
def menu_escolher():
    print("=================================")
    print("")
    print(" Bem vindo a central de jogos")
    print("")
    print("=================================")
    print("")
    # INICIO
    print("Escolha o jogo que queira jogar: ")
    print("[1] Adivinhação")
    print("[2] Forca")
    print("[3] Fechar o jogo")
    EscolhaJogo = int(input(""))
    print("=================================")
    if (EscolhaJogo == 1):
        AdivinhacaoAbsoluto.jogar_adivinhacao()
    elif(EscolhaJogo == 2):
        forca.jogar_forca()
    else:
        print("Fechando...")

if(__name__ == "__main__"):
    menu_escolher()