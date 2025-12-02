from .jogo import Jogo

class Colecao:
    """
    Representa uma coleção nomeada que contém vários objetos Jogo.
    """
    
    def __init__(self, nome, jogos=None):
        self.nome = nome
        self._jogos = jogos if jogos is not None else []

    # MÉTODOS:

    def adicionar(self, jogo: Jogo):
        if not isinstance(jogo, Jogo):
            raise ValueError("Apenas jogos podem ser adicionados.")
        if jogo in self._jogos:
            raise ValueError("Jogo duplicado na coleção (mesmo título e plataforma).")
        self._jogos.append(jogo)
        jogo.colecao = self

    def remover(self, jogo: Jogo):
        if jogo not in self._jogos:
            raise ValueError("Jogo não encontrado na coleção.")
        self._jogos.remove(jogo)
        jogo.colecao = None

    def listar(self):
        return list(self._jogos)

    # PERSISTÊNCIA JSON:

    def to_dict(self):
        return {
            "nome": self.nome,
            "jogos": [jogo.to_dict() for jogo in self._jogos]
        }

    @classmethod
    def from_dict(cls, data):
        nome = data["nome"]
        jogos_data = data.get("jogos", [])
        colecao = cls(nome)
        for jogo_dict in jogos_data:
            jogo = Jogo.from_dict(jogo_dict)
            colecao.adicionar(jogo)  # já cria o vínculo reverso
        return colecao

    # MÉTODOS ESPECIAIS:

    def __len__(self):
        return len(self._jogos)

    def __str__(self):
        return f"Coleção {self.nome} ({len(self._jogos)} jogos)"
