# Ler massa em quilogramas e converter para libras
# Uma libra equivale a 0,45 quilogramas

while True:
    userInput = input("Digite a massa em quilogramas (kg): ")

    try:
        quilogramas = float(userInput)
        libras = quilogramas / 0.45
        print(f"\n\u2705 Massa em libras: {libras:.2f} lbs \u2705")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
