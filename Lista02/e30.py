# Recebe 3 números do usuário
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Coloca os números em uma lista e ordena
numeros = [n1, n2, n3]
numeros.sort()

# Mostra os números em ordem crescente
print("Números em ordem crescente: ")
for n in numeros:
    print(n)