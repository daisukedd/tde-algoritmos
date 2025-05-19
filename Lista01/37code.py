# Produto com desconto de 12%

try:
    # Solicitar ao usuário o valor do produto
    valor_produto = float(input("Digite o valor do produto: R$ "))

    # Calcular o valor com o desconto de 12%
    desconto = valor_produto * 0.12
    valor_com_desconto = valor_produto - desconto

    print("\n📊 Resultado")
    print(f"Valor do produto: R$ {valor_produto:.2f}")
    print(f"Desconto de 12%: R$ {desconto:.2f}")
    print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
except ValueError:
    print("❌ Erro: por favor, digite um valor numérico válido.")
