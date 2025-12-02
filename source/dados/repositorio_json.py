import json
from source.dominio.jogo_pc import JogoPC
from source.dominio.jogo_console import JogoConsole
from source.dominio.jogo_mobile import JogoMobile
'''
RESPONSÁVEL POR ARMAZENAR E CONTER DADOS ADQUIRIDOS NO USO DO SISTEMA.
'''

def salvar_jogos(jogos, caminho="source/dados/jogos.json"):
    lista = [j.to_dict() for j in jogos]
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def carregar_jogos(caminho="source/dados/jogos.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    jogos = []
    for d in dados:
        tipo = d["tipo"]

        if tipo == "PC":
            cls = JogoPC
        elif tipo == "Console":
            cls = JogoConsole
        elif tipo == "Mobile":
            cls = JogoMobile
        else:
            raise ValueError(f"Tipo desconhecido: {tipo}")

        jogos.append(cls.from_dict(d))

    return jogos

