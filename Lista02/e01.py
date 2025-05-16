# Recebendo os dois números do usuário
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

# Comparando os números
if n1 > n2:
    print(f"O maior número é: {n1}")
elif n2 > n1:
    print(f"O maior número é: {n2}")
else:
    print("Os dois números são iguais.")