from source.dominio.jogo import Status

def top_5_por_horas(colecao):
    jogos = [j for j in colecao.listar() if j.horas > 0]
    jogos_ordenados = sorted(jogos, key=lambda j: j.horas, reverse=True)
    return jogos_ordenados[:5]

def media_horas(colecao):
    jogos = [j for j in colecao.listar() if j.horas > 0]
    if not jogos:
        return 0.0
    total = sum(j.horas for j in jogos)
    return round(total / len(jogos), 2)

def media_avaliacoes(colecao):
    jogos = [j for j in colecao.listar() if j.avaliacao is not None]
    if not jogos:
        return 0.0
    total = sum(j.avaliacao for j in jogos)
    return round(total / len(jogos), 2)

def percentual_por_status(colecao):
    total = len(colecao)
    if total == 0:
        return {status: 0 for status in Status}

    contagem = {status: 0 for status in Status}

    for jogo in colecao.listar():
        contagem[jogo.status] += 1

    return {
        status: round((qtd / total) * 100, 2)
        for status, qtd in contagem.items()
    }

def relatorio_texto(colecao):
    linhas = []

    linhas.append("=== RESUMO DA COLEÇÃO ===")
    linhas.append(f"Total de jogos: {len(colecao)}")

    linhas.append("\n=== TOP 5 POR HORAS JOGADAS ===")
    for j in top_5_por_horas(colecao):
        linhas.append(f"- {j.titulo}: {j.horas}h")

    linhas.append("\n=== MÉDIAS ===")
    linhas.append(f"Média de horas jogadas: {media_horas(colecao)}h")
    linhas.append(f"Média de avaliações: {media_avaliacoes(colecao)}")

    linhas.append("\n=== STATUS (%) ===")
    percentuais = percentual_por_status(colecao)
    for status, pct in percentuais.items():
        linhas.append(f"{status.value}: {pct}%")

    return "\n".join(linhas)

