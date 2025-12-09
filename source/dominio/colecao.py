from .jogo import Jogo, Status
from source.dados.repositorio_json import salvar_jogos, carregar_jogos
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
    
    def salvar(self, caminho ="source/dados/jogos.json"):
        salvar_jogos(self._jogos, caminho)
    
    def filtrar(self, genero = None, status = None, plataforma = None):
        jogos = self._jogos

        if genero:
            jogos = [j for j in jogos if j.genero.lower() == genero.lower()]

        if status:
            if isinstance(status, str):
                try:
                    status = Status[status.upper()]
                except KeyError:
                    raise ValueError(f"Status inválido: {status}")
            jogos = [j for j in jogos if j.status == status]

        if plataforma:
            jogos = [j for j in jogos if j.plataforma.lower() == plataforma.lower()]

        return jogos

    def ordenar_por(self, campo: str, reverso=False):
        campo = campo.lower().strip()

        regras = {
            "titulo": lambda j: j.titulo.lower(),
            "genero": lambda j: j.genero.lower(),
            "plataforma": lambda j: j.plataforma.lower(),
            "ano": lambda j: int(j.ano_lancamento),
            "horas": lambda j: j.horas,
            "avaliacao": lambda j: j.avaliacao if j.avaliacao is not None else -1,

            "status": lambda j: {
                Status.NAO_INICIADO: 0,
                Status.JOGANDO: 1,
                Status.FINALIZADO: 2
            }[j.status]
        }

        if campo not in regras:
            raise ValueError(f"Campo inválido para ordenação: {campo}")

        return sorted(self._jogos, key=regras[campo], reverse=reverso)


    @classmethod
    def carregar(cls, caminho = "source/dados/jogos.json"):
        jogos = carregar_jogos(caminho)
        colecao = cls("Minha coleção")
        for j in jogos:
            colecao.adicionar(j)
        return colecao

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
            colecao.adicionar(jogo)
        return colecao

    # MÉTODOS ESPECIAIS:

    def __len__(self):
        return len(self._jogos)

    def __str__(self):
        return f"Coleção {self.nome} ({len(self._jogos)} jogos)"
