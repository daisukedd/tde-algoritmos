# Laço contínuo até o usuário inserir valores válidos
while True:
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))

    # Verifica se os valores são válidos
    if base > 0 and altura > 0:
        area = (base * altura) / 2
        print(f"A área do triângulo é: {area}")
        break
    else:
        print("Entrada inválida. A base e a altura devem ser maiores que 0. Tente novamente.\n")