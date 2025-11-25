from .jogo import Jogo
class JogoConsole(Jogo):
    """
    Representa um jogo da plataforma Console.
    """
    def __init__(self, titulo, genero, ano_lancamento, modelo_console):
        super().__init__(titulo, genero, "Console", ano_lancamento)
        self.modelo_console = modelo_console