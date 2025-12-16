class Cor:
    RESET = "\033[0m"

    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    CIANO = "\033[36m"

def colorir(texto, cor):
    return f"{cor}{texto}{Cor.RESET}"
