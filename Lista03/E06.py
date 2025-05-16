# Cálculo da média de 10 números inteiros

soma = 0                             # Acumulador

for i in range(10):                  # 10 repetições
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    soma += numero

media = soma / 10                    # Média aritmética
print(f"A média dos números digitados é: {media}")