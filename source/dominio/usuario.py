import json
import os

class Usuario:
    """
    Representa o usuário do sistema
    
    """

    def __init__(self, nome: str, senha: str, meta_anual: int = 0):
        self.nome = nome
        self.senha = senha
        self.meta_anual = meta_anual

    # PERSISTÊNCIA:

    def salvar(self, caminho="source/dados/usuario.json"):
        dados = {
            "nome": self.nome,
            "senha": self.senha,
            "meta_anual": self.meta_anual
        }
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4)

    @classmethod
    def carregar(cls, caminho="source/dados/usuario.json"):
        if not os.path.exists(caminho):
            raise FileNotFoundError("Arquivo de usuário não encontrado.")

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        return cls(
            nome=dados["nome"],
            senha=dados["senha"],
            meta_anual=dados.get("meta_anual", 0)
        )


    # REGRAS DE NEGÓCIO:

    def atualizar_meta_anual(self, nova_meta: int):
        if nova_meta < 0:
            raise ValueError("Meta anual não pode ser negativa.")
        self.meta_anual = nova_meta

    def validar_senha(self, senha_digitada: str) -> bool:
        return senha_digitada == self.senha

    # CLI:

    @classmethod
    def criar_usuario_interativo(cls):
        print("Nenhum usuário encontrado. Vamos criar um.")
        nome = input("Nome ou nickname: ")
        senha = input("Crie uma senha: ")

        while True:
            try:
                meta = int(input("Meta anual de horas (0 se não quiser definir agora): "))
                break
            except ValueError:
                print("Digite um número válido para a meta.")

        user = cls(nome, senha, meta)
        user.salvar()
        print("Usuário criado com sucesso.")
        return user
