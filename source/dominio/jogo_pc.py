from .jogo import Jogo, Status

class JogoPC(Jogo):
    """
    Representa um jogo na plataforma PC.
    """
    def __init__(self, titulo, genero, ano_lancamento):
        super().__init__(titulo, genero, "PC", ano_lancamento)

    def to_dict(self):
        base = super().to_dict()
        return base  # PC não adiciona nada

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data["titulo"],
            data["genero"],
            data["ano_lancamento"]
        )
        obj._horas = data.get("horas", 0)
        obj._status = Status(data["status"])
        obj._avaliacao = data.get("avaliacao")
        return obj
