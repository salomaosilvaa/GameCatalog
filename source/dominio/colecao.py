from .jogo import Jogo

class Colecao:

    """
    Representa uma coleção nomeada que contém vários objetos Jogo.
    """
    
    def __init__(self, nome):
        self.nome = nome
        self._jogos = []

    #MÉTODOS:

    def adicionar(self, jogo: Jogo):
        if jogo in self._jogos:
            raise ValueError("Jogo duplicado na coleção (mesmo título e plataforma).")
        self._jogos.append(jogo)

    def remover(self, jogo: Jogo):
        if jogo not in self._jogos:
            raise ValueError("Jogo não encontrado na coleção.")
        self._jogos.remove(jogo)

    def listar(self):
        return list(self._jogos)
    
    #MÉTODOS ESPECIAIS:

    def __len__(self):
        return len(self._jogos)

    def __str__(self):
        return f"Coleção {self.nome} ({len(self._jogos)} jogos)"
