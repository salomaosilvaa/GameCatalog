from .jogo import Jogo, Status

class JogoMobile(Jogo):
    """
    Representa um jogo da plataforma Mobile.
    """
    def __init__(self, titulo, genero, ano_lancamento, touch=True):
        super().__init__(titulo, genero, "Mobile", ano_lancamento)
        self.touch = touch

    def to_dict(self):
        base = super().to_dict()
        base["touch"] = self.touch
        return base

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data["titulo"],
            data["genero"],
            data["ano_lancamento"],
            data.get("touch", True)
        )
        obj._horas = data.get("horas", 0)
        obj._status = Status(data["status"])
        obj._avaliacao = data.get("avaliacao")
        return obj
