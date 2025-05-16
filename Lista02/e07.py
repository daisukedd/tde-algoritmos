# Leitura de dois números fornecidos pelo usuário
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

# Compara os números e exibe o resultado
if n1 > n2:
    print(f"O maior número é: {n1}")
elif n2 > n1:
    print(f"O maior número é: {n2}")
else:
    print("Números iguais.")