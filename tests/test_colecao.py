from source.dominio.colecao import Colecao
from source.dominio.jogo import Jogo

def test_adicionar_e_listar():
    c = Colecao("Favoritos")
    j = Jogo("Hades", "Roguelike", "PC", "2020")

    c.adicionar(j)
    assert len(c) == 1
    assert c.listar()[0] == j
