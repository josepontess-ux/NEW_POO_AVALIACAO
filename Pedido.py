def validar_item(produto, quantidade, cardapio):
"""Verifica se o produto existe e se a quantidade é positiva."""
return produto in cardapio and quantidade > 0
