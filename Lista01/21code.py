#  Ler massa em libras e converter para quilogramas

while True:
    userInput = input("Digite a massa em libras (lbs): ")

    try:
        libras = float(userInput)
        quilogramas = libras * 0.45
        print(f"\n\u2705 Massa em quilogramas: {quilogramas:.2f} kg \u2705")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
