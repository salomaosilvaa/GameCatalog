import pytest
from source.dominio.jogo import Jogo, Status

def test_criacao_jogo():
    jogo = Jogo("Dark Souls", "RPG", "PC")
    assert jogo.titulo == "Dark Souls"
    assert jogo.genero == "RPG"
    assert jogo.plataforma == "PC"
    assert jogo.status == Status.NAO_INICIADO

def test_status_alterado():
    jogo = Jogo("Hades", "Roguelike", "Switch")
    jogo.status = Status.JOGANDO
    assert jogo.status == Status.JOGANDO

def test_to_dict():
    jogo = Jogo("Hades", "Roguelike", "Switch")
    data = jogo.to_dict()
    assert data["titulo"] == "Hades"
    assert data["genero"] == "Roguelike"
    assert data["plataforma"] == "Switch"
    assert data["status"] == "NAO_INICIADO"

def test_from_dict():
    data = {
        "titulo": "Hades",
        "genero": "Roguelike",
        "plataforma": "Switch",
        "status": "JOGANDO"
    }
    jogo = Jogo.from_dict(data)
    assert jogo.status == Status.JOGANDO

