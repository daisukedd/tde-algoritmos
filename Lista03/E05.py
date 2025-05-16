# Soma de 10 valores fornecidos pelo usuário

soma = 0                             # Acumulador

for i in range(1, 11):               # Loop de 1 a 10
    valor = float(input(f"Digite o {i}º valor: "))  # Lê valor
    soma += valor                    # Soma

print(f"A soma dos 10 valores é: {soma}")