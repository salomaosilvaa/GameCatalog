import pytest
from source.dominio.jogo import Jogo, Status
from source.dominio.colecao import Colecao
from source.dados.relatorios import (
    top_5_por_horas,
    media_horas,
    media_avaliacoes,
    percentual_por_status,
    relatorio_texto
)

@pytest.fixture
def colecao_com_jogos():
    c = Colecao("Relatórios")

    j1 = Jogo("Jogo A", "RPG", "PC", 2020)
    j1.adicionar_horas(10)
    j1.finalizar()
    j1.avaliacao = 8

    j2 = Jogo("Jogo B", "Ação", "Console", 2019)
    j2.adicionar_horas(5)

    j3 = Jogo("Jogo C", "Puzzle", "Mobile", 2021)
    j3.adicionar_horas(20)
    j3.finalizar()
    j3.avaliacao = 9

    j4 = Jogo("Jogo D", "RPG", "PC", 2018)
    j4.adicionar_horas(2)

    j5 = Jogo("Jogo E", "RPG", "PC", 2017)
    j5.adicionar_horas(15)

    j6 = Jogo("Jogo F", "RPG", "PC", 2022)  # sem horas

    for j in [j1, j2, j3, j4, j5, j6]:
        c.adicionar(j)

    return c

def test_top_5_por_horas(colecao_com_jogos):
    top5 = top_5_por_horas(colecao_com_jogos)

    assert len(top5) == 5
    assert top5[0].horas == 20
    assert top5[1].horas == 15
    assert top5[2].horas == 10

def test_media_horas(colecao_com_jogos):
    media = media_horas(colecao_com_jogos)

    assert media == 10.4

def test_media_avaliacoes(colecao_com_jogos):
    media = media_avaliacoes(colecao_com_jogos)

    assert media == 8.5

def test_percentual_por_status(colecao_com_jogos):
    percentuais = percentual_por_status(colecao_com_jogos)

    assert percentuais[Status.FINALIZADO] == round((2 / 6) * 100, 2)
    assert percentuais[Status.JOGANDO] == round((3 / 6) * 100, 2)
    assert percentuais[Status.NAO_INICIADO] == round((1 / 6) * 100, 2)

def test_relatorios_com_colecao_vazia():
    c = Colecao("Vazia")

    assert media_horas(c) == 0.0
    assert media_avaliacoes(c) == 0.0

    percentuais = percentual_por_status(c)
    for valor in percentuais.values():
        assert valor == 0

def test_relatorio_texto_basico(colecao_com_jogos):
    texto = relatorio_texto(colecao_com_jogos)

    assert "RESUMO DA COLEÇÃO" in texto
    assert "TOP 5 POR HORAS" in texto
    assert "MÉDIAS" in texto
    assert "STATUS (%)" in texto
