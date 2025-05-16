# Solicita ao usuário os valores de entrada
n = int(input("Digite a quantidade de números (n): "))
i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))

contador = 0  # Conta quantos números válidos foram encontrados
numero = 0    # Começa a verificar a partir do número 0

# Continua até encontrar n números múltiplos de i ou j
while contador < n:
    if numero % i == 0 or numero % j == 0:
        # Imprime o número com vírgula, exceto o último
        print(numero, end=", " if contador < n - 1 else "")
        contador += 1
    numero += 1