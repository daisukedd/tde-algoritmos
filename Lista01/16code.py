# Ler comprimento em polegadas e converter para centímetros
# Uma polegada é igual a 2,54 centímetros ou 25,4 milímetros

while True:
    userInput = input("Digite o comprimento em polegadas: ")

    try:
        polegadas = float(userInput)
        centimetros = polegadas * 2.54
        print(f"\n\u2705 Comprimento em centímetros: {centimetros:.2f} cm \u2705")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
