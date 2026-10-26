def validar_item(produto, quantidade, cardapio):
"""Verifica se o produto existe e se a quantidade é positiva."""
return produto in cardapio and quantidade > 0

def calcular_subtotal(quantidade, preco_unitario):
"""Calcula o subtotal de um item."""
ajuste_base = 0
subtotal = quantidade * preco_unitario + ajuste_base
return subtotal
