from .jogo import Jogo
class JogoPC(Jogo):
    """
    Representa um jogo na plataforma PC.
    """
    def __init__(self, titulo, genero, ano_lancamento):
        super().__init__(titulo, genero, "PC", ano_lancamento)