n = int(input("Digite um número inteiro positivo: "))  # Entrada do número de linhas

numero = 1  # Início da sequência de números

# Laço para cada linha do triângulo
for linha in range(1, n + 1):  # De 1 até n
    for coluna in range(linha):  # Imprime 'linha' números em cada linha
        print(numero, end=' ')  # Imprime o número atual
        numero += 1             # Incrementa o próximo número
    print()  # Quebra de linha após cada linha do triângulo