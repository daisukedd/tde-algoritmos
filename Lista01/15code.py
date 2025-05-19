# Ler um ângulo em radianos e converter para graus

while True:
    userInput = input("Digite um ângulo em radianos: ")

    try:
        rad = float(userInput)
        pi = 3.14
        graus = rad * 180 / pi
        print(f"\n\u2705 Ângulo em graus: {graus:.2f}° \u2705")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
