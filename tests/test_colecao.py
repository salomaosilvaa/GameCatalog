import pytest
from source.dominio.jogo import Jogo
from source.dominio.colecao import Colecao

def test_adicionar_jogo():
    c = Colecao("Teste")
    j = Jogo("Doom", "FPS", "PC")
    c.adicionar(j)
    assert len(c) == 1
    assert j in c.listar()

def test_nao_permite_duplicados():
    c = Colecao("Teste")
    j1 = Jogo("Doom", "FPS", "PC")
    j2 = Jogo("Doom", "FPS", "PC")
    c.adicionar(j1)
    with pytest.raises(ValueError):
        c.adicionar(j2)

def test_remover_jogo():
    c = Colecao("Teste")
    j = Jogo("Celeste", "Plataforma", "PC")
    c.adicionar(j)
    c.remover(j)
    assert len(c) == 0
