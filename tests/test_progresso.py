from source.dominio.jogo import Jogo, Status
import pytest

def test_adicionar_horas():
    j = Jogo("Hades", "Roguelike", "PC", "2020")
    j.adicionar_horas(2)
    assert j.horas == 2
    assert j.status == Status.JOGANDO

def test_tentar_finalizar_sem_1_hora():
    j = Jogo("Hades", "Roguelike", "PC", "2020")
    with pytest.raises(ValueError):
        j.finalizar()
