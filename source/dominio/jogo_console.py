from .jogo import Jogo, Status

class JogoConsole(Jogo):
    """
    Representa um jogo da plataforma Console.
    """
    def __init__(self, titulo, genero, ano_lancamento, modelo_console):
        super().__init__(titulo, genero, "Console", ano_lancamento)
        self.modelo_console = modelo_console

    def to_dict(self):
        base = super().to_dict()
        base["modelo_console"] = self.modelo_console
        return base

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data["titulo"],
            data["genero"],
            data["ano_lancamento"],
            data["modelo_console"]
        )
        obj._horas = data.get("horas", 0)
        obj._status = Status(data["status"])
        obj._avaliacao = data.get("avaliacao")
        return obj
