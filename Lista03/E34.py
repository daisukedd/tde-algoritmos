import math

# Função para calcular o MMC usando o MDC (máximo divisor comum)
def calcular_mmc(a, b):
    return abs(a * b) // math.gcd(a, b)

mmc = 1
# Calcula o MMC de todos os números de 2 a 20
for i in range(2, 21): 
    mmc = calcular_mmc(mmc, i)

# Exibe o resultado
print(f"O menor número divisível por todos os números de 1 a 20 é: {mmc}")