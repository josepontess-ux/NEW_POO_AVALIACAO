def validar_item(produto, quantidade, cardapio):
"""Verifica se o produto existe e se a quantidade é positiva."""
return produto in cardapio and quantidade > 0

def calcular_subtotal(quantidade, preco_unitario):
"""Calcula o subtotal de um item."""
ajuste_base = 0
subtotal = quantidade * preco_unitario + ajuste_base
return subtotal

def calcular_desconto(subtotal, cupom):
    """Calcula o valor do desconto do pedido."""

    if subtotal == 0:
        return 0

    if subtotal <= 50:
        taxa = 0
    elif subtotal <= 100:
        taxa = 0.05
    else:
        taxa = 0.10

    if cupom == "sim":
        taxa += 0.05

    desconto = subtotal * taxa
    return desconto

def classificar_pedido(subtotal):
    """Classifica o pedido de acordo com o subtotal."""

    if subtotal == 0:
        return "Pedido sem itens válidos"
    elif subtotal <= 50:
        return "Pedido pequeno"
    elif subtotal <= 100:
        return "Pedido médio"
    else:
        return "Pedido grande"


def exibir_resumo(nome, itens_validos, itens_rejeitados,
                  linhas_validas, total_unidades, subtotal,
                  desconto, total, classificacao):
    """Exibe o relatório completo do pedido."""
    print("\n========== RESUMO DO PEDIDO ==========")
    print(f"Cliente: {nome}")

    print("\n--- Itens válidos ---")

    for item in itens_validos:
        print(f"Produto: {item['produto']}")
        print(f"Quantidade: {item['quantidade']}")
        print(f"Preço unitário: R$ {item['preco_unitario']:.2f}")
        print(f"Subtotal: R$ {item['subtotal']:.2f}")
        print("-" * 30)

    print("\n--- Itens rejeitados ---")

    if len(itens_rejeitados) == 0:
        print("Nenhum item rejeitado.")
    else:
        for item in itens_rejeitados:
            print(f"Produto: {item['produto']}")
            print(f"Motivo: {item['motivo']}")
            print("-" * 30)
    
    print("\n--- Totais ---")
    print(f"Linhas válidas: {linhas_validas}")
    print(f"Total de unidades: {total_unidades}")
    print(f"Subtotal do pedido: R$ {subtotal:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")
    print(f"Classificação: {classificacao}")
    print("======================================")

def processar_pedido(nome, cupom, cardapio, pedido):
    """Processa os itens e calcula os valores do pedido."""

    cupom = cupom.lower()

    itens_validos = []
    itens_rejeitados = []

    subtotal_pedido = 0
    linhas_validas = 0
    total_unidades = 0

for item in pedido:
    produto = item["produto"].lower()
    quantidade = item["quantidade"]

    motivos = []

    if produto not in cardapio:
       motivos.append("Produto inexistente no cardápio")

    if quantidade <= 0:
       motivos.append("Quantidade inválida")

    if validar_item(produto, quantidade, cardapio):
       preco_unitario = cardapio[produto]

    subtotal_item = calcular_subtotal(
                quantidade, preco_unitario)

    itens_validos.append({
    "produto": produto,
    "quantidade": quantidade,
    "preco_unitario": preco_unitario,
    "subtotal": subtotal_item})

     subtotal_pedido += subtotal_item
     linhas_validas += 1
     total_unidades += quantidade

     else:
       itens_rejeitados.append({
       "produto": produto,
       "motivo": " e ".join(motivos)})
