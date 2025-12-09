import pytest
from source.dominio.jogo import Jogo
from source.dominio.colecao import Colecao

def test_ordenar_titulo():
    c = Colecao("Ordenação")
    c.adicionar(Jogo("Zelda", "Aventura", "Switch"))
    c.adicionar(Jogo("Dark Souls", "RPG", "PC"))
    c.adicionar(Jogo("Hollow Knight", "Metroidvania", "PC"))

    ordenado = c.ordenar_por("titulo")
    assert [j.titulo for j in ordenado] == ["Dark Souls", "Hollow Knight", "Zelda"]

def test_ordenar_genero():
    c = Colecao("Ordenação")
    c.adicionar(Jogo("Zelda", "Aventura", "Switch"))
    c.adicionar(Jogo("Dark Souls", "RPG", "PC"))
    c.adicionar(Jogo("Hollow Knight", "Metroidvania", "PC"))

    ordenado = c.ordenar_por("genero")
    assert [j.genero for j in ordenado] == ["Aventura", "Metroidvania", "RPG"]

def test_ordenar_invalido():
    c = Colecao("Ordenação")
    with pytest.raises(ValueError):
        c.ordenar_por("inexistente")
