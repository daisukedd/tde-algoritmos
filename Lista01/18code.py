#  Ler volume em metros cúbicos e converter para litros

while True:
    userInput = input("Digite o volume em metros cúbicos (m³): ")

    try:
        metros_cubicos = float(userInput)
        litros = 1000 * metros_cubicos
        print(f"\n\u2705 Volume em litros: {litros:.2f} L \u2705")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
