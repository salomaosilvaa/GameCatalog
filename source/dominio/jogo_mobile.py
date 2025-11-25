from .jogo import Jogo
class JogoMobile(Jogo):
    """
    Representa um jogo da plataforma Mobile.
    """
    def __init__(self, titulo, genero, ano_lancamento, touch):
        super().__init__(titulo, genero, "Mobile", ano_lancamento)
        self.touch = True