from source.utils.cores import Cor, colorir
from source.dominio.jogo import Jogo
from source.dominio.usuario import Usuario
from source.dominio.colecao import Colecao
from source.dados.relatorios import (
    relatorio_texto,
    top_5_por_horas,
    media_horas,
    media_avaliacoes,
    percentual_por_status
)
from source.dados.settings import CAMINHO_JOGOS



# LOGIN E CARREGAMENTO

def login():
    try:
        usuario = Usuario.carregar()
        print(colorir(f"\nBem-vindo de volta, {usuario.nome}!", Cor.VERDE))

        senha = input("Senha: ")
        while not usuario.validar_senha(senha):
            print(colorir("Senha incorreta.", Cor.AMARELO))
            senha = input("Tente novamente: ")

        return usuario

    except FileNotFoundError:
        return Usuario.criar_usuario_interativo()


def carregar_colecao():
    try:
        colecao = Colecao.carregar(CAMINHO_JOGOS)
        print(colorir("Coleção carregada com sucesso.", Cor.VERDE))
    except FileNotFoundError:
        print(colorir("Nenhuma coleção encontrada. Criando nova...", Cor.AZUL))
        colecao = Colecao("Minha Coleção")

    return colecao


# FUNÇÕES DO SISTEMA

def adicionar_jogo(colecao):
    print(colorir("\n=== Adicionar Jogo ===", Cor.CIANO))
    titulo = input("Título: ")
    genero = input("Gênero: ")
    plataforma = input("Plataforma (PC/Console/Mobile): ")
    ano = input("Ano de lançamento: ")

    jogo = Jogo(titulo, genero, plataforma, ano)
    colecao.adicionar(jogo)
    print(colorir(f"Jogo '{titulo}' adicionado com sucesso!", Cor.VERDE))


def listar_jogos(colecao):
    print(colorir("\n=== Lista de Jogos ===", Cor.CIANO))
    for jogo in colecao.listar():
        print(jogo)


def salvar_colecao(colecao):
    colecao.salvar(CAMINHO_JOGOS)
    print(colorir("Coleção salva.", Cor.VERDE))


def executar_relatorios(colecao):
    while True:
        menu_relatorios()
        opcao = int(input("> ").strip())

        if opcao == 1:
            print(colorir(relatorio_texto(colecao), Cor.AZUL))

        elif opcao == 2:
            print(colorir("\n=== TOP 5 POR HORAS JOGADAS ===", Cor.AZUL))
            top5 = top_5_por_horas(colecao)
            if not top5:
                print(colorir("Nenhum jogo com horas registradas.", Cor.AMARELO))
            else:
                for j in top5:
                    print(f"- {j.titulo}: {j.horas}h")

        elif opcao == 3:
            print(colorir("\n=== MÉDIAS ===", Cor.AZUL))
            print(colorir(f"Média de horas jogadas: {media_horas(colecao)}h", Cor.AZUL))
            print(colorir(f"Média de avaliações: {media_avaliacoes(colecao)}", Cor.AZUL))

        elif opcao == 4:
            print(colorir("\n=== STATUS (%) ===", Cor.AZUL))
            percentuais = percentual_por_status(colecao)
            for status, pct in percentuais.items():
                print(f"{status.value}: {pct}%")

        elif opcao == 0:
            break

        else:
            print(colorir("Opção inválida.", Cor.VERMELHO))


def filtrar_jogos(colecao):
    print(colorir("\n=== FILTRAR JOGOS ===", Cor.CIANO))

    genero = input("Filtrar por gênero (deixe vazio para escolher outro filtro): ").strip()
    genero = genero if genero else None

    plataforma = input("Filtrar por plataforma (deixe vazio para escolher outro filtro): ").strip()
    plataforma = plataforma if plataforma else None

    status = input("Filtrar por status (NAO_INICIADO/INICIADO/FINALIZADO ou vazio): ").strip()
    status = status if status else None

    try:
        resultados = colecao.filtrar(genero = genero, plataforma = plataforma, status = status)
    except ValueError as e:
        print(colorir(f"Erro: {e}", Cor.VERMELHO))
        return
    
    print(colorir("\n=== RESULTADOS DO FILTRO ===", Cor.CIANO))
    if not resultados:
        print(colorir("Nenhum jogo encontrado.", Cor.AMARELO))
    else:
        for j in resultados:
            print(j)

def ordenar_jogos(colecao):
    print(colorir("\n=== ORDENAR JOGOS ===", Cor.CIANO))
    print(colorir("Campos disponíveis: titulo, genero, plataforma, ano, horas, avaliacao, status", Cor.CIANO))

    campo = input("Ordenar por: ").strip().lower()
    reverso = input("Ordem reversa? (s/n): ").strip().lower() == "s"

    try:
        ordenados = colecao.ordenar_por(campo, reverso=reverso)
    except ValueError as e:
        print(colorir(f"Erro: {e}", Cor.VERMELHO))
        return

    print(colorir("\n=== JOGOS ORDENADOS ===", Cor.CIANO))
    for j in ordenados:
        print(j)

def escolher_jogo(colecao):
    jogos = colecao.listar()

    if not jogos:
        print(colorir("Nenhum jogo cadastrado.", Cor.AMARELO))
        return None
    
    print(colorir("\n=== ESCOLHA UM JOGO ===", Cor.CIANO))
    for i, jogo in enumerate(jogos, start=1):
        print(f"{i} - {jogo}")
    try:
        opcao = int(input("> "))
        return jogos[opcao-1]
    except(ValueError, IndexError):
        print(colorir("Escolha inválida.", Cor.VERMELHO))
        return None

def atualizar_horas(colecao):
    jogo = escolher_jogo(colecao)

    if not jogo:
        return
    
    try:
        horas = float(input("Quantas horas pretende adicionar?: "))
        jogo.adicionar_horas(horas)
        print(colorir("Horas atualizadas com sucesso.", Cor.VERDE))
    except ValueError as e:
        print(colorir(f"Erro: {e}", Cor.VERMELHO))

def finalizar_jogo(colecao):
    jogo = escolher_jogo(colecao)
    if not jogo:
        return
    
    try:
        jogo.finalizar()
        print(colorir("Jogo finalizado com sucesso!", Cor.VERDE))
    except ValueError as e:
        print(colorir(f"Erro: {e}", Cor.VERMELHO))

def reiniciar_jogo(colecao):
    jogo = escolher_jogo(colecao)
    if not jogo:
        return
    
    try:
        jogo.reiniciar()
        print(colorir("Jogo reiniciado!", Cor.VERDE))
    except ValueError as e:
        print(colorir(f"Erro: {e}", Cor.VERMELHO))

def avaliar_jogo(colecao):
    jogo = escolher_jogo(colecao)
    if not jogo:
        return
    
    try:
        nota = int(input("Digite a nota do jogo:\n> "))
        jogo.avaliacao = nota
        print(colorir("Jogo avaliado com sucesso.", Cor.VERDE))
    except ValueError as e:
        print(colorir(f"Erro: {e}", Cor.VERMELHO))

# MENUS

def menu():
    print(colorir("\n=== MENU PRINCIPAL ===", Cor.CIANO))
    print(colorir("1 - Adicionar jogo", Cor.CIANO))
    print(colorir("2 - Listar jogos", Cor.CIANO))
    print(colorir("3 - Salvar coleção", Cor.CIANO))
    print(colorir("4 - Relatórios", Cor.CIANO))
    print(colorir("5 - Filtrar jogos", Cor.CIANO))
    print(colorir("6 - Ordenar jogos", Cor.CIANO))
    print(colorir("7 - Atualizar horas jogadas", Cor.CIANO))
    print(colorir("8 - Finalizar jogo", Cor.CIANO))
    print(colorir("9 - Reiniciar jogo", Cor.CIANO))
    print(colorir("10 - Avaliar jogo", Cor.CIANO))
    print(colorir("0 - Sair", Cor.CIANO))

def menu_relatorios():
    print(colorir("\n=== RELATÓRIOS ===", Cor.CIANO))
    print(colorir("1 - Relatório Geral", Cor.AZUL))
    print(colorir("2 - Top 5 por horas jogadas", Cor.AZUL))
    print(colorir("3 - Médias", Cor.AZUL))
    print(colorir("4 - Percentual por status", Cor.AZUL))
    print(colorir("0 - Voltar", Cor.CIANO))

# LOOP PRINCIPAL

def executar():
    usuario = login()
    colecao = carregar_colecao()

    while True:
        menu()
        opcao = int(input("> ").strip())

        if opcao == 1:
            adicionar_jogo(colecao)

        elif opcao == 2:
            listar_jogos(colecao)

        elif opcao == 3:
            salvar_colecao(colecao)

        elif opcao == 4:
            executar_relatorios(colecao)

        elif opcao == 5:
            filtrar_jogos(colecao)

        elif opcao == 6:
            ordenar_jogos(colecao)

        elif opcao == 7:
            atualizar_horas(colecao)

        elif opcao == 8:
            finalizar_jogo(colecao)
        
        elif opcao == 9:
            reiniciar_jogo(colecao)

        elif opcao == 10:
            avaliar_jogo(colecao)

        elif opcao == 0:
            print(colorir(f"Tchau, {usuario.nome}!", Cor.CIANO))
            break
        

        else:
            print(colorir("Opção inválida. Tente novamente.", Cor.AMARELO))


if __name__ == "__main__":
    executar()
