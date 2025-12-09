from source.dominio.usuario import Usuario
from source.dominio.colecao import Colecao
from source.dados.relatorios import relatorio_texto


# LOGIN E CARREGAMENTO

def login():
    try:
        usuario = Usuario.carregar()
        print(f"\nBem-vindo de volta, {usuario.nome}!")

        senha = input("Senha: ")
        while not usuario.validar_senha(senha):
            print("Senha incorreta.")
            senha = input("Tente novamente: ")

        return usuario

    except FileNotFoundError:
        return Usuario.criar_usuario_interativo()


def carregar_colecao():
    try:
        colecao = Colecao.carregar("source/dados/jogos.json")
        print("Coleção carregada com sucesso.")
    except FileNotFoundError:
        print("Nenhuma coleção encontrada. Criando nova...")
        colecao = Colecao("Minha Coleção")

    return colecao


# FUNÇÕES DO SISTEMA

def adicionar_jogo(colecao):
    print("\n=== Adicionar Jogo ===")
    titulo = input("Título: ")
    genero = input("Gênero: ")
    plataforma = input("Plataforma (PC/Console/Mobile): ")
    ano = input("Ano de lançamento: ")

    colecao.adicionar(titulo, genero, plataforma, ano)
    print(f"Jogo '{titulo}' adicionado com sucesso!")


def listar_jogos(colecao):
    print("\n=== Lista de Jogos ===")
    for jogo in colecao.listar():
        print(jogo)


def salvar_colecao(colecao):
    colecao.salvar("source/dados/jogos.json")
    print("Coleção salva.")


def mostrar_relatorio(colecao):
    print("\n=== RELATÓRIO ===")
    print(relatorio_texto(colecao))

def filtrar_jogos(colecao):
    print("\n=== FILTRAR JOGOS ===")

    genero = input("Filtrar por gênero (deixe vazio para escolher outro filtro): ").strip()
    genero = genero if genero else None

    plataforma = input("Filtrar por plataforma (deixe vazio para escolher outro filtro): ").strip()
    plataforma = plataforma if plataforma else None

    status = input("Filtrar por status (NAO_INICIADO/INICIADO/FINALIZADO ou vazio): ").strip()
    status = status if status else None

    try:
        resultados = colecao.filtrar(genero = genero, plataforma = plataforma, status = status)
    except ValueError as e:
        print(f"Erro: {e}")
        return
    
    print("\n=== RESULTADOS DO FILTRO ===")
    if not resultados:
        print("Nenhum jogo encontrado.")
    else:
        for j in resultados:
            print(j)

def ordenar_jogos(colecao):
    print("\n=== ORDENAR JOGOS ===")
    print("Campos disponíveis: titulo, genero, plataforma, ano, horas, avaliacao, status")

    campo = input("Ordenar por: ").strip().lower()
    reverso = input("Ordem reversa? (s/n): ").strip().lower() == "s"

    try:
        ordenados = colecao.ordenar_por(campo, reverso=reverso)
    except ValueError as e:
        print(f"Erro: {e}")
        return

    print("\n=== JOGOS ORDENADOS ===")
    for j in ordenados:
        print(j)


# MENU

def menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Adicionar jogo")
    print("2 - Listar jogos")
    print("3 - Salvar coleção")
    print("4 - Exibir relatório inicial")
    print("5 - Filtrar jogos")
    print("6 - Ordenar jogos")
    print("0 - Sair")


# LOOP PRINCIPAL

def executar():
    usuario = login()
    colecao = carregar_colecao()

    while True:
        menu()
        opcao = input("> ").strip()

        if opcao == "1":
            adicionar_jogo(colecao)

        elif opcao == "2":
            listar_jogos(colecao)

        elif opcao == "3":
            salvar_colecao(colecao)

        elif opcao == "4":
            mostrar_relatorio(colecao)

        elif opcao == "5":
            filtrar_jogos(colecao)

        elif opcao == "6":
            ordenar_jogos(colecao)

        elif opcao == "0":
            print(f"Tchau, {usuario.nome}!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar()
