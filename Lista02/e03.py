# Leitura de um número real fornceido pelo usuário
n = float(input("Informe um número real: "))

# Verifica se o número é positivo
if n >= 0:
    raiz = n ** 0.5
    print(f"A raiz quadrada de {n} é {raiz:.2f}")
else:
    quadrado = n ** 2
    print(f"O número ao quadrado é {quadrado:.2f}")