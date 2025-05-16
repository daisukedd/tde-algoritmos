# Lê um número do usuário
numero = int(input("Digite um número inteiro: "))

# Inicializa a variável de busca
proximo = numero + 1

# Loop até encontrar um múltiplo de 11, 13 ou 17
while True:
    if proximo % 11 == 0 or proximo % 13 == 0 or proximo % 17 == 0:
        print(f"O primeiro múltiplo de 11, 13 ou 17 após {numero} é: {proximo}")
        break
    proximo += 1