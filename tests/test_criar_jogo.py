from source.dominio.jogo import Jogo, Status

def test_criacao_jogo():
    j = Jogo("Hades", "Roguelike", "PC", "2020")
    assert j.titulo == "Hades"
    assert j.status == Status.NAO_INICIADO
    assert j.horas == 0
