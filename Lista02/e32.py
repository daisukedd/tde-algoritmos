# Cardápio como tabela
cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hamburguer", 1.20),
    104: ("Cheeseburguer", 1.70),
    105: ("Suco", 2.20),
    106: ("Refrigerante", 1.00)
}

# Entrada do usuário
codigo = int(input("Informe o código do produto: "))
quantidade = int(input("Informe a quantidade: "))

# Verifica se o código é válido
if codigo in cardapio:
    produto, preco = cardapio[codigo]
    total = preco * quantidade
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Total a pagar: R$ {total:.2f}")
else:
    print("Código Inválido.")