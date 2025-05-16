numero = int(input("Digite um número positivo: "))

# Verifica se o número é positivo
if numero <= 0:
    print("Por favor, informe um número positivo.")
else:
    a, b = 0, 1  # Início da sequência de Fibonacci
    print("Sequência de Fibonacci:")

    # Enquanto o valor atual for menor ou igual ao número informado
    while a <= numero:
        print(a, end=' ')
        a, b = b, a + b

    # Exibe o próximo número após a sequência
    print(a)