import json
from source.dominio.jogo import Jogo
from source.dominio.colecao import Colecao

def test_salvar_e_carregar(tmp_path):
    caminho = tmp_path / "jogos.json"

    c = Colecao("Teste")
    c.adicionar(Jogo("Hades", "Roguelike", "Switch"))
    c.salvar(caminho)

    nova = Colecao.carregar(caminho)
    assert len(nova) == 1
    assert nova.listar()[0].titulo == "Hades"
