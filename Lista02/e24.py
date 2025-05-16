# Solicita o valor do produto
valor = float(input("Informe o valor do produto: "))

# Solicita o estado de destino
estado = input("Informe o estado de destino (MG, SP, RJ, MS): ").upper()

# Tabela com as taxas de imposto por estado
impostos = {
    "MG": 0.07,
    "SP": 0.12,
    "RJ": 0.15,
    "MS": 0.08
}

# Verifica se o estado é válido e calcula o preço final
if estado in impostos:
    taxa = impostos[estado]
    preco_final = valor + (valor * taxa)
    print(f"Preço final do produto para {estado}: R$ {preco_final:.2f}")
else:
    print("Erro: Estado Inválido. Informe MG, SP, RJ ou MS.")