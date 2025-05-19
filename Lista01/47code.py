numero = int(input("Digite um número de 4 dígitos: "))

milhar = numero // 1000
resto = numero % 1000

centena = resto // 100
resto = resto % 100

dezena = resto // 10
unidade = resto % 10

print(milhar)
print(centena)
print(dezena)
print(unidade)
