import math

# Leitura de um número inteiro fornecido pelo usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é válido
if numero > 0:
    logaritmo = math.log10(numero)
    print(f"O logaritmo de {numero} na base 10 é: {logaritmo:.4f}")
else:
    print("Número inválido. O número deve ser maior que zero.")