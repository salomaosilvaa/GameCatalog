import pytest
from source.dominio.jogo import Jogo, Status
from source.dominio.colecao import Colecao

def criar_colecao_teste():
    c = Colecao("Testes")
    c.adicionar(Jogo("Dark Souls", "RPG", "PC"))
    c.adicionar(Jogo("Hades", "Roguelike", "Switch"))
    c.adicionar(Jogo("Celeste", "Plataforma", "PC", status=Status.JOGANDO))
    return c

def test_filtrar_genero():
    c = criar_colecao_teste()
    rpgs = c.filtrar(genero="RPG")
    assert len(rpgs) == 1
    assert rpgs[0].titulo == "Dark Souls"

def test_filtrar_plataforma():
    c = criar_colecao_teste()
    pc = c.filtrar(plataforma="PC")
    assert len(pc) == 2

def test_filtrar_status():
    c = criar_colecao_teste()
    andamento = c.filtrar(status="JOGANDO")
    assert len(andamento) == 1
    assert andamento[0].titulo == "Celeste"
