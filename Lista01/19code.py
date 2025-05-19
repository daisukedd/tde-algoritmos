# Ler volume em litros e converter para metros cúbicos

while True:
    userInput = input("Digite o volume em litros (L): ")

    try:
        litros = float(userInput)
        metros_cubicos = litros / 1000
        print(f"\n\u2705 Volume em metros cúbicos: {metros_cubicos:.3f} m³ \u2705")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
