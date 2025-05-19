# Ler um ângulo em graus e converter para radianos
# A definição de radiano considera a medida de um ângulo central de uma circunferência e relaciona o arco determinado por esse ângulo com o raio da circunferência

while True:
    userInput = input("Digite um ângulo em Graus: ")

    try:
        graus = float(userInput)
        pi = 3.14
        radianos = graus * pi / 180
        print(f"\n\u27b0 Ângulo em Radianos: {radianos:.4f} rad \u27b0")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
