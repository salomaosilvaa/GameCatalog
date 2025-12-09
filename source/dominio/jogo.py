from enum import Enum

class Status(Enum):
    NAO_INICIADO = "NAO_INICIADO"
    JOGANDO = "JOGANDO"
    FINALIZADO = "FINALIZADO"


class Jogo:
    """
    Classe base para jogos do catálogo.
    """
    def __init__(self, titulo, genero, plataforma, ano_lancamento=None, status=None):
        self.titulo = titulo.strip()
        self.genero = genero.strip()
        self.plataforma = plataforma.strip()
        self.ano_lancamento = str(ano_lancamento) if ano_lancamento else None

        self._horas = 0.0

        if status is None:
            self._status = Status.NAO_INICIADO
        else:
            if not isinstance(status, Status):
                raise ValueError("Status inválido.")
            self._status = status

        self._avaliacao = None

    # PROPRIEDADES
    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):
        if valor < 0:
            raise ValueError("Não é possível creditar horas negativas.")
        if valor < self._horas:
            raise ValueError("Não é possível reduzir horas jogadas.")
        self._horas = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        if not isinstance(novo_status, Status):
            raise ValueError("Status inválido.")
        if self._status == Status.FINALIZADO and novo_status != Status.FINALIZADO:
            raise ValueError("Não é possível alterar o status após a finalização.")
        self._status = novo_status

    @property
    def avaliacao(self):
        return self._avaliacao

    @avaliacao.setter
    def avaliacao(self, nota):
        if nota is not None:
            if not isinstance(nota, int) or not (0 <= nota <= 10):
                raise ValueError("A nota deve ser um INTEIRO entre 0 e 10.")
            if self._status != Status.FINALIZADO:
                raise ValueError("Você ainda NÃO FINALIZOU o jogo. Não pode avaliar.")
        self._avaliacao = nota

    # MÉTODOS
    def adicionar_horas(self, qtd):
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
            "tipo": "Jogo",
            "titulo": self.titulo,
            "genero": self.genero,
            "plataforma": self.plataforma,
            "ano_lancamento": self.ano_lancamento,
            "horas": self._horas,
            "status": self._status.value,
            "avaliacao": self._avaliacao,
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            data["titulo"],
            data["genero"],
            data["plataforma"],
            data.get("ano_lancamento"),
            status=Status(data["status"])
        )
        obj._horas = data.get("horas", 0)
        obj._avaliacao = data.get("avaliacao")
        return obj

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


