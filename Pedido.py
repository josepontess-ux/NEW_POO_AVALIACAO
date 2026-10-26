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
