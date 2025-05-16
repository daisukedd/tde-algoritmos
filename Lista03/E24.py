# Lê um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Inicializa a soma dos divisores
soma_divisores = 0

# Percorre todos os números de 1 até número - 1
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

print(f"A soma dos divisores de {numero}, exceto ele próprio, é: {soma_divisores}")