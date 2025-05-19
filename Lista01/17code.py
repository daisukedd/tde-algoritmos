# Ler comprimento em centímetros e converter para polegadas

while True:
    userInput = input("Digite o comprimento em centímetros: ")

    try:
        centimetros = float(userInput)
        polegadas = centimetros / 2.54
        print(f"\n\u2705 Comprimento em polegadas: {polegadas:.2f} in \u2705")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
