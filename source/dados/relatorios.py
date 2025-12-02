def relatorio_inicial(colecao):
    """
    Gera um relatório simples da coleção:
    - total de jogos
    - total de horas jogadas
    """

    total_jogos = len(colecao)
    total_horas = sum(j.horas for j in colecao.listar())

    return {
        "total_jogos": total_jogos,
        "total_horas": total_horas
    }


def relatorio_texto(colecao):
    """
    Retorna uma string formatada para exibir ao usuário ou salvar em .txt
    """
    dados = relatorio_inicial(colecao)

    return (
        f"Relatório da Coleção '{colecao.nome}':\n"
        f"- Total de jogos: {dados['total_jogos']}\n"
        f"- Total de horas jogadas: {dados['total_horas']}\n"
    )
