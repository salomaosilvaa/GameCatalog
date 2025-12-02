from enum import Enum

class Status(Enum):
    NAO_INICIADO = "NÃO INICIADO"
    JOGANDO = "JOGANDO"
    FINALIZADO = "FINALIZADO"


class Jogo:
    """
    Classe base para jogos do catálogo.
    Atributos comuns e comportamentos gerais dos jogos.
    """

    def __init__(self, titulo, genero, plataforma, ano_lancamento):
        self.titulo = titulo.strip()
        self.genero = genero.strip()
        self.plataforma = plataforma.strip()

        self._horas = 0.0
        self._status = Status.NAO_INICIADO
        self._avaliacao = None
        self.ano_lancamento = ano_lancamento.strip()

    # PROPRIEDADES:

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor: float):
        if valor < 0:
            raise ValueError("Não é possível creditar horas negativas.")
        self._horas = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status: Status):
        if not isinstance(novo_status, Status):
            raise ValueError("Status Inválido.")
        self._status = novo_status

    @property
    def avaliacao(self):
        return self._avaliacao

    @avaliacao.setter
    def avaliacao(self, nota: int):
        if nota is not None:
            if not isinstance(nota, int) or not (0 <= nota <= 10):
                raise ValueError("A nota deve ser um INTEIRO entre 0 e 10.")
            if self._status != Status.FINALIZADO:
                raise ValueError("Você ainda NÃO FINALIZOU o jogo. Não pode avaliar.")
        self._avaliacao = nota

    # MÉTODOS:

    def adicionar_horas(self, qtd: float):
        if qtd < 0:
            raise ValueError("Não é possível adicionar horas negativas.")
        self._horas += qtd

        if self._horas > 0 and self._status == Status.NAO_INICIADO:
            self.status = Status.JOGANDO

    def finalizar(self):
        if self._horas < 1:
            raise ValueError("Não é possível finalizar um jogo com menos de 1 hora.")
        self.status = Status.FINALIZADO

    def reiniciar(self):
        self._horas = 0
        self.status = Status.JOGANDO

    # SERIALIZAÇÃO

    def to_dict(self):
        return {
            "tipo": self.plataforma,
            "titulo": self.titulo,
            "genero": self.genero,
            "ano_lancamento": self.ano_lancamento,
            "horas": self._horas,
            "status": self._status.value,
            "avaliacao": self._avaliacao
    }


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

    # MÉTODOS ESPECIAIS:

    def __str__(self):
        return f"{self.titulo} ({self.plataforma}) - {self.status.value}"

    def __repr__(self):
        return (
            f"Jogo(titulo={self.titulo!r}, genero={self.genero!r}, "
            f"plataforma={self.plataforma!r}, horas={self._horas}, "
            f"status={self._status}, avaliacao={self._avaliacao}, "
            f"ano={self.ano_lancamento})"
        )

    def __eq__(self, other):
        if not isinstance(other, Jogo):
            return False
        return (self.titulo.lower(), self.plataforma.lower()) == \
               (other.titulo.lower(), other.plataforma.lower())

    def __lt__(self, other):
        if not isinstance(other, Jogo):
            return NotImplemented
        return self.horas < other.horas

