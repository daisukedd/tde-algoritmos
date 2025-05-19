try:

    valor_total = float(input("Digite o valor total da venda R$: "))

    valor_desconto = valor_total * 0.10
    valor_com_desconto = valor_total - valor_desconto

    valor_parcela = valor_total / 3

    comissao_vista = valor_com_desconto * 0.05

    comissao_parcelada = valor_total * 0.05

    # Show resultados
    print("\n📊 RESUMO DA VENDA")
    print(f"Valor total da venda: R$ {valor_total:.2f}")
    print(f"Total a pagar à vista com 10% de desconto: R$ {valor_com_desconto:.2f}")
    print(f"Valor de cada parcela (3x sem juros): R$ {valor_parcela:.2f}")
    print(f"Comissão do vendedor - Venda à vista): R$ {comissao_vista:.2f}")
    print(f"Comissão do vendedor - Venda parcelada): R$ {comissao_parcelada:.2f}")

except ValueError:
    print("❌ Erro: Por favor, digite um valor numérico válido.")
