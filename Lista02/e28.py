import math

# Entrada dos números
x = int(input("Informe o primeiro número inteiro positivo: "))
y = int(input("Informe o segundo número inteiro positivo: "))
z = int(input("Informe o terceiro número inteiro positivo: "))

# Verificação se são positivos
if x <= 0 or y <= 0 or z <= 0:
    print("Todos os números devem ser inseridos positivos.")
else:
    # Menu de opções
    print("Escolha o tipo de Média:")
    print("1 - Geométrica")
    print("2 - Ponderada")
    print("3 - Marmonica")
    print("4 - Aritmética")

    opcao = int(input("Digite a opção (1-4): "))

    if opcao == 1:
        media = (x * y * z) ** (1/3)
        print(f"Média Geométrica: {media:.2f}")
    elif opcao == 2:
        media = (x + 2*y + 3*z) / 6
        print(f"Média Ponderada: {media:.2f}")
    elif opcao == 3:
        media = 1 / ((1/x) + (1/y) + (1/z))
        print(f"Média Harmonica: {media:.2f}")
    elif opcao == 4:
        media = ( x + y + z) / 3
        print(f"Média Aritmética: {media:.2f}")
    else:
        print("Opção Inválida.")