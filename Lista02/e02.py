import math

# Leitura de um número fornecido pelo usuário
n = float(input("Informe um número: "))

# Verifica se o número é positivo
if n >= 0:
    raiz = math.sqrt(n)
    print(f"A raiz quadrada de {n} é {raiz:.2f}")
else:
    print("Número inválido! Não é possível calcular a raiz quadrada de um número negativo.")