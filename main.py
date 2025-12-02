from source.dominio.colecao import Colecao
from source.dados.relatorios import relatorio_texto

def carregar_colecao():
    try:
        colecao = Colecao.carregar("jogos.json")
        print("Coleção carregada com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado, criando coleção nova...")
        colecao = Colecao("Minha Coleção")
    return colecao

def menu():
    print("\n=== MENU ===")
    print("1 - Adicionar jogo")
    print("2 - Listar jogos")
    print("3 - Salvar coleção")
    print("4 - Exibir relatório inicial")   # <--- IMPORTANTE
    print("0 - Sair")

def executar():
    colecao = carregar_colecao()

    while True:
        menu()
        opcao = input("> ")

        if opcao == "1":
            # adicionar jogo aqui
            pass

        elif opcao == "2":
            for jogo in colecao.listar():
                print(jogo)

        elif opcao == "3":
            colecao.salvar("jogos.json")
            print("Coleção salva.")

        elif opcao == "4":
            print("\n=== RELATÓRIO ===")
            print(relatorio_texto(colecao))

        elif opcao == "0":
            break

if __name__ == "__main__":
    executar()
