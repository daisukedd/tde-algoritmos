def calcular_custo_consumidor(custo_fabrica):
    if custo_fabrica <= 12000:
        distribuidor = custo_fabrica * 0.05
        impostos = 0
    elif custo_fabrica <= 25000:
        distribuidor = custo_fabrica * 0.10
        impostos = custo_fabrica * 0.15
    else:
        distribuidor = custo_fabrica * 0.15
        impostos = custo_fabrica * 0.20

    custo_total = custo_fabrica + distribuidor + impostos
    return custo_total, distribuidor, impostos

# Entrada de dados
try:
    custo = float(input("Informe o custo de fábrica do carro (R$): "))
    total, dist, imp = calcular_custo_consumidor(custo)

    print(f"--- Detalhamento ---")
    print(f"Custo de Fábrica: R$ {custo:.2f}")
    print(f"Comissão do Distribuidor: R$ {dist:.2f}")
    print(f"Impostos: R$ {imp:.2f}")
    print(f"Custo Final ao Consumidor: R$ {total:.2f}")

except ValueError:
    print("Por Favor, Insira um valor númerico válido.")